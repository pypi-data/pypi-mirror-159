from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.channel import Channel
from ...models.update_channel_privacy_json_body import UpdateChannelPrivacyJsonBody
from ...types import Response


def _get_kwargs(
    channel_id: str,
    *,
    client: Client,
    json_body: UpdateChannelPrivacyJsonBody,
) -> Dict[str, Any]:
    url = "{}/channels/{channel_id}/privacy".format(client.base_url, channel_id=channel_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Channel]]:
    if response.status_code == 200:
        response_200 = Channel.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Channel]]:
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
    json_body: UpdateChannelPrivacyJsonBody,
) -> Response[Union[Any, Channel]]:
    """Update channel's privacy

     Updates channel's privacy allowing changing a channel from Public to Private and back.

    __Minimum server version__: 5.16

    ##### Permissions
    `manage_team` permission for the channels team on version < 5.28.
    `convert_public_channel_to_private` permission for the channel if updating privacy to 'P' on version
    >= 5.28. `convert_private_channel_to_public` permission for the channel if updating privacy to 'O'
    on version >= 5.28.

    Args:
        channel_id (str):
        json_body (UpdateChannelPrivacyJsonBody):

    Returns:
        Response[Union[Any, Channel]]
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
    json_body: UpdateChannelPrivacyJsonBody,
) -> Optional[Union[Any, Channel]]:
    """Update channel's privacy

     Updates channel's privacy allowing changing a channel from Public to Private and back.

    __Minimum server version__: 5.16

    ##### Permissions
    `manage_team` permission for the channels team on version < 5.28.
    `convert_public_channel_to_private` permission for the channel if updating privacy to 'P' on version
    >= 5.28. `convert_private_channel_to_public` permission for the channel if updating privacy to 'O'
    on version >= 5.28.

    Args:
        channel_id (str):
        json_body (UpdateChannelPrivacyJsonBody):

    Returns:
        Response[Union[Any, Channel]]
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
    json_body: UpdateChannelPrivacyJsonBody,
) -> Response[Union[Any, Channel]]:
    """Update channel's privacy

     Updates channel's privacy allowing changing a channel from Public to Private and back.

    __Minimum server version__: 5.16

    ##### Permissions
    `manage_team` permission for the channels team on version < 5.28.
    `convert_public_channel_to_private` permission for the channel if updating privacy to 'P' on version
    >= 5.28. `convert_private_channel_to_public` permission for the channel if updating privacy to 'O'
    on version >= 5.28.

    Args:
        channel_id (str):
        json_body (UpdateChannelPrivacyJsonBody):

    Returns:
        Response[Union[Any, Channel]]
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
    json_body: UpdateChannelPrivacyJsonBody,
) -> Optional[Union[Any, Channel]]:
    """Update channel's privacy

     Updates channel's privacy allowing changing a channel from Public to Private and back.

    __Minimum server version__: 5.16

    ##### Permissions
    `manage_team` permission for the channels team on version < 5.28.
    `convert_public_channel_to_private` permission for the channel if updating privacy to 'P' on version
    >= 5.28. `convert_private_channel_to_public` permission for the channel if updating privacy to 'O'
    on version >= 5.28.

    Args:
        channel_id (str):
        json_body (UpdateChannelPrivacyJsonBody):

    Returns:
        Response[Union[Any, Channel]]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
