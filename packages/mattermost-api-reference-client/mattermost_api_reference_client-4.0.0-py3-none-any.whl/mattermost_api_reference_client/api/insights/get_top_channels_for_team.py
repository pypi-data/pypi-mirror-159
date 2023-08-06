from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.top_channel_list import TopChannelList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_id: str,
    *,
    client: Client,
    time_range: str,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Dict[str, Any]:
    url = "{}/teams/{team_id}/top/channels".format(client.base_url, team_id=team_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["time_range"] = time_range

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, TopChannelList]]:
    if response.status_code == 200:
        response_200 = TopChannelList.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, TopChannelList]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    team_id: str,
    *,
    client: Client,
    time_range: str,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Response[Union[Any, TopChannelList]]:
    """Get a list of the top channels for a team.

     Get a list of the top public and private channels (the user is a member of) for a given team.
    ##### Permissions
    Must have `view_team` permission for the team.

    Args:
        team_id (str):
        time_range (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Returns:
        Response[Union[Any, TopChannelList]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        time_range=time_range,
        page=page,
        per_page=per_page,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    team_id: str,
    *,
    client: Client,
    time_range: str,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Optional[Union[Any, TopChannelList]]:
    """Get a list of the top channels for a team.

     Get a list of the top public and private channels (the user is a member of) for a given team.
    ##### Permissions
    Must have `view_team` permission for the team.

    Args:
        team_id (str):
        time_range (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Returns:
        Response[Union[Any, TopChannelList]]
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        time_range=time_range,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    *,
    client: Client,
    time_range: str,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Response[Union[Any, TopChannelList]]:
    """Get a list of the top channels for a team.

     Get a list of the top public and private channels (the user is a member of) for a given team.
    ##### Permissions
    Must have `view_team` permission for the team.

    Args:
        team_id (str):
        time_range (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Returns:
        Response[Union[Any, TopChannelList]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        time_range=time_range,
        page=page,
        per_page=per_page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    team_id: str,
    *,
    client: Client,
    time_range: str,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Optional[Union[Any, TopChannelList]]:
    """Get a list of the top channels for a team.

     Get a list of the top public and private channels (the user is a member of) for a given team.
    ##### Permissions
    Must have `view_team` permission for the team.

    Args:
        team_id (str):
        time_range (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Returns:
        Response[Union[Any, TopChannelList]]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            time_range=time_range,
            page=page,
            per_page=per_page,
        )
    ).parsed
