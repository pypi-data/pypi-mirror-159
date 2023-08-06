from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.file_info_list import FileInfoList
from ...models.search_files_multipart_data import SearchFilesMultipartData
from ...types import Response


def _get_kwargs(
    team_id: str,
    *,
    client: Client,
    multipart_data: SearchFilesMultipartData,
) -> Dict[str, Any]:
    url = "{}/teams/{team_id}/files/search".format(client.base_url, team_id=team_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, FileInfoList]]:
    if response.status_code == 200:
        response_200 = FileInfoList.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, FileInfoList]]:
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
    multipart_data: SearchFilesMultipartData,
) -> Response[Union[Any, FileInfoList]]:
    """Search files in a team

     Search for files in a team based on file name, extention and file content (if file content
    extraction is enabled and supported for the files).
    __Minimum server version__: 5.34
    ##### Permissions
    Must be authenticated and have the `view_team` permission.

    Args:
        team_id (str):
        multipart_data (SearchFilesMultipartData):

    Returns:
        Response[Union[Any, FileInfoList]]
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
    multipart_data: SearchFilesMultipartData,
) -> Optional[Union[Any, FileInfoList]]:
    """Search files in a team

     Search for files in a team based on file name, extention and file content (if file content
    extraction is enabled and supported for the files).
    __Minimum server version__: 5.34
    ##### Permissions
    Must be authenticated and have the `view_team` permission.

    Args:
        team_id (str):
        multipart_data (SearchFilesMultipartData):

    Returns:
        Response[Union[Any, FileInfoList]]
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
    multipart_data: SearchFilesMultipartData,
) -> Response[Union[Any, FileInfoList]]:
    """Search files in a team

     Search for files in a team based on file name, extention and file content (if file content
    extraction is enabled and supported for the files).
    __Minimum server version__: 5.34
    ##### Permissions
    Must be authenticated and have the `view_team` permission.

    Args:
        team_id (str):
        multipart_data (SearchFilesMultipartData):

    Returns:
        Response[Union[Any, FileInfoList]]
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
    multipart_data: SearchFilesMultipartData,
) -> Optional[Union[Any, FileInfoList]]:
    """Search files in a team

     Search for files in a team based on file name, extention and file content (if file content
    extraction is enabled and supported for the files).
    __Minimum server version__: 5.34
    ##### Permissions
    Must be authenticated and have the `view_team` permission.

    Args:
        team_id (str):
        multipart_data (SearchFilesMultipartData):

    Returns:
        Response[Union[Any, FileInfoList]]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
