from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.channel_member import ChannelMember
from ...types import Response


def _get_kwargs(
    user_id: str,
    team_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/teams/{team_id}/channels/members".format(
        client.base_url, user_id=user_id, team_id=team_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
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
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[ChannelMember]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: str,
    team_id: str,
    *,
    client: Client,
) -> Response[Union[Any, List[ChannelMember]]]:
    """Get channel memberships and roles for a user

     Get all channel memberships and associated membership roles (i.e. `channel_user`, `channel_admin`)
    for a user on a specific team.
    ##### Permissions
    Logged in as the user and `view_team` permission for the team. Having `manage_system` permission
    voids the previous requirements.

    Args:
        user_id (str):
        team_id (str):

    Returns:
        Response[Union[Any, List[ChannelMember]]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        team_id=team_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: str,
    team_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, List[ChannelMember]]]:
    """Get channel memberships and roles for a user

     Get all channel memberships and associated membership roles (i.e. `channel_user`, `channel_admin`)
    for a user on a specific team.
    ##### Permissions
    Logged in as the user and `view_team` permission for the team. Having `manage_system` permission
    voids the previous requirements.

    Args:
        user_id (str):
        team_id (str):

    Returns:
        Response[Union[Any, List[ChannelMember]]]
    """

    return sync_detailed(
        user_id=user_id,
        team_id=team_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    team_id: str,
    *,
    client: Client,
) -> Response[Union[Any, List[ChannelMember]]]:
    """Get channel memberships and roles for a user

     Get all channel memberships and associated membership roles (i.e. `channel_user`, `channel_admin`)
    for a user on a specific team.
    ##### Permissions
    Logged in as the user and `view_team` permission for the team. Having `manage_system` permission
    voids the previous requirements.

    Args:
        user_id (str):
        team_id (str):

    Returns:
        Response[Union[Any, List[ChannelMember]]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        team_id=team_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    team_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, List[ChannelMember]]]:
    """Get channel memberships and roles for a user

     Get all channel memberships and associated membership roles (i.e. `channel_user`, `channel_admin`)
    for a user on a specific team.
    ##### Permissions
    Logged in as the user and `view_team` permission for the team. Having `manage_system` permission
    voids the previous requirements.

    Args:
        user_id (str):
        team_id (str):

    Returns:
        Response[Union[Any, List[ChannelMember]]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            team_id=team_id,
            client=client,
        )
    ).parsed
