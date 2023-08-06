from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.terms_of_service import TermsOfService
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/terms_of_service".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, TermsOfService]]:
    if response.status_code == 200:
        response_200 = TermsOfService.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, TermsOfService]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, TermsOfService]]:
    """Get latest terms of service

     Get latest terms of service from the server

    __Minimum server version__: 5.4
    ##### Permissions
    Must be authenticated.

    Returns:
        Response[Union[Any, TermsOfService]]
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
) -> Optional[Union[Any, TermsOfService]]:
    """Get latest terms of service

     Get latest terms of service from the server

    __Minimum server version__: 5.4
    ##### Permissions
    Must be authenticated.

    Returns:
        Response[Union[Any, TermsOfService]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, TermsOfService]]:
    """Get latest terms of service

     Get latest terms of service from the server

    __Minimum server version__: 5.4
    ##### Permissions
    Must be authenticated.

    Returns:
        Response[Union[Any, TermsOfService]]
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
) -> Optional[Union[Any, TermsOfService]]:
    """Get latest terms of service

     Get latest terms of service from the server

    __Minimum server version__: 5.4
    ##### Permissions
    Must be authenticated.

    Returns:
        Response[Union[Any, TermsOfService]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
