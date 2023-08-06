from typing import Any, Dict

import httpx

from ...client import Client
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    url: str,
) -> Dict[str, Any]:
    url = "{}/redirect_location".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["url"] = url

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
    *,
    client: Client,
    url: str,
) -> Response[Any]:
    """Get redirect location

     __Minimum server version__: 3.10
    ##### Permissions
    Must be logged in.

    Args:
        url (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        url=url,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    url: str,
) -> Response[Any]:
    """Get redirect location

     __Minimum server version__: 3.10
    ##### Permissions
    Must be logged in.

    Args:
        url (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        url=url,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
