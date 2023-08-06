from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_team_invite_info_response_200 import GetTeamInviteInfoResponse200
from ...types import Response


def _get_kwargs(
    invite_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/teams/invite/{invite_id}".format(client.base_url, invite_id=invite_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GetTeamInviteInfoResponse200]]:
    if response.status_code == 200:
        response_200 = GetTeamInviteInfoResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, GetTeamInviteInfoResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    invite_id: str,
    *,
    client: Client,
) -> Response[Union[Any, GetTeamInviteInfoResponse200]]:
    """Get invite info for a team

     Get the `name`, `display_name`, `description` and `id` for a team from the invite id.

    __Minimum server version__: 4.0

    ##### Permissions
    No authentication required.

    Args:
        invite_id (str):

    Returns:
        Response[Union[Any, GetTeamInviteInfoResponse200]]
    """

    kwargs = _get_kwargs(
        invite_id=invite_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    invite_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, GetTeamInviteInfoResponse200]]:
    """Get invite info for a team

     Get the `name`, `display_name`, `description` and `id` for a team from the invite id.

    __Minimum server version__: 4.0

    ##### Permissions
    No authentication required.

    Args:
        invite_id (str):

    Returns:
        Response[Union[Any, GetTeamInviteInfoResponse200]]
    """

    return sync_detailed(
        invite_id=invite_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    invite_id: str,
    *,
    client: Client,
) -> Response[Union[Any, GetTeamInviteInfoResponse200]]:
    """Get invite info for a team

     Get the `name`, `display_name`, `description` and `id` for a team from the invite id.

    __Minimum server version__: 4.0

    ##### Permissions
    No authentication required.

    Args:
        invite_id (str):

    Returns:
        Response[Union[Any, GetTeamInviteInfoResponse200]]
    """

    kwargs = _get_kwargs(
        invite_id=invite_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    invite_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, GetTeamInviteInfoResponse200]]:
    """Get invite info for a team

     Get the `name`, `display_name`, `description` and `id` for a team from the invite id.

    __Minimum server version__: 4.0

    ##### Permissions
    No authentication required.

    Args:
        invite_id (str):

    Returns:
        Response[Union[Any, GetTeamInviteInfoResponse200]]
    """

    return (
        await asyncio_detailed(
            invite_id=invite_id,
            client=client,
        )
    ).parsed
