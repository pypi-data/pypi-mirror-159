from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.set_team_icon_multipart_data import SetTeamIconMultipartData
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    team_id: str,
    *,
    client: Client,
    multipart_data: SetTeamIconMultipartData,
) -> Dict[str, Any]:
    url = "{}/teams/{team_id}/image".format(client.base_url, team_id=team_id)

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
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
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
    multipart_data: SetTeamIconMultipartData,
) -> Response[Union[Any, StatusOK]]:
    """Sets the team icon

     Sets the team icon for the team.

    __Minimum server version__: 4.9

    ##### Permissions
    Must be authenticated and have the `manage_team` permission.

    Args:
        team_id (str):
        multipart_data (SetTeamIconMultipartData):

    Returns:
        Response[Union[Any, StatusOK]]
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
    multipart_data: SetTeamIconMultipartData,
) -> Optional[Union[Any, StatusOK]]:
    """Sets the team icon

     Sets the team icon for the team.

    __Minimum server version__: 4.9

    ##### Permissions
    Must be authenticated and have the `manage_team` permission.

    Args:
        team_id (str):
        multipart_data (SetTeamIconMultipartData):

    Returns:
        Response[Union[Any, StatusOK]]
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
    multipart_data: SetTeamIconMultipartData,
) -> Response[Union[Any, StatusOK]]:
    """Sets the team icon

     Sets the team icon for the team.

    __Minimum server version__: 4.9

    ##### Permissions
    Must be authenticated and have the `manage_team` permission.

    Args:
        team_id (str):
        multipart_data (SetTeamIconMultipartData):

    Returns:
        Response[Union[Any, StatusOK]]
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
    multipart_data: SetTeamIconMultipartData,
) -> Optional[Union[Any, StatusOK]]:
    """Sets the team icon

     Sets the team icon for the team.

    __Minimum server version__: 4.9

    ##### Permissions
    Must be authenticated and have the `manage_team` permission.

    Args:
        team_id (str):
        multipart_data (SetTeamIconMultipartData):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
