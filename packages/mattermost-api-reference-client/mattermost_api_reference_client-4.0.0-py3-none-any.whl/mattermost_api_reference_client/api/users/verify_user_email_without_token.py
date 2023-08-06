from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.user import User
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/email/verify/member".format(client.base_url, user_id=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, User]]:
    if response.status_code == 200:
        response_200 = User.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, User]]:
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
) -> Response[Union[Any, User]]:
    """Verify user email by ID

     Verify the email used by a user without a token.

    __Minimum server version__: 5.24

    ##### Permissions

    Must have `manage_system` permission.

    Args:
        user_id (str):

    Returns:
        Response[Union[Any, User]]
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
) -> Optional[Union[Any, User]]:
    """Verify user email by ID

     Verify the email used by a user without a token.

    __Minimum server version__: 5.24

    ##### Permissions

    Must have `manage_system` permission.

    Args:
        user_id (str):

    Returns:
        Response[Union[Any, User]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Client,
) -> Response[Union[Any, User]]:
    """Verify user email by ID

     Verify the email used by a user without a token.

    __Minimum server version__: 5.24

    ##### Permissions

    Must have `manage_system` permission.

    Args:
        user_id (str):

    Returns:
        Response[Union[Any, User]]
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
) -> Optional[Union[Any, User]]:
    """Verify user email by ID

     Verify the email used by a user without a token.

    __Minimum server version__: 5.24

    ##### Permissions

    Must have `manage_system` permission.

    Args:
        user_id (str):

    Returns:
        Response[Union[Any, User]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
