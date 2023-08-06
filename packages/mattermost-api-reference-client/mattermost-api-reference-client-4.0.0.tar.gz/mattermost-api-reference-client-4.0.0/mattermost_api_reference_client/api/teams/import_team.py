from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.import_team_multipart_data import ImportTeamMultipartData
from ...models.import_team_response_200 import ImportTeamResponse200
from ...types import Response


def _get_kwargs(
    team_id: str,
    *,
    client: Client,
    multipart_data: ImportTeamMultipartData,
) -> Dict[str, Any]:
    url = "{}/teams/{team_id}/import".format(client.base_url, team_id=team_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ImportTeamResponse200]]:
    if response.status_code == 200:
        response_200 = ImportTeamResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ImportTeamResponse200]]:
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
    multipart_data: ImportTeamMultipartData,
) -> Response[Union[Any, ImportTeamResponse200]]:
    """Import a Team from other application

     Import a team into a existing team. Import users, channels, posts, hooks.
    ##### Permissions
    Must have `permission_import_team` permission.

    Args:
        team_id (str):
        multipart_data (ImportTeamMultipartData):

    Returns:
        Response[Union[Any, ImportTeamResponse200]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        multipart_data=multipart_data,
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
    multipart_data: ImportTeamMultipartData,
) -> Optional[Union[Any, ImportTeamResponse200]]:
    """Import a Team from other application

     Import a team into a existing team. Import users, channels, posts, hooks.
    ##### Permissions
    Must have `permission_import_team` permission.

    Args:
        team_id (str):
        multipart_data (ImportTeamMultipartData):

    Returns:
        Response[Union[Any, ImportTeamResponse200]]
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    *,
    client: Client,
    multipart_data: ImportTeamMultipartData,
) -> Response[Union[Any, ImportTeamResponse200]]:
    """Import a Team from other application

     Import a team into a existing team. Import users, channels, posts, hooks.
    ##### Permissions
    Must have `permission_import_team` permission.

    Args:
        team_id (str):
        multipart_data (ImportTeamMultipartData):

    Returns:
        Response[Union[Any, ImportTeamResponse200]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    team_id: str,
    *,
    client: Client,
    multipart_data: ImportTeamMultipartData,
) -> Optional[Union[Any, ImportTeamResponse200]]:
    """Import a Team from other application

     Import a team into a existing team. Import users, channels, posts, hooks.
    ##### Permissions
    Must have `permission_import_team` permission.

    Args:
        team_id (str):
        multipart_data (ImportTeamMultipartData):

    Returns:
        Response[Union[Any, ImportTeamResponse200]]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
