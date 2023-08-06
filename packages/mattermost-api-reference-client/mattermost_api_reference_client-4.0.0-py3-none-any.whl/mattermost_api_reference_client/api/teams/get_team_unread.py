from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.team_unread import TeamUnread
from ...types import Response


def _get_kwargs(
    user_id: str,
    team_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/teams/{team_id}/unread".format(client.base_url, user_id=user_id, team_id=team_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, TeamUnread]]:
    if response.status_code == 200:
        response_200 = TeamUnread.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, TeamUnread]]:
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
) -> Response[Union[Any, TeamUnread]]:
    """Get unreads for a team

     Get the unread mention and message counts for a team for the specified user.
    ##### Permissions
    Must be the user or have `edit_other_users` permission and have `view_team` permission for the team.

    Args:
        user_id (str):
        team_id (str):

    Returns:
        Response[Union[Any, TeamUnread]]
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
) -> Optional[Union[Any, TeamUnread]]:
    """Get unreads for a team

     Get the unread mention and message counts for a team for the specified user.
    ##### Permissions
    Must be the user or have `edit_other_users` permission and have `view_team` permission for the team.

    Args:
        user_id (str):
        team_id (str):

    Returns:
        Response[Union[Any, TeamUnread]]
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
) -> Response[Union[Any, TeamUnread]]:
    """Get unreads for a team

     Get the unread mention and message counts for a team for the specified user.
    ##### Permissions
    Must be the user or have `edit_other_users` permission and have `view_team` permission for the team.

    Args:
        user_id (str):
        team_id (str):

    Returns:
        Response[Union[Any, TeamUnread]]
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
) -> Optional[Union[Any, TeamUnread]]:
    """Get unreads for a team

     Get the unread mention and message counts for a team for the specified user.
    ##### Permissions
    Must be the user or have `edit_other_users` permission and have `view_team` permission for the team.

    Args:
        user_id (str):
        team_id (str):

    Returns:
        Response[Union[Any, TeamUnread]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            team_id=team_id,
            client=client,
        )
    ).parsed
