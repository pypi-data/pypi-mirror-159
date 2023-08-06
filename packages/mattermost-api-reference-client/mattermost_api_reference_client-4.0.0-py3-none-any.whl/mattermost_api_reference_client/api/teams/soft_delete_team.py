from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.status_ok import StatusOK
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_id: str,
    *,
    client: Client,
    permanent: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/teams/{team_id}".format(client.base_url, team_id=team_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["permanent"] = permanent

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
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
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
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
    permanent: Union[Unset, None, bool] = False,
) -> Response[Union[Any, StatusOK]]:
    """Delete a team

     Soft deletes a team, by marking the team as deleted in the database. Soft deleted teams will not be
    accessible in the user interface.

    Optionally use the permanent query parameter to hard delete the team for compliance reasons. As of
    server version 5.0, to use this feature `ServiceSettings.EnableAPITeamDeletion` must be set to
    `true` in the server's configuration.
    ##### Permissions
    Must have the `manage_team` permission.

    Args:
        team_id (str):
        permanent (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        permanent=permanent,
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
    permanent: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, StatusOK]]:
    """Delete a team

     Soft deletes a team, by marking the team as deleted in the database. Soft deleted teams will not be
    accessible in the user interface.

    Optionally use the permanent query parameter to hard delete the team for compliance reasons. As of
    server version 5.0, to use this feature `ServiceSettings.EnableAPITeamDeletion` must be set to
    `true` in the server's configuration.
    ##### Permissions
    Must have the `manage_team` permission.

    Args:
        team_id (str):
        permanent (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        permanent=permanent,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    *,
    client: Client,
    permanent: Union[Unset, None, bool] = False,
) -> Response[Union[Any, StatusOK]]:
    """Delete a team

     Soft deletes a team, by marking the team as deleted in the database. Soft deleted teams will not be
    accessible in the user interface.

    Optionally use the permanent query parameter to hard delete the team for compliance reasons. As of
    server version 5.0, to use this feature `ServiceSettings.EnableAPITeamDeletion` must be set to
    `true` in the server's configuration.
    ##### Permissions
    Must have the `manage_team` permission.

    Args:
        team_id (str):
        permanent (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        permanent=permanent,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    team_id: str,
    *,
    client: Client,
    permanent: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, StatusOK]]:
    """Delete a team

     Soft deletes a team, by marking the team as deleted in the database. Soft deleted teams will not be
    accessible in the user interface.

    Optionally use the permanent query parameter to hard delete the team for compliance reasons. As of
    server version 5.0, to use this feature `ServiceSettings.EnableAPITeamDeletion` must be set to
    `true` in the server's configuration.
    ##### Permissions
    Must have the `manage_team` permission.

    Args:
        team_id (str):
        permanent (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            permanent=permanent,
        )
    ).parsed
