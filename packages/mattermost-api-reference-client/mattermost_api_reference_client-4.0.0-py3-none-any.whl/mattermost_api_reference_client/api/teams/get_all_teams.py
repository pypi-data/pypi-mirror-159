from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.team import Team
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    include_total_count: Union[Unset, None, bool] = False,
    exclude_policy_constrained: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/teams".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["per_page"] = per_page

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[Team]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Team.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[Team]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    include_total_count: Union[Unset, None, bool] = False,
    exclude_policy_constrained: Union[Unset, None, bool] = False,
) -> Response[Union[Any, List[Team]]]:
    """Get teams

     For regular users only returns open teams. Users with the \"manage_system\" permission will return
    teams regardless of type. The result is based on query string parameters - page and per_page.
    ##### Permissions
    Must be authenticated. \"manage_system\" permission is required to show all teams.

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        include_total_count (Union[Unset, None, bool]):
        exclude_policy_constrained (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Team]]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
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
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    include_total_count: Union[Unset, None, bool] = False,
    exclude_policy_constrained: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, List[Team]]]:
    """Get teams

     For regular users only returns open teams. Users with the \"manage_system\" permission will return
    teams regardless of type. The result is based on query string parameters - page and per_page.
    ##### Permissions
    Must be authenticated. \"manage_system\" permission is required to show all teams.

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        include_total_count (Union[Unset, None, bool]):
        exclude_policy_constrained (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Team]]]
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        include_total_count=include_total_count,
        exclude_policy_constrained=exclude_policy_constrained,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    include_total_count: Union[Unset, None, bool] = False,
    exclude_policy_constrained: Union[Unset, None, bool] = False,
) -> Response[Union[Any, List[Team]]]:
    """Get teams

     For regular users only returns open teams. Users with the \"manage_system\" permission will return
    teams regardless of type. The result is based on query string parameters - page and per_page.
    ##### Permissions
    Must be authenticated. \"manage_system\" permission is required to show all teams.

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        include_total_count (Union[Unset, None, bool]):
        exclude_policy_constrained (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Team]]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
        include_total_count=include_total_count,
        exclude_policy_constrained=exclude_policy_constrained,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    include_total_count: Union[Unset, None, bool] = False,
    exclude_policy_constrained: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, List[Team]]]:
    """Get teams

     For regular users only returns open teams. Users with the \"manage_system\" permission will return
    teams regardless of type. The result is based on query string parameters - page and per_page.
    ##### Permissions
    Must be authenticated. \"manage_system\" permission is required to show all teams.

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        include_total_count (Union[Unset, None, bool]):
        exclude_policy_constrained (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Team]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            include_total_count=include_total_count,
            exclude_policy_constrained=exclude_policy_constrained,
        )
    ).parsed
