from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.scheme import Scheme
from ...types import Response


def _get_kwargs(
    scheme_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/schemes/{scheme_id}".format(client.base_url, scheme_id=scheme_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Scheme]]:
    if response.status_code == 200:
        response_200 = Scheme.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Scheme]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    scheme_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Scheme]]:
    """Get a scheme

     Get a scheme from the provided scheme id.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.0

    Args:
        scheme_id (str):

    Returns:
        Response[Union[Any, Scheme]]
    """

    kwargs = _get_kwargs(
        scheme_id=scheme_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    scheme_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Scheme]]:
    """Get a scheme

     Get a scheme from the provided scheme id.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.0

    Args:
        scheme_id (str):

    Returns:
        Response[Union[Any, Scheme]]
    """

    return sync_detailed(
        scheme_id=scheme_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    scheme_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Scheme]]:
    """Get a scheme

     Get a scheme from the provided scheme id.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.0

    Args:
        scheme_id (str):

    Returns:
        Response[Union[Any, Scheme]]
    """

    kwargs = _get_kwargs(
        scheme_id=scheme_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    scheme_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Scheme]]:
    """Get a scheme

     Get a scheme from the provided scheme id.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.0

    Args:
        scheme_id (str):

    Returns:
        Response[Union[Any, Scheme]]
    """

    return (
        await asyncio_detailed(
            scheme_id=scheme_id,
            client=client,
        )
    ).parsed
