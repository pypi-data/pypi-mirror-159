from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.channel import Channel
from ...types import UNSET, Response


def _get_kwargs(
    team_id: str,
    *,
    client: Client,
    name: str,
) -> Dict[str, Any]:
    url = "{}/teams/{team_id}/channels/autocomplete".format(client.base_url, team_id=team_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[Channel]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Channel.from_dict(response_200_item_data)

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
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[Channel]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    team_id: str,
    *,
    client: Client,
    name: str,
) -> Response[Union[Any, List[Channel]]]:
    """Autocomplete channels

     Autocomplete public channels on a team based on the search term provided in the request URL.

    __Minimum server version__: 4.7

    ##### Permissions
    Must have the `list_team_channels` permission.

    Args:
        team_id (str):
        name (str):

    Returns:
        Response[Union[Any, List[Channel]]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        name=name,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    team_id: str,
    *,
    client: Client,
    name: str,
) -> Optional[Union[Any, List[Channel]]]:
    """Autocomplete channels

     Autocomplete public channels on a team based on the search term provided in the request URL.

    __Minimum server version__: 4.7

    ##### Permissions
    Must have the `list_team_channels` permission.

    Args:
        team_id (str):
        name (str):

    Returns:
        Response[Union[Any, List[Channel]]]
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        name=name,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    *,
    client: Client,
    name: str,
) -> Response[Union[Any, List[Channel]]]:
    """Autocomplete channels

     Autocomplete public channels on a team based on the search term provided in the request URL.

    __Minimum server version__: 4.7

    ##### Permissions
    Must have the `list_team_channels` permission.

    Args:
        team_id (str):
        name (str):

    Returns:
        Response[Union[Any, List[Channel]]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        name=name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    team_id: str,
    *,
    client: Client,
    name: str,
) -> Optional[Union[Any, List[Channel]]]:
    """Autocomplete channels

     Autocomplete public channels on a team based on the search term provided in the request URL.

    __Minimum server version__: 4.7

    ##### Permissions
    Must have the `list_team_channels` permission.

    Args:
        team_id (str):
        name (str):

    Returns:
        Response[Union[Any, List[Channel]]]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            name=name,
        )
    ).parsed
