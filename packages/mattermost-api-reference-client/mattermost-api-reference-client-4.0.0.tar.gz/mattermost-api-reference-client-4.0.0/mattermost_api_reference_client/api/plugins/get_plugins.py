from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_plugins_response_200 import GetPluginsResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/plugins".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GetPluginsResponse200]]:
    if response.status_code == 200:
        response_200 = GetPluginsResponse200.from_dict(response.json())

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
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, GetPluginsResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, GetPluginsResponse200]]:
    """Get plugins

     Get a list of inactive and a list of active plugin manifests. Plugins must be enabled in the
    server's config settings.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 4.4

    Returns:
        Response[Union[Any, GetPluginsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[Any, GetPluginsResponse200]]:
    """Get plugins

     Get a list of inactive and a list of active plugin manifests. Plugins must be enabled in the
    server's config settings.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 4.4

    Returns:
        Response[Union[Any, GetPluginsResponse200]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, GetPluginsResponse200]]:
    """Get plugins

     Get a list of inactive and a list of active plugin manifests. Plugins must be enabled in the
    server's config settings.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 4.4

    Returns:
        Response[Union[Any, GetPluginsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[Any, GetPluginsResponse200]]:
    """Get plugins

     Get a list of inactive and a list of active plugin manifests. Plugins must be enabled in the
    server's config settings.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 4.4

    Returns:
        Response[Union[Any, GetPluginsResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
