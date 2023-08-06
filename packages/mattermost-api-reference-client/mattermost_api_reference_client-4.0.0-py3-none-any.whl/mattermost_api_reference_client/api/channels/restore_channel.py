from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.channel import Channel
from ...types import Response


def _get_kwargs(
    channel_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/channels/{channel_id}/restore".format(client.base_url, channel_id=channel_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Channel]]:
    if response.status_code == 200:
        response_200 = Channel.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, Channel]]:
    """Restore a channel

     Restore channel from the provided channel id string.

    __Minimum server version__: 3.10

    ##### Permissions
    `manage_team` permission for the team of the channel.

    Args:
        channel_id (str):

    Returns:
        Response[Union[Any, Channel]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
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
) -> Optional[Union[Any, Channel]]:
    """Restore a channel

     Restore channel from the provided channel id string.

    __Minimum server version__: 3.10

    ##### Permissions
    `manage_team` permission for the team of the channel.

    Args:
        channel_id (str):

    Returns:
        Response[Union[Any, Channel]]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Channel]]:
    """Restore a channel

     Restore channel from the provided channel id string.

    __Minimum server version__: 3.10

    ##### Permissions
    `manage_team` permission for the team of the channel.

    Args:
        channel_id (str):

    Returns:
        Response[Union[Any, Channel]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    channel_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Channel]]:
    """Restore a channel

     Restore channel from the provided channel id string.

    __Minimum server version__: 3.10

    ##### Permissions
    `manage_team` permission for the team of the channel.

    Args:
        channel_id (str):

    Returns:
        Response[Union[Any, Channel]]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
        )
    ).parsed
