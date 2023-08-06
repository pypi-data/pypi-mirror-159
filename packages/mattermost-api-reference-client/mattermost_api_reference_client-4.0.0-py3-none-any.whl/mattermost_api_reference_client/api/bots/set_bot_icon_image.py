from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.set_bot_icon_image_multipart_data import SetBotIconImageMultipartData
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    bot_user_id: str,
    *,
    client: Client,
    multipart_data: SetBotIconImageMultipartData,
) -> Dict[str, Any]:
    url = "{}/bots/{bot_user_id}/icon".format(client.base_url, bot_user_id=bot_user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
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
    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
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
    bot_user_id: str,
    *,
    client: Client,
    multipart_data: SetBotIconImageMultipartData,
) -> Response[Union[Any, StatusOK]]:
    """Set bot's LHS icon image

     Set a bot's LHS icon image based on bot_user_id string parameter. Icon image must be SVG format, all
    other formats are rejected.
    ##### Permissions
    Must have `manage_bots` permission.
    __Minimum server version__: 5.14

    Args:
        bot_user_id (str):
        multipart_data (SetBotIconImageMultipartData):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        bot_user_id=bot_user_id,
        client=client,
        multipart_data=multipart_data,
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
    multipart_data: SetBotIconImageMultipartData,
) -> Optional[Union[Any, StatusOK]]:
    """Set bot's LHS icon image

     Set a bot's LHS icon image based on bot_user_id string parameter. Icon image must be SVG format, all
    other formats are rejected.
    ##### Permissions
    Must have `manage_bots` permission.
    __Minimum server version__: 5.14

    Args:
        bot_user_id (str):
        multipart_data (SetBotIconImageMultipartData):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        bot_user_id=bot_user_id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    bot_user_id: str,
    *,
    client: Client,
    multipart_data: SetBotIconImageMultipartData,
) -> Response[Union[Any, StatusOK]]:
    """Set bot's LHS icon image

     Set a bot's LHS icon image based on bot_user_id string parameter. Icon image must be SVG format, all
    other formats are rejected.
    ##### Permissions
    Must have `manage_bots` permission.
    __Minimum server version__: 5.14

    Args:
        bot_user_id (str):
        multipart_data (SetBotIconImageMultipartData):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        bot_user_id=bot_user_id,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    bot_user_id: str,
    *,
    client: Client,
    multipart_data: SetBotIconImageMultipartData,
) -> Optional[Union[Any, StatusOK]]:
    """Set bot's LHS icon image

     Set a bot's LHS icon image based on bot_user_id string parameter. Icon image must be SVG format, all
    other formats are rejected.
    ##### Permissions
    Must have `manage_bots` permission.
    __Minimum server version__: 5.14

    Args:
        bot_user_id (str):
        multipart_data (SetBotIconImageMultipartData):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            bot_user_id=bot_user_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
