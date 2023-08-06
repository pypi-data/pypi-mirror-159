from collections import namedtuple
from enum import Enum
from typing import TYPE_CHECKING, Any, Type

from django.conf import settings
from django.http import HttpRequest
from rest_framework.permissions import SAFE_METHODS, BasePermission

from external_permissions_drf.services.keys import KeyParser

if TYPE_CHECKING:
    from external_permissions_drf.models import AbstractAPIKey


class Permission(Enum):
    """
    READ_AND_WRITE exists instead of WRITE because often times
    before a write can happen, a read is required. I.e. to update
    a product, first it needs to be retrieved.
    """

    READ = 0
    READ_AND_WRITE = 1


# Read and ReadAndWrite are referred to as "resource permissions"
Read = namedtuple(
    "Read",
    "resource permission",
    defaults=[None, Permission.READ.value],
)
ReadAndWrite = namedtuple(
    "ReadAndWrite",
    "resource permission",
    defaults=[None, Permission.READ_AND_WRITE.value],
)


class BaseHasResourceAccess(BasePermission):
    """
    Subclasses must define "model" and "resource" attributes and
    implement "get_store_subdomain" method.
    """

    model: Type["AbstractAPIKey"]
    resource: str

    key_parser = KeyParser()

    def get_store_subdomain(self, request: HttpRequest) -> str:
        raise NotImplementedError("Subclasses must implement this method.")

    def has_permission(self, request: HttpRequest, view: Any) -> bool:
        key = self.key_parser.get(request)
        if key is None:
            # Client didn't provide key in request
            return False

        try:
            api_key = self.model.objects.get_from_key(key)
        except self.model.DoesNotExist:
            # api key object does not exist in the database
            return False

        if api_key.expired or api_key.revoked:
            return False

        if api_key.store_subdomain != self.get_store_subdomain(request):
            return False

        permission = api_key.get_resource_permission(self.resource)
        if permission is None:
            return False

        if request.method in SAFE_METHODS and permission in [
            Permission.READ.value,
            Permission.READ_AND_WRITE.value,
        ]:
            return True

        if (
            request.method not in SAFE_METHODS
            and permission == Permission.READ_AND_WRITE.value
        ):
            return True

        return False

    def has_object_permission(
        self, request: HttpRequest, view: Any, obj: "AbstractAPIKey"
    ) -> bool:
        return self.has_permission(request, view)


class HasRootAccess(BasePermission):
    key_parser = KeyParser()

    def has_permission(self, request: HttpRequest, view: Any) -> bool:
        key = self.key_parser.get(request)
        if key is None:
            return False
        return key == settings.SERVICE_API_KEY

    def has_object_permission(
        self, request: HttpRequest, view: Any, obj: "AbstractAPIKey"
    ) -> bool:
        return self.has_permission(request, view)
