import typing

from open_feature.exception.exceptions import GeneralError
from open_feature.open_feature_client import OpenFeatureClient
from open_feature.provider.no_op_provider import NoOpProvider
from open_feature.provider.provider import AbstractProvider

_provider: typing.Optional[AbstractProvider] = None


def get_client(
    name: typing.Optional[str] = None, version: typing.Optional[str] = None
) -> OpenFeatureClient:
    if _provider is None:
        return NoOpProvider()
    return OpenFeatureClient(name=name, version=version, provider=_provider)


def set_provider(provider: AbstractProvider):
    global _provider
    if provider is None:
        raise GeneralError(error_message="No provider")
    _provider = provider


def get_provider() -> typing.Optional[AbstractProvider]:
    global _provider
    return _provider
