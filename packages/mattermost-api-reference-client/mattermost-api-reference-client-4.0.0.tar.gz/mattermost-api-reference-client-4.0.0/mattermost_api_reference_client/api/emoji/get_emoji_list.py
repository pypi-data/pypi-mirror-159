from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.emoji import Emoji
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    sort: Union[Unset, None, str] = "",
) -> Dict[str, Any]:
    url = "{}/emoji".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["per_page"] = per_page

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Emoji]]:
    if response.status_code == 200:
        response_200 = Emoji.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Emoji]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    sort: Union[Unset, None, str] = "",
) -> Response[Union[Any, Emoji]]:
    """Get a list of custom emoji

     Get a page of metadata for custom emoji on the system. Since server version 4.7, sort using the
    `sort` query parameter.
    ##### Permissions
    Must be authenticated.

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        sort (Union[Unset, None, str]):  Default: ''.

    Returns:
        Response[Union[Any, Emoji]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
        sort=sort,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    sort: Union[Unset, None, str] = "",
) -> Optional[Union[Any, Emoji]]:
    """Get a list of custom emoji

     Get a page of metadata for custom emoji on the system. Since server version 4.7, sort using the
    `sort` query parameter.
    ##### Permissions
    Must be authenticated.

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        sort (Union[Unset, None, str]):  Default: ''.

    Returns:
        Response[Union[Any, Emoji]]
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    sort: Union[Unset, None, str] = "",
) -> Response[Union[Any, Emoji]]:
    """Get a list of custom emoji

     Get a page of metadata for custom emoji on the system. Since server version 4.7, sort using the
    `sort` query parameter.
    ##### Permissions
    Must be authenticated.

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        sort (Union[Unset, None, str]):  Default: ''.

    Returns:
        Response[Union[Any, Emoji]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
        sort=sort,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    sort: Union[Unset, None, str] = "",
) -> Optional[Union[Any, Emoji]]:
    """Get a list of custom emoji

     Get a page of metadata for custom emoji on the system. Since server version 4.7, sort using the
    `sort` query parameter.
    ##### Permissions
    Must be authenticated.

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        sort (Union[Unset, None, str]):  Default: ''.

    Returns:
        Response[Union[Any, Emoji]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            sort=sort,
        )
    ).parsed
