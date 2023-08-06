from typing import Any, Dict

import httpx

from ...client import Client
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
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    upload_id: str,
    *,
    client: Client,
) -> Response[Any]:
    """Get an upload session

     Gets an upload session that has been previously created.

    ##### Permissions
    Must be logged in as the user who created the upload session.

    Args:
        upload_id (str):

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    upload_id: str,
    *,
    client: Client,
) -> Response[Any]:
    """Get an upload session

     Gets an upload session that has been previously created.

    ##### Permissions
    Must be logged in as the user who created the upload session.

    Args:
        upload_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        upload_id=upload_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
