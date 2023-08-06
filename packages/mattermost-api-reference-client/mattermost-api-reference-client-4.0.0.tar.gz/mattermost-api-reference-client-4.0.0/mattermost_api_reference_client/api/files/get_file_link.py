from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_file_link_response_200 import GetFileLinkResponse200
from ...types import Response


def _get_kwargs(
    file_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/files/{file_id}/link".format(client.base_url, file_id=file_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GetFileLinkResponse200]]:
    if response.status_code == 200:
        response_200 = GetFileLinkResponse200.from_dict(response.json())

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
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, GetFileLinkResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    file_id: str,
    *,
    client: Client,
) -> Response[Union[Any, GetFileLinkResponse200]]:
    """Get a public file link

     Gets a public link for a file that can be accessed without logging into Mattermost.
    ##### Permissions
    Must have `read_channel` permission or be uploader of the file.

    Args:
        file_id (str):

    Returns:
        Response[Union[Any, GetFileLinkResponse200]]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    file_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, GetFileLinkResponse200]]:
    """Get a public file link

     Gets a public link for a file that can be accessed without logging into Mattermost.
    ##### Permissions
    Must have `read_channel` permission or be uploader of the file.

    Args:
        file_id (str):

    Returns:
        Response[Union[Any, GetFileLinkResponse200]]
    """

    return sync_detailed(
        file_id=file_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    file_id: str,
    *,
    client: Client,
) -> Response[Union[Any, GetFileLinkResponse200]]:
    """Get a public file link

     Gets a public link for a file that can be accessed without logging into Mattermost.
    ##### Permissions
    Must have `read_channel` permission or be uploader of the file.

    Args:
        file_id (str):

    Returns:
        Response[Union[Any, GetFileLinkResponse200]]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    file_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, GetFileLinkResponse200]]:
    """Get a public file link

     Gets a public link for a file that can be accessed without logging into Mattermost.
    ##### Permissions
    Must have `read_channel` permission or be uploader of the file.

    Args:
        file_id (str):

    Returns:
        Response[Union[Any, GetFileLinkResponse200]]
    """

    return (
        await asyncio_detailed(
            file_id=file_id,
            client=client,
        )
    ).parsed
