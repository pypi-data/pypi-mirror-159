from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.add_channel_member_json_body import AddChannelMemberJsonBody
from ...models.channel_member import ChannelMember
from ...types import Response


def _get_kwargs(
    channel_id: str,
    *,
    client: Client,
    json_body: AddChannelMemberJsonBody,
) -> Dict[str, Any]:
    url = "{}/channels/{channel_id}/members".format(client.base_url, channel_id=channel_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ChannelMember]]:
    if response.status_code == 201:
        response_201 = ChannelMember.from_dict(response.json())

        return response_201
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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ChannelMember]]:
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
    json_body: AddChannelMemberJsonBody,
) -> Response[Union[Any, ChannelMember]]:
    """Add user to channel

     Add a user to a channel by creating a channel member object.

    Args:
        channel_id (str):
        json_body (AddChannelMemberJsonBody):

    Returns:
        Response[Union[Any, ChannelMember]]
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
    json_body: AddChannelMemberJsonBody,
) -> Optional[Union[Any, ChannelMember]]:
    """Add user to channel

     Add a user to a channel by creating a channel member object.

    Args:
        channel_id (str):
        json_body (AddChannelMemberJsonBody):

    Returns:
        Response[Union[Any, ChannelMember]]
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
    json_body: AddChannelMemberJsonBody,
) -> Response[Union[Any, ChannelMember]]:
    """Add user to channel

     Add a user to a channel by creating a channel member object.

    Args:
        channel_id (str):
        json_body (AddChannelMemberJsonBody):

    Returns:
        Response[Union[Any, ChannelMember]]
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
    json_body: AddChannelMemberJsonBody,
) -> Optional[Union[Any, ChannelMember]]:
    """Add user to channel

     Add a user to a channel by creating a channel member object.

    Args:
        channel_id (str):
        json_body (AddChannelMemberJsonBody):

    Returns:
        Response[Union[Any, ChannelMember]]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
