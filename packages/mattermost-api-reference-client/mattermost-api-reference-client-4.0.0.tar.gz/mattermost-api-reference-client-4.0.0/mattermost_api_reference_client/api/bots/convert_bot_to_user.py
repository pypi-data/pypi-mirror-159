from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.convert_bot_to_user_json_body import ConvertBotToUserJsonBody
from ...models.status_ok import StatusOK
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bot_user_id: str,
    *,
    client: Client,
    json_body: ConvertBotToUserJsonBody,
    set_system_admin: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/bots/{bot_user_id}/convert_to_user".format(client.base_url, bot_user_id=bot_user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["set_system_admin"] = set_system_admin

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, StatusOK]]:
    if response.status_code == 200:
        response_200 = StatusOK.from_dict(response.json())

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
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, StatusOK]]:
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
    json_body: ConvertBotToUserJsonBody,
    set_system_admin: Union[Unset, None, bool] = False,
) -> Response[Union[Any, StatusOK]]:
    """Convert a bot into a user

     Convert a bot into a user.

    __Minimum server version__: 5.26

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        bot_user_id (str):
        set_system_admin (Union[Unset, None, bool]):
        json_body (ConvertBotToUserJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        bot_user_id=bot_user_id,
        client=client,
        json_body=json_body,
        set_system_admin=set_system_admin,
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
    json_body: ConvertBotToUserJsonBody,
    set_system_admin: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, StatusOK]]:
    """Convert a bot into a user

     Convert a bot into a user.

    __Minimum server version__: 5.26

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        bot_user_id (str):
        set_system_admin (Union[Unset, None, bool]):
        json_body (ConvertBotToUserJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        bot_user_id=bot_user_id,
        client=client,
        json_body=json_body,
        set_system_admin=set_system_admin,
    ).parsed


async def asyncio_detailed(
    bot_user_id: str,
    *,
    client: Client,
    json_body: ConvertBotToUserJsonBody,
    set_system_admin: Union[Unset, None, bool] = False,
) -> Response[Union[Any, StatusOK]]:
    """Convert a bot into a user

     Convert a bot into a user.

    __Minimum server version__: 5.26

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        bot_user_id (str):
        set_system_admin (Union[Unset, None, bool]):
        json_body (ConvertBotToUserJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        bot_user_id=bot_user_id,
        client=client,
        json_body=json_body,
        set_system_admin=set_system_admin,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    bot_user_id: str,
    *,
    client: Client,
    json_body: ConvertBotToUserJsonBody,
    set_system_admin: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, StatusOK]]:
    """Convert a bot into a user

     Convert a bot into a user.

    __Minimum server version__: 5.26

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        bot_user_id (str):
        set_system_admin (Union[Unset, None, bool]):
        json_body (ConvertBotToUserJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            bot_user_id=bot_user_id,
            client=client,
            json_body=json_body,
            set_system_admin=set_system_admin,
        )
    ).parsed
