from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    invoice_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/cloud/subscription/invoices/{invoice_id}/pdf".format(client.base_url, invoice_id=invoice_id)

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
    invoice_id: str,
    *,
    client: Client,
) -> Response[Any]:
    """Get cloud invoice PDF

     Retrieves the PDF for the invoice passed as parameter
    ##### Permissions
    Must have `manage_system` permission and be licensed for Cloud.
    __Minimum server version__: 5.30 __Note:__ This is intended for internal use and is subject to
    change.

    Args:
        invoice_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    invoice_id: str,
    *,
    client: Client,
) -> Response[Any]:
    """Get cloud invoice PDF

     Retrieves the PDF for the invoice passed as parameter
    ##### Permissions
    Must have `manage_system` permission and be licensed for Cloud.
    __Minimum server version__: 5.30 __Note:__ This is intended for internal use and is subject to
    change.

    Args:
        invoice_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        invoice_id=invoice_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
