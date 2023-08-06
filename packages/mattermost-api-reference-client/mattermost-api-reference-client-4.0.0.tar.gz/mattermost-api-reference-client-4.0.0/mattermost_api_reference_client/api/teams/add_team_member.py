from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.add_team_member_json_body import AddTeamMemberJsonBody
from ...models.team_member import TeamMember
from ...types import Response


def _get_kwargs(
    team_id: str,
    *,
    client: Client,
    json_body: AddTeamMemberJsonBody,
) -> Dict[str, Any]:
    url = "{}/teams/{team_id}/members".format(client.base_url, team_id=team_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, TeamMember]]:
    if response.status_code == 201:
        response_201 = TeamMember.from_dict(response.json())

        return response_201
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
    *,
    client: Client,
    json_body: AddTeamMemberJsonBody,
) -> Response[Union[Any, TeamMember]]:
    """Add user to team

     Add user to the team by user_id.
    ##### Permissions
    Must be authenticated and team be open to add self. For adding another user, authenticated user must
    have the `add_user_to_team` permission.

    Args:
        team_id (str):
        json_body (AddTeamMemberJsonBody):

    Returns:
        Response[Union[Any, TeamMember]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        json_body=json_body,
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
    json_body: AddTeamMemberJsonBody,
) -> Optional[Union[Any, TeamMember]]:
    """Add user to team

     Add user to the team by user_id.
    ##### Permissions
    Must be authenticated and team be open to add self. For adding another user, authenticated user must
    have the `add_user_to_team` permission.

    Args:
        team_id (str):
        json_body (AddTeamMemberJsonBody):

    Returns:
        Response[Union[Any, TeamMember]]
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    *,
    client: Client,
    json_body: AddTeamMemberJsonBody,
) -> Response[Union[Any, TeamMember]]:
    """Add user to team

     Add user to the team by user_id.
    ##### Permissions
    Must be authenticated and team be open to add self. For adding another user, authenticated user must
    have the `add_user_to_team` permission.

    Args:
        team_id (str):
        json_body (AddTeamMemberJsonBody):

    Returns:
        Response[Union[Any, TeamMember]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    team_id: str,
    *,
    client: Client,
    json_body: AddTeamMemberJsonBody,
) -> Optional[Union[Any, TeamMember]]:
    """Add user to team

     Add user to the team by user_id.
    ##### Permissions
    Must be authenticated and team be open to add self. For adding another user, authenticated user must
    have the `add_user_to_team` permission.

    Args:
        team_id (str):
        json_body (AddTeamMemberJsonBody):

    Returns:
        Response[Union[Any, TeamMember]]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
