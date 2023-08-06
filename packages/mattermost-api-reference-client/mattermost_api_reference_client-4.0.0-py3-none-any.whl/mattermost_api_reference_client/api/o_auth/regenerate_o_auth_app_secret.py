from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.o_auth_app import OAuthApp
from ...types import Response


def _get_kwargs(
    app_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/oauth/apps/{app_id}/regen_secret".format(client.base_url, app_id=app_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, OAuthApp]]:
    if response.status_code == 200:
        response_200 = OAuthApp.from_dict(response.json())

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
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, OAuthApp]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    app_id: str,
    *,
    client: Client,
) -> Response[Union[Any, OAuthApp]]:
    """Regenerate OAuth app secret

     Regenerate the client secret for an OAuth 2.0 client application registered with Mattermost.
    ##### Permissions
    If app creator, must have `mange_oauth` permission otherwise `manage_system_wide_oauth` permission
    is required.

    Args:
        app_id (str):

    Returns:
        Response[Union[Any, OAuthApp]]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    app_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, OAuthApp]]:
    """Regenerate OAuth app secret

     Regenerate the client secret for an OAuth 2.0 client application registered with Mattermost.
    ##### Permissions
    If app creator, must have `mange_oauth` permission otherwise `manage_system_wide_oauth` permission
    is required.

    Args:
        app_id (str):

    Returns:
        Response[Union[Any, OAuthApp]]
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: Client,
) -> Response[Union[Any, OAuthApp]]:
    """Regenerate OAuth app secret

     Regenerate the client secret for an OAuth 2.0 client application registered with Mattermost.
    ##### Permissions
    If app creator, must have `mange_oauth` permission otherwise `manage_system_wide_oauth` permission
    is required.

    Args:
        app_id (str):

    Returns:
        Response[Union[Any, OAuthApp]]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    app_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, OAuthApp]]:
    """Regenerate OAuth app secret

     Regenerate the client secret for an OAuth 2.0 client application registered with Mattermost.
    ##### Permissions
    If app creator, must have `mange_oauth` permission otherwise `manage_system_wide_oauth` permission
    is required.

    Args:
        app_id (str):

    Returns:
        Response[Union[Any, OAuthApp]]
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
        )
    ).parsed
