from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.channel_moderation import ChannelModeration
from ...models.channel_moderation_patch import ChannelModerationPatch
from ...types import Response


def _get_kwargs(
    channel_id: str,
    *,
    client: Client,
    json_body: ChannelModerationPatch,
) -> Dict[str, Any]:
    url = "{}/channels/{channel_id}/moderations/patch".format(client.base_url, channel_id=channel_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[ChannelModeration]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ChannelModeration.from_dict(response_200_item_data)

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[ChannelModeration]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    channel_id: str,
    *,
    client: Client,
    json_body: ChannelModerationPatch,
) -> Response[Union[Any, List[ChannelModeration]]]:
    """Update a channel's moderation settings.

     ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.22

    Args:
        channel_id (str):
        json_body (ChannelModerationPatch):

    Returns:
        Response[Union[Any, List[ChannelModeration]]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    channel_id: str,
    *,
    client: Client,
    json_body: ChannelModerationPatch,
) -> Optional[Union[Any, List[ChannelModeration]]]:
    """Update a channel's moderation settings.

     ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.22

    Args:
        channel_id (str):
        json_body (ChannelModerationPatch):

    Returns:
        Response[Union[Any, List[ChannelModeration]]]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: Client,
    json_body: ChannelModerationPatch,
) -> Response[Union[Any, List[ChannelModeration]]]:
    """Update a channel's moderation settings.

     ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.22

    Args:
        channel_id (str):
        json_body (ChannelModerationPatch):

    Returns:
        Response[Union[Any, List[ChannelModeration]]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    channel_id: str,
    *,
    client: Client,
    json_body: ChannelModerationPatch,
) -> Optional[Union[Any, List[ChannelModeration]]]:
    """Update a channel's moderation settings.

     ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.22

    Args:
        channel_id (str):
        json_body (ChannelModerationPatch):

    Returns:
        Response[Union[Any, List[ChannelModeration]]]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
