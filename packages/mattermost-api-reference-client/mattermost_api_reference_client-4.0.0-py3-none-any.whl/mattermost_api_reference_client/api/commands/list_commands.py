from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.command import Command
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    team_id: Union[Unset, None, str] = UNSET,
    custom_only: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/commands".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["team_id"] = team_id

    params["custom_only"] = custom_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[Command]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Command.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[Command]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    team_id: Union[Unset, None, str] = UNSET,
    custom_only: Union[Unset, None, bool] = False,
) -> Response[Union[Any, List[Command]]]:
    """List commands for a team

     List commands for a team.
    ##### Permissions
    `manage_slash_commands` if need list custom commands.

    Args:
        team_id (Union[Unset, None, str]):
        custom_only (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Command]]]
    """

    kwargs = _get_kwargs(
        client=client,
        team_id=team_id,
        custom_only=custom_only,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    team_id: Union[Unset, None, str] = UNSET,
    custom_only: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, List[Command]]]:
    """List commands for a team

     List commands for a team.
    ##### Permissions
    `manage_slash_commands` if need list custom commands.

    Args:
        team_id (Union[Unset, None, str]):
        custom_only (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Command]]]
    """

    return sync_detailed(
        client=client,
        team_id=team_id,
        custom_only=custom_only,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    team_id: Union[Unset, None, str] = UNSET,
    custom_only: Union[Unset, None, bool] = False,
) -> Response[Union[Any, List[Command]]]:
    """List commands for a team

     List commands for a team.
    ##### Permissions
    `manage_slash_commands` if need list custom commands.

    Args:
        team_id (Union[Unset, None, str]):
        custom_only (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Command]]]
    """

    kwargs = _get_kwargs(
        client=client,
        team_id=team_id,
        custom_only=custom_only,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    team_id: Union[Unset, None, str] = UNSET,
    custom_only: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, List[Command]]]:
    """List commands for a team

     List commands for a team.
    ##### Permissions
    `manage_slash_commands` if need list custom commands.

    Args:
        team_id (Union[Unset, None, str]):
        custom_only (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Command]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            team_id=team_id,
            custom_only=custom_only,
        )
    ).parsed
