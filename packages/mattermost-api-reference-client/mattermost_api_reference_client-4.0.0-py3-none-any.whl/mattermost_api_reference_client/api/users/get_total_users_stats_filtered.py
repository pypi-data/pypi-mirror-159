from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.users_stats import UsersStats
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    in_team: Union[Unset, None, str] = UNSET,
    in_channel: Union[Unset, None, str] = UNSET,
    include_deleted: Union[Unset, None, bool] = UNSET,
    include_bots: Union[Unset, None, bool] = UNSET,
    roles: Union[Unset, None, str] = UNSET,
    channel_roles: Union[Unset, None, str] = UNSET,
    team_roles: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/users/stats/filtered".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["in_team"] = in_team

    params["in_channel"] = in_channel

    params["include_deleted"] = include_deleted

    params["include_bots"] = include_bots

    params["roles"] = roles

    params["channel_roles"] = channel_roles

    params["team_roles"] = team_roles

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, UsersStats]]:
    if response.status_code == 200:
        response_200 = UsersStats.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, UsersStats]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    in_team: Union[Unset, None, str] = UNSET,
    in_channel: Union[Unset, None, str] = UNSET,
    include_deleted: Union[Unset, None, bool] = UNSET,
    include_bots: Union[Unset, None, bool] = UNSET,
    roles: Union[Unset, None, str] = UNSET,
    channel_roles: Union[Unset, None, str] = UNSET,
    team_roles: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, UsersStats]]:
    """Get total count of users in the system matching the specified filters

     Get a count of users in the system matching the specified filters.

    __Minimum server version__: 5.26

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        in_team (Union[Unset, None, str]):
        in_channel (Union[Unset, None, str]):
        include_deleted (Union[Unset, None, bool]):
        include_bots (Union[Unset, None, bool]):
        roles (Union[Unset, None, str]):
        channel_roles (Union[Unset, None, str]):
        team_roles (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, UsersStats]]
    """

    kwargs = _get_kwargs(
        client=client,
        in_team=in_team,
        in_channel=in_channel,
        include_deleted=include_deleted,
        include_bots=include_bots,
        roles=roles,
        channel_roles=channel_roles,
        team_roles=team_roles,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    in_team: Union[Unset, None, str] = UNSET,
    in_channel: Union[Unset, None, str] = UNSET,
    include_deleted: Union[Unset, None, bool] = UNSET,
    include_bots: Union[Unset, None, bool] = UNSET,
    roles: Union[Unset, None, str] = UNSET,
    channel_roles: Union[Unset, None, str] = UNSET,
    team_roles: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, UsersStats]]:
    """Get total count of users in the system matching the specified filters

     Get a count of users in the system matching the specified filters.

    __Minimum server version__: 5.26

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        in_team (Union[Unset, None, str]):
        in_channel (Union[Unset, None, str]):
        include_deleted (Union[Unset, None, bool]):
        include_bots (Union[Unset, None, bool]):
        roles (Union[Unset, None, str]):
        channel_roles (Union[Unset, None, str]):
        team_roles (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, UsersStats]]
    """

    return sync_detailed(
        client=client,
        in_team=in_team,
        in_channel=in_channel,
        include_deleted=include_deleted,
        include_bots=include_bots,
        roles=roles,
        channel_roles=channel_roles,
        team_roles=team_roles,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    in_team: Union[Unset, None, str] = UNSET,
    in_channel: Union[Unset, None, str] = UNSET,
    include_deleted: Union[Unset, None, bool] = UNSET,
    include_bots: Union[Unset, None, bool] = UNSET,
    roles: Union[Unset, None, str] = UNSET,
    channel_roles: Union[Unset, None, str] = UNSET,
    team_roles: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, UsersStats]]:
    """Get total count of users in the system matching the specified filters

     Get a count of users in the system matching the specified filters.

    __Minimum server version__: 5.26

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        in_team (Union[Unset, None, str]):
        in_channel (Union[Unset, None, str]):
        include_deleted (Union[Unset, None, bool]):
        include_bots (Union[Unset, None, bool]):
        roles (Union[Unset, None, str]):
        channel_roles (Union[Unset, None, str]):
        team_roles (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, UsersStats]]
    """

    kwargs = _get_kwargs(
        client=client,
        in_team=in_team,
        in_channel=in_channel,
        include_deleted=include_deleted,
        include_bots=include_bots,
        roles=roles,
        channel_roles=channel_roles,
        team_roles=team_roles,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    in_team: Union[Unset, None, str] = UNSET,
    in_channel: Union[Unset, None, str] = UNSET,
    include_deleted: Union[Unset, None, bool] = UNSET,
    include_bots: Union[Unset, None, bool] = UNSET,
    roles: Union[Unset, None, str] = UNSET,
    channel_roles: Union[Unset, None, str] = UNSET,
    team_roles: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, UsersStats]]:
    """Get total count of users in the system matching the specified filters

     Get a count of users in the system matching the specified filters.

    __Minimum server version__: 5.26

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        in_team (Union[Unset, None, str]):
        in_channel (Union[Unset, None, str]):
        include_deleted (Union[Unset, None, bool]):
        include_bots (Union[Unset, None, bool]):
        roles (Union[Unset, None, str]):
        channel_roles (Union[Unset, None, str]):
        team_roles (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, UsersStats]]
    """

    return (
        await asyncio_detailed(
            client=client,
            in_team=in_team,
            in_channel=in_channel,
            include_deleted=include_deleted,
            include_bots=include_bots,
            roles=roles,
            channel_roles=channel_roles,
            team_roles=team_roles,
        )
    ).parsed
