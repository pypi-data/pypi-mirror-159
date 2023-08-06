from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.install_marketplace_plugin_json_body import InstallMarketplacePluginJsonBody
from ...models.plugin_manifest import PluginManifest
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: InstallMarketplacePluginJsonBody,
) -> Dict[str, Any]:
    url = "{}/plugins/marketplace".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, PluginManifest]]:
    if response.status_code == 200:
        response_200 = PluginManifest.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, PluginManifest]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: InstallMarketplacePluginJsonBody,
) -> Response[Union[Any, PluginManifest]]:
    """Installs a marketplace plugin

     Installs a plugin listed in the marketplace server.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.16

    Args:
        json_body (InstallMarketplacePluginJsonBody):

    Returns:
        Response[Union[Any, PluginManifest]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: InstallMarketplacePluginJsonBody,
) -> Optional[Union[Any, PluginManifest]]:
    """Installs a marketplace plugin

     Installs a plugin listed in the marketplace server.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.16

    Args:
        json_body (InstallMarketplacePluginJsonBody):

    Returns:
        Response[Union[Any, PluginManifest]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: InstallMarketplacePluginJsonBody,
) -> Response[Union[Any, PluginManifest]]:
    """Installs a marketplace plugin

     Installs a plugin listed in the marketplace server.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.16

    Args:
        json_body (InstallMarketplacePluginJsonBody):

    Returns:
        Response[Union[Any, PluginManifest]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: InstallMarketplacePluginJsonBody,
) -> Optional[Union[Any, PluginManifest]]:
    """Installs a marketplace plugin

     Installs a plugin listed in the marketplace server.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.16

    Args:
        json_body (InstallMarketplacePluginJsonBody):

    Returns:
        Response[Union[Any, PluginManifest]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
