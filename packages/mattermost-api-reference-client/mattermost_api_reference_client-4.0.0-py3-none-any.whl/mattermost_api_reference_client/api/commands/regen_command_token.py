from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.regen_command_token_response_200 import RegenCommandTokenResponse200
from ...types import Response


def _get_kwargs(
    command_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/commands/{command_id}/regen_token".format(client.base_url, command_id=command_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RegenCommandTokenResponse200]]:
    if response.status_code == 200:
        response_200 = RegenCommandTokenResponse200.from_dict(response.json())

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
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RegenCommandTokenResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    command_id: str,
    *,
    client: Client,
) -> Response[Union[Any, RegenCommandTokenResponse200]]:
    """Generate a new token

     Generate a new token for the command based on command id string.
    ##### Permissions
    Must have `manage_slash_commands` permission for the team the command is in.

    Args:
        command_id (str):

    Returns:
        Response[Union[Any, RegenCommandTokenResponse200]]
    """

    kwargs = _get_kwargs(
        command_id=command_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    command_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, RegenCommandTokenResponse200]]:
    """Generate a new token

     Generate a new token for the command based on command id string.
    ##### Permissions
    Must have `manage_slash_commands` permission for the team the command is in.

    Args:
        command_id (str):

    Returns:
        Response[Union[Any, RegenCommandTokenResponse200]]
    """

    return sync_detailed(
        command_id=command_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    command_id: str,
    *,
    client: Client,
) -> Response[Union[Any, RegenCommandTokenResponse200]]:
    """Generate a new token

     Generate a new token for the command based on command id string.
    ##### Permissions
    Must have `manage_slash_commands` permission for the team the command is in.

    Args:
        command_id (str):

    Returns:
        Response[Union[Any, RegenCommandTokenResponse200]]
    """

    kwargs = _get_kwargs(
        command_id=command_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    command_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, RegenCommandTokenResponse200]]:
    """Generate a new token

     Generate a new token for the command based on command id string.
    ##### Permissions
    Must have `manage_slash_commands` permission for the team the command is in.

    Args:
        command_id (str):

    Returns:
        Response[Union[Any, RegenCommandTokenResponse200]]
    """

    return (
        await asyncio_detailed(
            command_id=command_id,
            client=client,
        )
    ).parsed
