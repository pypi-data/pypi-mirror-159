from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.upload_file_multipart_data import UploadFileMultipartData
from ...models.upload_file_response_201 import UploadFileResponse201
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    multipart_data: UploadFileMultipartData,
    channel_id: Union[Unset, None, str] = UNSET,
    filename: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/files".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["channel_id"] = channel_id

    params["filename"] = filename

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, UploadFileResponse201]]:
    if response.status_code == 201:
        response_201 = UploadFileResponse201.from_dict(response.json())

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
    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, UploadFileResponse201]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    multipart_data: UploadFileMultipartData,
    channel_id: Union[Unset, None, str] = UNSET,
    filename: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, UploadFileResponse201]]:
    """Upload a file

     Uploads a file that can later be attached to a post.

    This request can either be a multipart/form-data request with a channel_id, files and optional
    client_ids defined in the FormData, or it can be a request with the channel_id and filename
    defined as query parameters with the contents of a single file in the body of the request.

    Only multipart/form-data requests are supported by server versions up to and including 4.7.
    Server versions 4.8 and higher support both types of requests.

    ##### Permissions
    Must have `upload_file` permission.

    Args:
        channel_id (Union[Unset, None, str]):
        filename (Union[Unset, None, str]):
        multipart_data (UploadFileMultipartData):

    Returns:
        Response[Union[Any, UploadFileResponse201]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        channel_id=channel_id,
        filename=filename,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    multipart_data: UploadFileMultipartData,
    channel_id: Union[Unset, None, str] = UNSET,
    filename: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, UploadFileResponse201]]:
    """Upload a file

     Uploads a file that can later be attached to a post.

    This request can either be a multipart/form-data request with a channel_id, files and optional
    client_ids defined in the FormData, or it can be a request with the channel_id and filename
    defined as query parameters with the contents of a single file in the body of the request.

    Only multipart/form-data requests are supported by server versions up to and including 4.7.
    Server versions 4.8 and higher support both types of requests.

    ##### Permissions
    Must have `upload_file` permission.

    Args:
        channel_id (Union[Unset, None, str]):
        filename (Union[Unset, None, str]):
        multipart_data (UploadFileMultipartData):

    Returns:
        Response[Union[Any, UploadFileResponse201]]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
        channel_id=channel_id,
        filename=filename,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: UploadFileMultipartData,
    channel_id: Union[Unset, None, str] = UNSET,
    filename: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, UploadFileResponse201]]:
    """Upload a file

     Uploads a file that can later be attached to a post.

    This request can either be a multipart/form-data request with a channel_id, files and optional
    client_ids defined in the FormData, or it can be a request with the channel_id and filename
    defined as query parameters with the contents of a single file in the body of the request.

    Only multipart/form-data requests are supported by server versions up to and including 4.7.
    Server versions 4.8 and higher support both types of requests.

    ##### Permissions
    Must have `upload_file` permission.

    Args:
        channel_id (Union[Unset, None, str]):
        filename (Union[Unset, None, str]):
        multipart_data (UploadFileMultipartData):

    Returns:
        Response[Union[Any, UploadFileResponse201]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        channel_id=channel_id,
        filename=filename,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    multipart_data: UploadFileMultipartData,
    channel_id: Union[Unset, None, str] = UNSET,
    filename: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, UploadFileResponse201]]:
    """Upload a file

     Uploads a file that can later be attached to a post.

    This request can either be a multipart/form-data request with a channel_id, files and optional
    client_ids defined in the FormData, or it can be a request with the channel_id and filename
    defined as query parameters with the contents of a single file in the body of the request.

    Only multipart/form-data requests are supported by server versions up to and including 4.7.
    Server versions 4.8 and higher support both types of requests.

    ##### Permissions
    Must have `upload_file` permission.

    Args:
        channel_id (Union[Unset, None, str]):
        filename (Union[Unset, None, str]):
        multipart_data (UploadFileMultipartData):

    Returns:
        Response[Union[Any, UploadFileResponse201]]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
            channel_id=channel_id,
            filename=filename,
        )
    ).parsed
