from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.file_info import FileInfo
from ...types import Response


def _get_kwargs(
    upload_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/uploads/{upload_id}".format(client.base_url, upload_id=upload_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, FileInfo]]:
    if response.status_code == 201:
        response_201 = FileInfo.from_dict(response.json())

        return response_201
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
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
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, FileInfo]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    upload_id: str,
    *,
    client: Client,
) -> Response[Union[Any, FileInfo]]:
    """Perform a file upload

     Starts or resumes a file upload.
    To resume an existing (incomplete) upload, data should be sent starting from the offset specified in
    the upload session object.

    The request body can be in one of two formats:
    - Binary file content streamed in request's body
    - multipart/form-data

    ##### Permissions
    Must be logged in as the user who created the upload session.

    Args:
        upload_id (str):

    Returns:
        Response[Union[Any, FileInfo]]
    """

    kwargs = _get_kwargs(
        upload_id=upload_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    upload_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, FileInfo]]:
    """Perform a file upload

     Starts or resumes a file upload.
    To resume an existing (incomplete) upload, data should be sent starting from the offset specified in
    the upload session object.

    The request body can be in one of two formats:
    - Binary file content streamed in request's body
    - multipart/form-data

    ##### Permissions
    Must be logged in as the user who created the upload session.

    Args:
        upload_id (str):

    Returns:
        Response[Union[Any, FileInfo]]
    """

    return sync_detailed(
        upload_id=upload_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    upload_id: str,
    *,
    client: Client,
) -> Response[Union[Any, FileInfo]]:
    """Perform a file upload

     Starts or resumes a file upload.
    To resume an existing (incomplete) upload, data should be sent starting from the offset specified in
    the upload session object.

    The request body can be in one of two formats:
    - Binary file content streamed in request's body
    - multipart/form-data

    ##### Permissions
    Must be logged in as the user who created the upload session.

    Args:
        upload_id (str):

    Returns:
        Response[Union[Any, FileInfo]]
    """

    kwargs = _get_kwargs(
        upload_id=upload_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    upload_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, FileInfo]]:
    """Perform a file upload

     Starts or resumes a file upload.
    To resume an existing (incomplete) upload, data should be sent starting from the offset specified in
    the upload session object.

    The request body can be in one of two formats:
    - Binary file content streamed in request's body
    - multipart/form-data

    ##### Permissions
    Must be logged in as the user who created the upload session.

    Args:
        upload_id (str):

    Returns:
        Response[Union[Any, FileInfo]]
    """

    return (
        await asyncio_detailed(
            upload_id=upload_id,
            client=client,
        )
    ).parsed
