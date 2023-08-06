from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/saml/certificate/public".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, StatusOK]]:
    if response.status_code == 200:
        response_200 = StatusOK.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, StatusOK]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, StatusOK]]:
    """Remove public certificate

     Delete the current public certificate being used with your SAML configuration. This will also
    disable encryption for SAML on your system as this certificate is required for that.
    ##### Permissions
    Must have `sysconsole_write_authentication` permission.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[Any, StatusOK]]:
    """Remove public certificate

     Delete the current public certificate being used with your SAML configuration. This will also
    disable encryption for SAML on your system as this certificate is required for that.
    ##### Permissions
    Must have `sysconsole_write_authentication` permission.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, StatusOK]]:
    """Remove public certificate

     Delete the current public certificate being used with your SAML configuration. This will also
    disable encryption for SAML on your system as this certificate is required for that.
    ##### Permissions
    Must have `sysconsole_write_authentication` permission.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[Any, StatusOK]]:
    """Remove public certificate

     Delete the current public certificate being used with your SAML configuration. This will also
    disable encryption for SAML on your system as this certificate is required for that.
    ##### Permissions
    Must have `sysconsole_write_authentication` permission.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
