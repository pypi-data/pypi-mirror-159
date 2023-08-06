from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.team_member import TeamMember
from ...types import Response


def _get_kwargs(
    team_id: str,
    user_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/teams/{team_id}/members/{user_id}".format(client.base_url, team_id=team_id, user_id=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, TeamMember]]:
    if response.status_code == 200:
        response_200 = TeamMember.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, TeamMember]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    team_id: str,
    user_id: str,
    *,
    client: Client,
) -> Response[Union[Any, TeamMember]]:
    """Get a team member

     Get a team member on the system.
    ##### Permissions
    Must be authenticated and have the `view_team` permission.

    Args:
        team_id (str):
        user_id (str):

    Returns:
        Response[Union[Any, TeamMember]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        user_id=user_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    team_id: str,
    user_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, TeamMember]]:
    """Get a team member

     Get a team member on the system.
    ##### Permissions
    Must be authenticated and have the `view_team` permission.

    Args:
        team_id (str):
        user_id (str):

    Returns:
        Response[Union[Any, TeamMember]]
    """

    return sync_detailed(
        team_id=team_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    user_id: str,
    *,
    client: Client,
) -> Response[Union[Any, TeamMember]]:
    """Get a team member

     Get a team member on the system.
    ##### Permissions
    Must be authenticated and have the `view_team` permission.

    Args:
        team_id (str):
        user_id (str):

    Returns:
        Response[Union[Any, TeamMember]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        user_id=user_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    team_id: str,
    user_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, TeamMember]]:
    """Get a team member

     Get a team member on the system.
    ##### Permissions
    Must be authenticated and have the `view_team` permission.

    Args:
        team_id (str):
        user_id (str):

    Returns:
        Response[Union[Any, TeamMember]]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
