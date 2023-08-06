from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/cloud/webhook".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
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
    *,
    client: Client,
) -> Response[Any]:
    """POST endpoint for CWS Webhooks

     An endpoint for processing webhooks from the Customer Portal
    ##### Permissions
    This endpoint should only be accessed by CWS, in a Mattermost Cloud instance
    __Minimum server version__: 5.30 __Note:__ This is intended for internal use and is subject to
    change.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Any]:
    """POST endpoint for CWS Webhooks

     An endpoint for processing webhooks from the Customer Portal
    ##### Permissions
    This endpoint should only be accessed by CWS, in a Mattermost Cloud instance
    __Minimum server version__: 5.30 __Note:__ This is intended for internal use and is subject to
    change.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
