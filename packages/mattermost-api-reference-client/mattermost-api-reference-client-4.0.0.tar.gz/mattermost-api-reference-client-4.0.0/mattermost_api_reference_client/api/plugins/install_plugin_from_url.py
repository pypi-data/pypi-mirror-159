from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.status_ok import StatusOK
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    plugin_download_url: str,
    force: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/plugins/install_from_url".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["plugin_download_url"] = plugin_download_url

    params["force"] = force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, StatusOK]]:
    if response.status_code == 201:
        response_201 = StatusOK.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, StatusOK]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    plugin_download_url: str,
    force: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, StatusOK]]:
    """Install plugin from url

     Supply a URL to a plugin compressed in a .tar.gz file. Plugins must be enabled in the server's
    config settings.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.14

    Args:
        plugin_download_url (str):
        force (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
        plugin_download_url=plugin_download_url,
        force=force,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    plugin_download_url: str,
    force: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, StatusOK]]:
    """Install plugin from url

     Supply a URL to a plugin compressed in a .tar.gz file. Plugins must be enabled in the server's
    config settings.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.14

    Args:
        plugin_download_url (str):
        force (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        client=client,
        plugin_download_url=plugin_download_url,
        force=force,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    plugin_download_url: str,
    force: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, StatusOK]]:
    """Install plugin from url

     Supply a URL to a plugin compressed in a .tar.gz file. Plugins must be enabled in the server's
    config settings.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.14

    Args:
        plugin_download_url (str):
        force (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
        plugin_download_url=plugin_download_url,
        force=force,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    plugin_download_url: str,
    force: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, StatusOK]]:
    """Install plugin from url

     Supply a URL to a plugin compressed in a .tar.gz file. Plugins must be enabled in the server's
    config settings.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.14

    Args:
        plugin_download_url (str):
        force (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            client=client,
            plugin_download_url=plugin_download_url,
            force=force,
        )
    ).parsed
