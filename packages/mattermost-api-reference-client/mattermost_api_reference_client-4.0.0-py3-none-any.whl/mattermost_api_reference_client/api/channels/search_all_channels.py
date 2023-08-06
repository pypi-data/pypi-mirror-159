from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.search_all_channels_json_body import SearchAllChannelsJsonBody
from ...models.search_all_channels_response_200 import SearchAllChannelsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: SearchAllChannelsJsonBody,
    system_console: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/channels/search".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["system_console"] = system_console

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, SearchAllChannelsResponse200]]:
    if response.status_code == 200:
        response_200 = SearchAllChannelsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, SearchAllChannelsResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SearchAllChannelsJsonBody,
    system_console: Union[Unset, None, bool] = True,
) -> Response[Union[Any, SearchAllChannelsResponse200]]:
    """Search all private and open type channels across all teams

     Returns all private and open type channels where 'term' matches on the name, display name, or
    purpose of
    the channel.

    Configured 'default' channels (ex Town Square and Off-Topic) can be excluded from the results
    with the `exclude_default_channels` boolean parameter.

    Channels that are associated (via GroupChannel records) to a given group can be excluded from the
    results
    with the `not_associated_to_group` parameter and a group id string.

    Args:
        system_console (Union[Unset, None, bool]):  Default: True.
        json_body (SearchAllChannelsJsonBody):

    Returns:
        Response[Union[Any, SearchAllChannelsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        system_console=system_console,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: SearchAllChannelsJsonBody,
    system_console: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, SearchAllChannelsResponse200]]:
    """Search all private and open type channels across all teams

     Returns all private and open type channels where 'term' matches on the name, display name, or
    purpose of
    the channel.

    Configured 'default' channels (ex Town Square and Off-Topic) can be excluded from the results
    with the `exclude_default_channels` boolean parameter.

    Channels that are associated (via GroupChannel records) to a given group can be excluded from the
    results
    with the `not_associated_to_group` parameter and a group id string.

    Args:
        system_console (Union[Unset, None, bool]):  Default: True.
        json_body (SearchAllChannelsJsonBody):

    Returns:
        Response[Union[Any, SearchAllChannelsResponse200]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        system_console=system_console,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SearchAllChannelsJsonBody,
    system_console: Union[Unset, None, bool] = True,
) -> Response[Union[Any, SearchAllChannelsResponse200]]:
    """Search all private and open type channels across all teams

     Returns all private and open type channels where 'term' matches on the name, display name, or
    purpose of
    the channel.

    Configured 'default' channels (ex Town Square and Off-Topic) can be excluded from the results
    with the `exclude_default_channels` boolean parameter.

    Channels that are associated (via GroupChannel records) to a given group can be excluded from the
    results
    with the `not_associated_to_group` parameter and a group id string.

    Args:
        system_console (Union[Unset, None, bool]):  Default: True.
        json_body (SearchAllChannelsJsonBody):

    Returns:
        Response[Union[Any, SearchAllChannelsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        system_console=system_console,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: SearchAllChannelsJsonBody,
    system_console: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, SearchAllChannelsResponse200]]:
    """Search all private and open type channels across all teams

     Returns all private and open type channels where 'term' matches on the name, display name, or
    purpose of
    the channel.

    Configured 'default' channels (ex Town Square and Off-Topic) can be excluded from the results
    with the `exclude_default_channels` boolean parameter.

    Channels that are associated (via GroupChannel records) to a given group can be excluded from the
    results
    with the `not_associated_to_group` parameter and a group id string.

    Args:
        system_console (Union[Unset, None, bool]):  Default: True.
        json_body (SearchAllChannelsJsonBody):

    Returns:
        Response[Union[Any, SearchAllChannelsResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            system_console=system_console,
        )
    ).parsed
