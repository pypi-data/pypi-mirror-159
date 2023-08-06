from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.marketplace_plugin import MarketplacePlugin
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    server_version: Union[Unset, None, str] = UNSET,
    local_only: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/plugins/marketplace".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["per_page"] = per_page

    params["filter"] = filter_

    params["server_version"] = server_version

    params["local_only"] = local_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[MarketplacePlugin]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MarketplacePlugin.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[MarketplacePlugin]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    server_version: Union[Unset, None, str] = UNSET,
    local_only: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, List[MarketplacePlugin]]]:
    """Gets all the marketplace plugins

     Gets all plugins from the marketplace server, merging data from locally installed plugins as well as
    prepackaged plugins shipped with the server.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.16

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):
        filter_ (Union[Unset, None, str]):
        server_version (Union[Unset, None, str]):
        local_only (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[MarketplacePlugin]]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
        filter_=filter_,
        server_version=server_version,
        local_only=local_only,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    server_version: Union[Unset, None, str] = UNSET,
    local_only: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, List[MarketplacePlugin]]]:
    """Gets all the marketplace plugins

     Gets all plugins from the marketplace server, merging data from locally installed plugins as well as
    prepackaged plugins shipped with the server.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.16

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):
        filter_ (Union[Unset, None, str]):
        server_version (Union[Unset, None, str]):
        local_only (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[MarketplacePlugin]]]
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        filter_=filter_,
        server_version=server_version,
        local_only=local_only,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    server_version: Union[Unset, None, str] = UNSET,
    local_only: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, List[MarketplacePlugin]]]:
    """Gets all the marketplace plugins

     Gets all plugins from the marketplace server, merging data from locally installed plugins as well as
    prepackaged plugins shipped with the server.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.16

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):
        filter_ (Union[Unset, None, str]):
        server_version (Union[Unset, None, str]):
        local_only (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[MarketplacePlugin]]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
        filter_=filter_,
        server_version=server_version,
        local_only=local_only,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, None, int] = UNSET,
    per_page: Union[Unset, None, int] = UNSET,
    filter_: Union[Unset, None, str] = UNSET,
    server_version: Union[Unset, None, str] = UNSET,
    local_only: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, List[MarketplacePlugin]]]:
    """Gets all the marketplace plugins

     Gets all plugins from the marketplace server, merging data from locally installed plugins as well as
    prepackaged plugins shipped with the server.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.16

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):
        filter_ (Union[Unset, None, str]):
        server_version (Union[Unset, None, str]):
        local_only (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[MarketplacePlugin]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            filter_=filter_,
            server_version=server_version,
            local_only=local_only,
        )
    ).parsed
