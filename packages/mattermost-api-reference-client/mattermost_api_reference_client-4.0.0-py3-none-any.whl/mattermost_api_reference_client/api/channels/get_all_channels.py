from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.channel_with_team_data import ChannelWithTeamData
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    not_associated_to_group: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 0,
    exclude_default_channels: Union[Unset, None, bool] = False,
    include_deleted: Union[Unset, None, bool] = False,
    include_total_count: Union[Unset, None, bool] = False,
    exclude_policy_constrained: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/channels".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["not_associated_to_group"] = not_associated_to_group

    params["page"] = page

    params["per_page"] = per_page

    params["exclude_default_channels"] = exclude_default_channels

    params["include_deleted"] = include_deleted

    params["include_total_count"] = include_total_count

    params["exclude_policy_constrained"] = exclude_policy_constrained

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[ChannelWithTeamData]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_channel_list_with_team_data_item_data in _response_200:
            componentsschemas_channel_list_with_team_data_item = ChannelWithTeamData.from_dict(
                componentsschemas_channel_list_with_team_data_item_data
            )

            response_200.append(componentsschemas_channel_list_with_team_data_item)

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[ChannelWithTeamData]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    not_associated_to_group: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 0,
    exclude_default_channels: Union[Unset, None, bool] = False,
    include_deleted: Union[Unset, None, bool] = False,
    include_total_count: Union[Unset, None, bool] = False,
    exclude_policy_constrained: Union[Unset, None, bool] = False,
) -> Response[Union[Any, List[ChannelWithTeamData]]]:
    """Get a list of all channels

     ##### Permissions
    `manage_system`

    Args:
        not_associated_to_group (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):
        exclude_default_channels (Union[Unset, None, bool]):
        include_deleted (Union[Unset, None, bool]):
        include_total_count (Union[Unset, None, bool]):
        exclude_policy_constrained (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[ChannelWithTeamData]]]
    """

    kwargs = _get_kwargs(
        client=client,
        not_associated_to_group=not_associated_to_group,
        page=page,
        per_page=per_page,
        exclude_default_channels=exclude_default_channels,
        include_deleted=include_deleted,
        include_total_count=include_total_count,
        exclude_policy_constrained=exclude_policy_constrained,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    not_associated_to_group: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 0,
    exclude_default_channels: Union[Unset, None, bool] = False,
    include_deleted: Union[Unset, None, bool] = False,
    include_total_count: Union[Unset, None, bool] = False,
    exclude_policy_constrained: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, List[ChannelWithTeamData]]]:
    """Get a list of all channels

     ##### Permissions
    `manage_system`

    Args:
        not_associated_to_group (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):
        exclude_default_channels (Union[Unset, None, bool]):
        include_deleted (Union[Unset, None, bool]):
        include_total_count (Union[Unset, None, bool]):
        exclude_policy_constrained (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[ChannelWithTeamData]]]
    """

    return sync_detailed(
        client=client,
        not_associated_to_group=not_associated_to_group,
        page=page,
        per_page=per_page,
        exclude_default_channels=exclude_default_channels,
        include_deleted=include_deleted,
        include_total_count=include_total_count,
        exclude_policy_constrained=exclude_policy_constrained,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    not_associated_to_group: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 0,
    exclude_default_channels: Union[Unset, None, bool] = False,
    include_deleted: Union[Unset, None, bool] = False,
    include_total_count: Union[Unset, None, bool] = False,
    exclude_policy_constrained: Union[Unset, None, bool] = False,
) -> Response[Union[Any, List[ChannelWithTeamData]]]:
    """Get a list of all channels

     ##### Permissions
    `manage_system`

    Args:
        not_associated_to_group (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):
        exclude_default_channels (Union[Unset, None, bool]):
        include_deleted (Union[Unset, None, bool]):
        include_total_count (Union[Unset, None, bool]):
        exclude_policy_constrained (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[ChannelWithTeamData]]]
    """

    kwargs = _get_kwargs(
        client=client,
        not_associated_to_group=not_associated_to_group,
        page=page,
        per_page=per_page,
        exclude_default_channels=exclude_default_channels,
        include_deleted=include_deleted,
        include_total_count=include_total_count,
        exclude_policy_constrained=exclude_policy_constrained,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    not_associated_to_group: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 0,
    exclude_default_channels: Union[Unset, None, bool] = False,
    include_deleted: Union[Unset, None, bool] = False,
    include_total_count: Union[Unset, None, bool] = False,
    exclude_policy_constrained: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, List[ChannelWithTeamData]]]:
    """Get a list of all channels

     ##### Permissions
    `manage_system`

    Args:
        not_associated_to_group (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):
        exclude_default_channels (Union[Unset, None, bool]):
        include_deleted (Union[Unset, None, bool]):
        include_total_count (Union[Unset, None, bool]):
        exclude_policy_constrained (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[ChannelWithTeamData]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            not_associated_to_group=not_associated_to_group,
            page=page,
            per_page=per_page,
            exclude_default_channels=exclude_default_channels,
            include_deleted=include_deleted,
            include_total_count=include_total_count,
            exclude_policy_constrained=exclude_policy_constrained,
        )
    ).parsed
