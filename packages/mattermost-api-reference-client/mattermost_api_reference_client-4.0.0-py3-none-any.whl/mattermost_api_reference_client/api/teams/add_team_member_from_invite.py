from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.team_member import TeamMember
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    token: str,
) -> Dict[str, Any]:
    url = "{}/teams/members/invite".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["token"] = token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
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
    *,
    client: Client,
    token: str,
) -> Response[Union[Any, TeamMember]]:
    """Add user to team from invite

     Using either an invite id or hash/data pair from an email invite link, add a user to a team.
    ##### Permissions
    Must be authenticated.

    Args:
        token (str):

    Returns:
        Response[Union[Any, TeamMember]]
    """

    kwargs = _get_kwargs(
        client=client,
        token=token,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    token: str,
) -> Optional[Union[Any, TeamMember]]:
    """Add user to team from invite

     Using either an invite id or hash/data pair from an email invite link, add a user to a team.
    ##### Permissions
    Must be authenticated.

    Args:
        token (str):

    Returns:
        Response[Union[Any, TeamMember]]
    """

    return sync_detailed(
        client=client,
        token=token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    token: str,
) -> Response[Union[Any, TeamMember]]:
    """Add user to team from invite

     Using either an invite id or hash/data pair from an email invite link, add a user to a team.
    ##### Permissions
    Must be authenticated.

    Args:
        token (str):

    Returns:
        Response[Union[Any, TeamMember]]
    """

    kwargs = _get_kwargs(
        client=client,
        token=token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    token: str,
) -> Optional[Union[Any, TeamMember]]:
    """Add user to team from invite

     Using either an invite id or hash/data pair from an email invite link, add a user to a team.
    ##### Permissions
    Must be authenticated.

    Args:
        token (str):

    Returns:
        Response[Union[Any, TeamMember]]
    """

    return (
        await asyncio_detailed(
            client=client,
            token=token,
        )
    ).parsed
