from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.channel import Channel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_name: str,
    channel_name: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/teams/name/{team_name}/channels/name/{channel_name}".format(
        client.base_url, team_name=team_name, channel_name=channel_name
    )

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
    team_name: str,
    channel_name: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = False,
) -> Response[Union[Any, Channel]]:
    """Get a channel by name and team name

     Gets a channel from the provided team name and channel name strings.
    ##### Permissions
    `read_channel` permission for the channel.

    Args:
        team_name (str):
        channel_name (str):
        include_deleted (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Channel]]
    """

    kwargs = _get_kwargs(
        team_name=team_name,
        channel_name=channel_name,
        client=client,
        include_deleted=include_deleted,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    team_name: str,
    channel_name: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, Channel]]:
    """Get a channel by name and team name

     Gets a channel from the provided team name and channel name strings.
    ##### Permissions
    `read_channel` permission for the channel.

    Args:
        team_name (str):
        channel_name (str):
        include_deleted (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Channel]]
    """

    return sync_detailed(
        team_name=team_name,
        channel_name=channel_name,
        client=client,
        include_deleted=include_deleted,
    ).parsed


async def asyncio_detailed(
    team_name: str,
    channel_name: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = False,
) -> Response[Union[Any, Channel]]:
    """Get a channel by name and team name

     Gets a channel from the provided team name and channel name strings.
    ##### Permissions
    `read_channel` permission for the channel.

    Args:
        team_name (str):
        channel_name (str):
        include_deleted (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Channel]]
    """

    kwargs = _get_kwargs(
        team_name=team_name,
        channel_name=channel_name,
        client=client,
        include_deleted=include_deleted,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    team_name: str,
    channel_name: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, Channel]]:
    """Get a channel by name and team name

     Gets a channel from the provided team name and channel name strings.
    ##### Permissions
    `read_channel` permission for the channel.

    Args:
        team_name (str):
        channel_name (str):
        include_deleted (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Channel]]
    """

    return (
        await asyncio_detailed(
            team_name=team_name,
            channel_name=channel_name,
            client=client,
            include_deleted=include_deleted,
        )
    ).parsed
