from typing import Any, Dict

import httpx

from ...client import Client
from ...models.request_trial_license_json_body import RequestTrialLicenseJsonBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: RequestTrialLicenseJsonBody,
) -> Dict[str, Any]:
    url = "{}/trial-license".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: RequestTrialLicenseJsonBody,
) -> Response[Any]:
    """Request and install a trial license for your server

     Request and install a trial license for your server
    __Minimum server version__: 5.25
    ##### Permissions
    Must have `manage_system` permission.

    Args:
        json_body (RequestTrialLicenseJsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    json_body: RequestTrialLicenseJsonBody,
) -> Response[Any]:
    """Request and install a trial license for your server

     Request and install a trial license for your server
    __Minimum server version__: 5.25
    ##### Permissions
    Must have `manage_system` permission.

    Args:
        json_body (RequestTrialLicenseJsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
