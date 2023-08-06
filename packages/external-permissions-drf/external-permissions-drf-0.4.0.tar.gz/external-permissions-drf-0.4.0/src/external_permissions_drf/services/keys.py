from typing import Tuple, Union

from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpRequest
from django.utils.crypto import get_random_string


class KeyGenerator:
    def __init__(self, prefix_length: int = 16, secret_key_length: int = 32) -> None:
        self.prefix_length = prefix_length
        self.secret_key_length = secret_key_length

    def get_prefix(self) -> str:
        return get_random_string(self.prefix_length)

    def get_secret_key(self) -> str:
        return get_random_string(self.secret_key_length)

    def generate(self) -> Tuple[str, str, str]:
        prefix = self.get_prefix()
        secret_key = self.get_secret_key()
        key = f"{prefix}.{secret_key}"
        hashed_key = make_password(key)
        return key, prefix, hashed_key

    def verify(self, key: str, hashed_key: str) -> bool:
        return check_password(key, hashed_key)


class KeyParser:
    keyword = "Api-Key"

    def get(self, request: HttpRequest) -> Union[None, str]:
        custom_header = getattr(settings, "API_KEY_CUSTOM_HEADER", None)
        if custom_header is not None:
            return self.get_from_header(request, custom_header)

        return self.get_from_authorization(request)

    def get_from_authorization(self, request: HttpRequest) -> Union[None, str]:
        authorization = request.META.get("HTTP_AUTHORIZATION")

        if authorization is None:
            return None

        try:
            _, key = authorization.split("{} ".format(self.keyword))
        except ValueError:
            key = None

        return key

    def get_from_header(self, request: HttpRequest, name: str) -> Union[None, str]:
        """
        Unlike authorization header, custom header's value does not start with keyword.

        For example, if you set API_KEY_CUSTOM_HEADER in settings to "HTTP_X_API_KEY",
        then clients must make requests using HTTP_X_API_KEY: foobar, instead of
        HTTP_X_API_KEY: Api-Key foobar
        """
        return request.META.get(name) or None
