from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.bot import Bot
from ...types import Response


def _get_kwargs(
    bot_user_id: str,
    user_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/bots/{bot_user_id}/assign/{user_id}".format(client.base_url, bot_user_id=bot_user_id, user_id=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
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
    user_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Bot]]:
    """Assign a bot to a user

     Assign a bot to a specified user.
    ##### Permissions
    Must have `manage_bots` permission.
    __Minimum server version__: 5.10

    Args:
        bot_user_id (str):
        user_id (str):

    Returns:
        Response[Union[Any, Bot]]
    """

    kwargs = _get_kwargs(
        bot_user_id=bot_user_id,
        user_id=user_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    bot_user_id: str,
    user_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Bot]]:
    """Assign a bot to a user

     Assign a bot to a specified user.
    ##### Permissions
    Must have `manage_bots` permission.
    __Minimum server version__: 5.10

    Args:
        bot_user_id (str):
        user_id (str):

    Returns:
        Response[Union[Any, Bot]]
    """

    return sync_detailed(
        bot_user_id=bot_user_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    bot_user_id: str,
    user_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Bot]]:
    """Assign a bot to a user

     Assign a bot to a specified user.
    ##### Permissions
    Must have `manage_bots` permission.
    __Minimum server version__: 5.10

    Args:
        bot_user_id (str):
        user_id (str):

    Returns:
        Response[Union[Any, Bot]]
    """

    kwargs = _get_kwargs(
        bot_user_id=bot_user_id,
        user_id=user_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    bot_user_id: str,
    user_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Bot]]:
    """Assign a bot to a user

     Assign a bot to a specified user.
    ##### Permissions
    Must have `manage_bots` permission.
    __Minimum server version__: 5.10

    Args:
        bot_user_id (str):
        user_id (str):

    Returns:
        Response[Union[Any, Bot]]
    """

    return (
        await asyncio_detailed(
            bot_user_id=bot_user_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
