from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.channel_member import ChannelMember
from ...types import Response


def _get_kwargs(
    channel_id: str,
    *,
    client: Client,
    json_body: List[str],
) -> Dict[str, Any]:
    url = "{}/channels/{channel_id}/members/ids".format(client.base_url, channel_id=channel_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[ChannelMember]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ChannelMember.from_dict(response_200_item_data)

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
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[ChannelMember]]]:
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
    json_body: List[str],
) -> Response[Union[Any, List[ChannelMember]]]:
    """Get channel members by ids

     Get a list of channel members based on the provided user ids.
    ##### Permissions
    Must have the `read_channel` permission.

    Args:
        channel_id (str):
        json_body (List[str]):

    Returns:
        Response[Union[Any, List[ChannelMember]]]
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
    json_body: List[str],
) -> Optional[Union[Any, List[ChannelMember]]]:
    """Get channel members by ids

     Get a list of channel members based on the provided user ids.
    ##### Permissions
    Must have the `read_channel` permission.

    Args:
        channel_id (str):
        json_body (List[str]):

    Returns:
        Response[Union[Any, List[ChannelMember]]]
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
    json_body: List[str],
) -> Response[Union[Any, List[ChannelMember]]]:
    """Get channel members by ids

     Get a list of channel members based on the provided user ids.
    ##### Permissions
    Must have the `read_channel` permission.

    Args:
        channel_id (str):
        json_body (List[str]):

    Returns:
        Response[Union[Any, List[ChannelMember]]]
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
    json_body: List[str],
) -> Optional[Union[Any, List[ChannelMember]]]:
    """Get channel members by ids

     Get a list of channel members based on the provided user ids.
    ##### Permissions
    Must have the `read_channel` permission.

    Args:
        channel_id (str):
        json_body (List[str]):

    Returns:
        Response[Union[Any, List[ChannelMember]]]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
