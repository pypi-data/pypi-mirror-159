from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.invite_guests_to_team_json_body import InviteGuestsToTeamJsonBody
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    team_id: str,
    *,
    client: Client,
    json_body: InviteGuestsToTeamJsonBody,
) -> Dict[str, Any]:
    url = "{}/teams/{team_id}/invite-guests/email".format(client.base_url, team_id=team_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, StatusOK]]:
    if response.status_code == 200:
        response_200 = StatusOK.from_dict(response.json())

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
    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, StatusOK]]:
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
    json_body: InviteGuestsToTeamJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Invite guests to the team by email

     Invite guests to existing team channels usign the user's email.

    The number of emails that can be sent is rate limited to 20 per hour with a burst of 20 emails. If
    the rate limit exceeds, the error message contains details on when to retry and when the timer will
    be reset.

    __Minimum server version__: 5.16

    ##### Permissions
    Must have `invite_guest` permission for the team.

    Args:
        team_id (str):
        json_body (InviteGuestsToTeamJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
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
    json_body: InviteGuestsToTeamJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Invite guests to the team by email

     Invite guests to existing team channels usign the user's email.

    The number of emails that can be sent is rate limited to 20 per hour with a burst of 20 emails. If
    the rate limit exceeds, the error message contains details on when to retry and when the timer will
    be reset.

    __Minimum server version__: 5.16

    ##### Permissions
    Must have `invite_guest` permission for the team.

    Args:
        team_id (str):
        json_body (InviteGuestsToTeamJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
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
    json_body: InviteGuestsToTeamJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Invite guests to the team by email

     Invite guests to existing team channels usign the user's email.

    The number of emails that can be sent is rate limited to 20 per hour with a burst of 20 emails. If
    the rate limit exceeds, the error message contains details on when to retry and when the timer will
    be reset.

    __Minimum server version__: 5.16

    ##### Permissions
    Must have `invite_guest` permission for the team.

    Args:
        team_id (str):
        json_body (InviteGuestsToTeamJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
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
    json_body: InviteGuestsToTeamJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Invite guests to the team by email

     Invite guests to existing team channels usign the user's email.

    The number of emails that can be sent is rate limited to 20 per hour with a burst of 20 emails. If
    the rate limit exceeds, the error message contains details on when to retry and when the timer will
    be reset.

    __Minimum server version__: 5.16

    ##### Permissions
    Must have `invite_guest` permission for the team.

    Args:
        team_id (str):
        json_body (InviteGuestsToTeamJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
