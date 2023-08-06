from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.user_access_token_sanitized import UserAccessTokenSanitized
from ...types import Response


def _get_kwargs(
    token_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users/tokens/{token_id}".format(client.base_url, token_id=token_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, UserAccessTokenSanitized]]:
    if response.status_code == 200:
        response_200 = UserAccessTokenSanitized.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, UserAccessTokenSanitized]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    token_id: str,
    *,
    client: Client,
) -> Response[Union[Any, UserAccessTokenSanitized]]:
    """Get a user access token

     Get a user access token. Does not include the actual authentication token.

    __Minimum server version__: 4.1

    ##### Permissions
    Must have `read_user_access_token` permission. For non-self requests, must also have the
    `edit_other_users` permission.

    Args:
        token_id (str):

    Returns:
        Response[Union[Any, UserAccessTokenSanitized]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    token_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, UserAccessTokenSanitized]]:
    """Get a user access token

     Get a user access token. Does not include the actual authentication token.

    __Minimum server version__: 4.1

    ##### Permissions
    Must have `read_user_access_token` permission. For non-self requests, must also have the
    `edit_other_users` permission.

    Args:
        token_id (str):

    Returns:
        Response[Union[Any, UserAccessTokenSanitized]]
    """

    return sync_detailed(
        token_id=token_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    token_id: str,
    *,
    client: Client,
) -> Response[Union[Any, UserAccessTokenSanitized]]:
    """Get a user access token

     Get a user access token. Does not include the actual authentication token.

    __Minimum server version__: 4.1

    ##### Permissions
    Must have `read_user_access_token` permission. For non-self requests, must also have the
    `edit_other_users` permission.

    Args:
        token_id (str):

    Returns:
        Response[Union[Any, UserAccessTokenSanitized]]
    """

    kwargs = _get_kwargs(
        token_id=token_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    token_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, UserAccessTokenSanitized]]:
    """Get a user access token

     Get a user access token. Does not include the actual authentication token.

    __Minimum server version__: 4.1

    ##### Permissions
    Must have `read_user_access_token` permission. For non-self requests, must also have the
    `edit_other_users` permission.

    Args:
        token_id (str):

    Returns:
        Response[Union[Any, UserAccessTokenSanitized]]
    """

    return (
        await asyncio_detailed(
            token_id=token_id,
            client=client,
        )
    ).parsed
