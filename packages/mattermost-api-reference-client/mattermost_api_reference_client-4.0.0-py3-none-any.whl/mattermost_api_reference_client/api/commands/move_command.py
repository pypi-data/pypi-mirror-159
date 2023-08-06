from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.move_command_json_body import MoveCommandJsonBody
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    command_id: str,
    *,
    client: Client,
    json_body: MoveCommandJsonBody,
) -> Dict[str, Any]:
    url = "{}/commands/{command_id}/move".format(client.base_url, command_id=command_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, StatusOK]]:
    if response.status_code == 200:
        response_200 = StatusOK.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, StatusOK]]:
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
    json_body: MoveCommandJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Move a command

     Move a command to a different team based on command id string.
    ##### Permissions
    Must have `manage_slash_commands` permission for the team the command is currently in and the
    destination team.

    __Minimum server version__: 5.22

    Args:
        command_id (str):
        json_body (MoveCommandJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        command_id=command_id,
        client=client,
        json_body=json_body,
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
    json_body: MoveCommandJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Move a command

     Move a command to a different team based on command id string.
    ##### Permissions
    Must have `manage_slash_commands` permission for the team the command is currently in and the
    destination team.

    __Minimum server version__: 5.22

    Args:
        command_id (str):
        json_body (MoveCommandJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        command_id=command_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    command_id: str,
    *,
    client: Client,
    json_body: MoveCommandJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Move a command

     Move a command to a different team based on command id string.
    ##### Permissions
    Must have `manage_slash_commands` permission for the team the command is currently in and the
    destination team.

    __Minimum server version__: 5.22

    Args:
        command_id (str):
        json_body (MoveCommandJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        command_id=command_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    command_id: str,
    *,
    client: Client,
    json_body: MoveCommandJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Move a command

     Move a command to a different team based on command id string.
    ##### Permissions
    Must have `manage_slash_commands` permission for the team the command is currently in and the
    destination team.

    __Minimum server version__: 5.22

    Args:
        command_id (str):
        json_body (MoveCommandJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            command_id=command_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
