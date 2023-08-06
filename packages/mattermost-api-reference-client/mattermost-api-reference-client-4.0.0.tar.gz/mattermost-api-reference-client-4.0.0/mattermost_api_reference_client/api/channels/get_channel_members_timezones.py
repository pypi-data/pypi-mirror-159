from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    channel_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/channels/{channel_id}/timezones".format(client.base_url, channel_id=channel_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[str]]]:
    if response.status_code == 200:
        response_200 = cast(List[str], response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[str]]]:
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
) -> Response[Union[Any, List[str]]]:
    """Get timezones in a channel

     Get a list of timezones for the users who are in this channel.

    __Minimum server version__: 5.6

    ##### Permissions
    Must have the `read_channel` permission.

    Args:
        channel_id (str):

    Returns:
        Response[Union[Any, List[str]]]
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
) -> Optional[Union[Any, List[str]]]:
    """Get timezones in a channel

     Get a list of timezones for the users who are in this channel.

    __Minimum server version__: 5.6

    ##### Permissions
    Must have the `read_channel` permission.

    Args:
        channel_id (str):

    Returns:
        Response[Union[Any, List[str]]]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: Client,
) -> Response[Union[Any, List[str]]]:
    """Get timezones in a channel

     Get a list of timezones for the users who are in this channel.

    __Minimum server version__: 5.6

    ##### Permissions
    Must have the `read_channel` permission.

    Args:
        channel_id (str):

    Returns:
        Response[Union[Any, List[str]]]
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
) -> Optional[Union[Any, List[str]]]:
    """Get timezones in a channel

     Get a list of timezones for the users who are in this channel.

    __Minimum server version__: 5.6

    ##### Permissions
    Must have the `read_channel` permission.

    Args:
        channel_id (str):

    Returns:
        Response[Union[Any, List[str]]]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
        )
    ).parsed
