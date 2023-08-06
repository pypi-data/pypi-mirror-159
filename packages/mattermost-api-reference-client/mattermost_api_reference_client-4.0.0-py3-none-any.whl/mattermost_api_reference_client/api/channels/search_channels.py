from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.channel import Channel
from ...models.search_channels_json_body import SearchChannelsJsonBody
from ...types import Response


def _get_kwargs(
    team_id: str,
    *,
    client: Client,
    json_body: SearchChannelsJsonBody,
) -> Dict[str, Any]:
    url = "{}/teams/{team_id}/channels/search".format(client.base_url, team_id=team_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[Channel]]]:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = Channel.from_dict(response_201_item_data)

            response_201.append(response_201_item)

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
    json_body: SearchChannelsJsonBody,
) -> Response[Union[Any, List[Channel]]]:
    """Search channels

     Search public channels on a team based on the search term provided in the request body.
    ##### Permissions
    Must have the `list_team_channels` permission.

    In server version 5.16 and later, a user without the `list_team_channels` permission will be able to
    use this endpoint, with the search results limited to the channels that the user is a member of.

    Args:
        team_id (str):
        json_body (SearchChannelsJsonBody):

    Returns:
        Response[Union[Any, List[Channel]]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        json_body=json_body,
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
    json_body: SearchChannelsJsonBody,
) -> Optional[Union[Any, List[Channel]]]:
    """Search channels

     Search public channels on a team based on the search term provided in the request body.
    ##### Permissions
    Must have the `list_team_channels` permission.

    In server version 5.16 and later, a user without the `list_team_channels` permission will be able to
    use this endpoint, with the search results limited to the channels that the user is a member of.

    Args:
        team_id (str):
        json_body (SearchChannelsJsonBody):

    Returns:
        Response[Union[Any, List[Channel]]]
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    *,
    client: Client,
    json_body: SearchChannelsJsonBody,
) -> Response[Union[Any, List[Channel]]]:
    """Search channels

     Search public channels on a team based on the search term provided in the request body.
    ##### Permissions
    Must have the `list_team_channels` permission.

    In server version 5.16 and later, a user without the `list_team_channels` permission will be able to
    use this endpoint, with the search results limited to the channels that the user is a member of.

    Args:
        team_id (str):
        json_body (SearchChannelsJsonBody):

    Returns:
        Response[Union[Any, List[Channel]]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    team_id: str,
    *,
    client: Client,
    json_body: SearchChannelsJsonBody,
) -> Optional[Union[Any, List[Channel]]]:
    """Search channels

     Search public channels on a team based on the search term provided in the request body.
    ##### Permissions
    Must have the `list_team_channels` permission.

    In server version 5.16 and later, a user without the `list_team_channels` permission will be able to
    use this endpoint, with the search results limited to the channels that the user is a member of.

    Args:
        team_id (str):
        json_body (SearchChannelsJsonBody):

    Returns:
        Response[Union[Any, List[Channel]]]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
