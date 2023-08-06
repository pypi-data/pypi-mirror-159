from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.channel import Channel
from ...models.search_group_channels_json_body import SearchGroupChannelsJsonBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: SearchGroupChannelsJsonBody,
) -> Dict[str, Any]:
    url = "{}/channels/group/search".format(client.base_url)

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
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[Channel]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SearchGroupChannelsJsonBody,
) -> Response[Union[Any, List[Channel]]]:
    """Search Group Channels

     Get a list of group channels for a user which members' usernames match the search term.

    __Minimum server version__: 5.14

    Args:
        json_body (SearchGroupChannelsJsonBody):

    Returns:
        Response[Union[Any, List[Channel]]]
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
    json_body: SearchGroupChannelsJsonBody,
) -> Optional[Union[Any, List[Channel]]]:
    """Search Group Channels

     Get a list of group channels for a user which members' usernames match the search term.

    __Minimum server version__: 5.14

    Args:
        json_body (SearchGroupChannelsJsonBody):

    Returns:
        Response[Union[Any, List[Channel]]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SearchGroupChannelsJsonBody,
) -> Response[Union[Any, List[Channel]]]:
    """Search Group Channels

     Get a list of group channels for a user which members' usernames match the search term.

    __Minimum server version__: 5.14

    Args:
        json_body (SearchGroupChannelsJsonBody):

    Returns:
        Response[Union[Any, List[Channel]]]
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
    json_body: SearchGroupChannelsJsonBody,
) -> Optional[Union[Any, List[Channel]]]:
    """Search Group Channels

     Get a list of group channels for a user which members' usernames match the search term.

    __Minimum server version__: 5.14

    Args:
        json_body (SearchGroupChannelsJsonBody):

    Returns:
        Response[Union[Any, List[Channel]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
