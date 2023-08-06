from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.create_scheme_json_body import CreateSchemeJsonBody
from ...models.scheme import Scheme
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateSchemeJsonBody,
) -> Dict[str, Any]:
    url = "{}/schemes".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Scheme]]:
    if response.status_code == 201:
        response_201 = Scheme.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Scheme]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateSchemeJsonBody,
) -> Response[Union[Any, Scheme]]:
    """Create a scheme

     Create a new scheme.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.0

    Args:
        json_body (CreateSchemeJsonBody):

    Returns:
        Response[Union[Any, Scheme]]
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


def sync(
    *,
    client: Client,
    json_body: CreateSchemeJsonBody,
) -> Optional[Union[Any, Scheme]]:
    """Create a scheme

     Create a new scheme.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.0

    Args:
        json_body (CreateSchemeJsonBody):

    Returns:
        Response[Union[Any, Scheme]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateSchemeJsonBody,
) -> Response[Union[Any, Scheme]]:
    """Create a scheme

     Create a new scheme.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.0

    Args:
        json_body (CreateSchemeJsonBody):

    Returns:
        Response[Union[Any, Scheme]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CreateSchemeJsonBody,
) -> Optional[Union[Any, Scheme]]:
    """Create a scheme

     Create a new scheme.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.0

    Args:
        json_body (CreateSchemeJsonBody):

    Returns:
        Response[Union[Any, Scheme]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
