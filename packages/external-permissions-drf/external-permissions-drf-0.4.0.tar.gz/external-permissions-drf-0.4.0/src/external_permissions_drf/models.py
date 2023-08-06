from datetime import datetime
from typing import Any, Tuple, Union

from django.db import models
from django.utils import timezone

from external_permissions_drf.services.keys import KeyGenerator
from external_permissions_drf.services.permissions import Read, ReadAndWrite


class BaseAPIKeyManager(models.Manager):
    key_generator = KeyGenerator()

    def create(self, **kwargs: Any) -> None:
        raise NotImplementedError("Use create_key instead.")

    def create_key(
        self,
        store_subdomain: str,
        resource_permissions: list[Union[Read, ReadAndWrite]],
        expiry_date: datetime = None,
    ) -> Tuple["AbstractAPIKey", str]:
        """
        Format for resource_permissions: [Read("Orders"), ReadAndWrite("Products")]
        """

        key, prefix, hashed_key = self.key_generator.generate()

        api_key = self.model(
            prefix=prefix,
            hashed_key=hashed_key,
            store_subdomain=store_subdomain,
            resource_permissions={
                item.resource: item.permission for item in resource_permissions
            },
            expiry_date=expiry_date,
        )
        api_key.full_clean()
        api_key.save()

        return api_key, key

    def get_from_key(self, key: str) -> "AbstractAPIKey":
        prefix, _, _ = key.partition(".")

        try:
            api_key = self.get(prefix=prefix)
        except self.model.DoesNotExist:
            raise

        if not self.key_generator.verify(key, api_key.hashed_key):
            # Object with given prefix exists but the key is invalid.
            # DoesNotExist must be raised because otherwise an adversary
            # has to guess only the prefix. If db leak were to occur,
            # they could simply generate api keys with prefixes:
            # f"{prefix}.any_random_string"
            raise self.model.DoesNotExist("Key is not valid.")

        return api_key


class APIKeyManager(BaseAPIKeyManager):
    pass


class AbstractAPIKey(models.Model):
    prefix = models.CharField(max_length=100, unique=True, editable=False)
    hashed_key = models.CharField(max_length=100, editable=False)

    store_subdomain = models.CharField(max_length=100)
    # Format: {"orders": 0, "products": 1}
    resource_permissions = models.JSONField()

    expiry_date = models.DateTimeField(blank=True, null=True)
    revoked = models.BooleanField(default=False)

    objects = APIKeyManager()

    class Meta:
        abstract = True

    @property
    def expired(self) -> bool:
        if self.expiry_date is None:
            return False
        return self.expiry_date < timezone.now()

    def get_resource_permission(self, resource: str) -> Union[None, int]:
        return self.resource_permissions.get(resource, None)

    def revoke(self):
        self.revoked = True
        self.save()
