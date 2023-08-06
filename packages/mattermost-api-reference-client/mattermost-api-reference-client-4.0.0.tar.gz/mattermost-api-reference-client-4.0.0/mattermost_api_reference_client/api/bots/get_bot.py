from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.bot import Bot
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bot_user_id: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/bots/{bot_user_id}".format(client.base_url, bot_user_id=bot_user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["include_deleted"] = include_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Bot]]:
    if response.status_code == 200:
        response_200 = Bot.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Bot]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    bot_user_id: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, Bot]]:
    """Get a bot

     Get a bot specified by its bot id.
    ##### Permissions
    Must have `read_bots` permission for bots you are managing, and `read_others_bots` permission for
    bots others are managing.
    __Minimum server version__: 5.10

    Args:
        bot_user_id (str):
        include_deleted (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Bot]]
    """

    kwargs = _get_kwargs(
        bot_user_id=bot_user_id,
        client=client,
        include_deleted=include_deleted,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    bot_user_id: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, Bot]]:
    """Get a bot

     Get a bot specified by its bot id.
    ##### Permissions
    Must have `read_bots` permission for bots you are managing, and `read_others_bots` permission for
    bots others are managing.
    __Minimum server version__: 5.10

    Args:
        bot_user_id (str):
        include_deleted (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Bot]]
    """

    return sync_detailed(
        bot_user_id=bot_user_id,
        client=client,
        include_deleted=include_deleted,
    ).parsed


async def asyncio_detailed(
    bot_user_id: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, Bot]]:
    """Get a bot

     Get a bot specified by its bot id.
    ##### Permissions
    Must have `read_bots` permission for bots you are managing, and `read_others_bots` permission for
    bots others are managing.
    __Minimum server version__: 5.10

    Args:
        bot_user_id (str):
        include_deleted (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Bot]]
    """

    kwargs = _get_kwargs(
        bot_user_id=bot_user_id,
        client=client,
        include_deleted=include_deleted,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    bot_user_id: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, Bot]]:
    """Get a bot

     Get a bot specified by its bot id.
    ##### Permissions
    Must have `read_bots` permission for bots you are managing, and `read_others_bots` permission for
    bots others are managing.
    __Minimum server version__: 5.10

    Args:
        bot_user_id (str):
        include_deleted (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Bot]]
    """

    return (
        await asyncio_detailed(
            bot_user_id=bot_user_id,
            client=client,
            include_deleted=include_deleted,
        )
    ).parsed
