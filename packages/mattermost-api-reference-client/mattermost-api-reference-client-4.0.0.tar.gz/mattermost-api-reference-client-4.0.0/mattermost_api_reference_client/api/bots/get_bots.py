from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.bot import Bot
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    include_deleted: Union[Unset, None, bool] = UNSET,
    only_orphaned: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/bots".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["per_page"] = per_page

    params["include_deleted"] = include_deleted

    params["only_orphaned"] = only_orphaned

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[Bot]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Bot.from_dict(response_200_item_data)

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
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[Bot]]]:
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
    include_deleted: Union[Unset, None, bool] = UNSET,
    only_orphaned: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, List[Bot]]]:
    """Get bots

     Get a page of a list of bots.
    ##### Permissions
    Must have `read_bots` permission for bots you are managing, and `read_others_bots` permission for
    bots others are managing.
    __Minimum server version__: 5.10

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        include_deleted (Union[Unset, None, bool]):
        only_orphaned (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Bot]]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
        include_deleted=include_deleted,
        only_orphaned=only_orphaned,
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
    include_deleted: Union[Unset, None, bool] = UNSET,
    only_orphaned: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, List[Bot]]]:
    """Get bots

     Get a page of a list of bots.
    ##### Permissions
    Must have `read_bots` permission for bots you are managing, and `read_others_bots` permission for
    bots others are managing.
    __Minimum server version__: 5.10

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        include_deleted (Union[Unset, None, bool]):
        only_orphaned (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Bot]]]
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        include_deleted=include_deleted,
        only_orphaned=only_orphaned,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    include_deleted: Union[Unset, None, bool] = UNSET,
    only_orphaned: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, List[Bot]]]:
    """Get bots

     Get a page of a list of bots.
    ##### Permissions
    Must have `read_bots` permission for bots you are managing, and `read_others_bots` permission for
    bots others are managing.
    __Minimum server version__: 5.10

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        include_deleted (Union[Unset, None, bool]):
        only_orphaned (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Bot]]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
        include_deleted=include_deleted,
        only_orphaned=only_orphaned,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    include_deleted: Union[Unset, None, bool] = UNSET,
    only_orphaned: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, List[Bot]]]:
    """Get bots

     Get a page of a list of bots.
    ##### Permissions
    Must have `read_bots` permission for bots you are managing, and `read_others_bots` permission for
    bots others are managing.
    __Minimum server version__: 5.10

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        include_deleted (Union[Unset, None, bool]):
        only_orphaned (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Bot]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            include_deleted=include_deleted,
            only_orphaned=only_orphaned,
        )
    ).parsed
