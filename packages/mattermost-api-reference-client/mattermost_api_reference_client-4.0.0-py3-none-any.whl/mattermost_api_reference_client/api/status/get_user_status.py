from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.status import Status
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/status".format(client.base_url, user_id=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Status]]:
    if response.status_code == 200:
        response_200 = Status.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Status]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Status]]:
    """Get user status

     Get user status by id from the server.
    ##### Permissions
    Must be authenticated.

    Args:
        user_id (str):

    Returns:
        Response[Union[Any, Status]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Status]]:
    """Get user status

     Get user status by id from the server.
    ##### Permissions
    Must be authenticated.

    Args:
        user_id (str):

    Returns:
        Response[Union[Any, Status]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Status]]:
    """Get user status

     Get user status by id from the server.
    ##### Permissions
    Must be authenticated.

    Args:
        user_id (str):

    Returns:
        Response[Union[Any, Status]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Status]]:
    """Get user status

     Get user status by id from the server.
    ##### Permissions
    Must be authenticated.

    Args:
        user_id (str):

    Returns:
        Response[Union[Any, Status]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
