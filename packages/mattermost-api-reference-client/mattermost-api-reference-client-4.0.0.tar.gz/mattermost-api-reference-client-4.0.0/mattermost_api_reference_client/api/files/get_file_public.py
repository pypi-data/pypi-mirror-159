from typing import Any, Dict

import httpx

from ...client import Client
from ...types import UNSET, Response


def _get_kwargs(
    file_id: str,
    *,
    client: Client,
    h: str,
) -> Dict[str, Any]:
    url = "{}/files/{file_id}/public".format(client.base_url, file_id=file_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["h"] = h

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    file_id: str,
    *,
    client: Client,
    h: str,
) -> Response[Any]:
    """Get a public file

     ##### Permissions
    No permissions required.

    Args:
        file_id (str):
        h (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
        client=client,
        h=h,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    file_id: str,
    *,
    client: Client,
    h: str,
) -> Response[Any]:
    """Get a public file

     ##### Permissions
    No permissions required.

    Args:
        file_id (str):
        h (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
        client=client,
        h=h,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
