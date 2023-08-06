from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: str,
    *,
    client: Client,
    include_timezones: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/channels/{channel_id}/member_counts_by_group".format(client.base_url, channel_id=channel_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["include_timezones"] = include_timezones

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    channel_id: str,
    *,
    client: Client,
    include_timezones: Union[Unset, None, bool] = False,
) -> Response[Any]:
    """Channel members counts for each group that has atleast one member in the channel

     Returns a set of ChannelMemberCountByGroup objects which contain a `group_id`,
    `channel_member_count` and a `channel_member_timezones_count`.
    ##### Permissions
    Must have `read_channel` permission for the given channel.
    __Minimum server version__: 5.24

    Args:
        channel_id (str):
        include_timezones (Union[Unset, None, bool]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
        include_timezones=include_timezones,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    channel_id: str,
    *,
    client: Client,
    include_timezones: Union[Unset, None, bool] = False,
) -> Response[Any]:
    """Channel members counts for each group that has atleast one member in the channel

     Returns a set of ChannelMemberCountByGroup objects which contain a `group_id`,
    `channel_member_count` and a `channel_member_timezones_count`.
    ##### Permissions
    Must have `read_channel` permission for the given channel.
    __Minimum server version__: 5.24

    Args:
        channel_id (str):
        include_timezones (Union[Unset, None, bool]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
        include_timezones=include_timezones,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
