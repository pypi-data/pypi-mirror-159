from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.group import Group
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_id: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    filter_allow_reference: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/teams/{team_id}/groups".format(client.base_url, team_id=team_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["per_page"] = per_page

    params["filter_allow_reference"] = filter_allow_reference

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[Group]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Group.from_dict(response_200_item_data)

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
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[Group]]]:
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
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    filter_allow_reference: Union[Unset, None, bool] = False,
) -> Response[Union[Any, List[Group]]]:
    """Get team groups

     Retrieve the list of groups associated with a given team.

    __Minimum server version__: 5.11

    Args:
        team_id (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        filter_allow_reference (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Group]]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        page=page,
        per_page=per_page,
        filter_allow_reference=filter_allow_reference,
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
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    filter_allow_reference: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, List[Group]]]:
    """Get team groups

     Retrieve the list of groups associated with a given team.

    __Minimum server version__: 5.11

    Args:
        team_id (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        filter_allow_reference (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Group]]]
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        page=page,
        per_page=per_page,
        filter_allow_reference=filter_allow_reference,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    filter_allow_reference: Union[Unset, None, bool] = False,
) -> Response[Union[Any, List[Group]]]:
    """Get team groups

     Retrieve the list of groups associated with a given team.

    __Minimum server version__: 5.11

    Args:
        team_id (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        filter_allow_reference (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Group]]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        page=page,
        per_page=per_page,
        filter_allow_reference=filter_allow_reference,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    team_id: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    filter_allow_reference: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, List[Group]]]:
    """Get team groups

     Retrieve the list of groups associated with a given team.

    __Minimum server version__: 5.11

    Args:
        team_id (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        filter_allow_reference (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Group]]]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            page=page,
            per_page=per_page,
            filter_allow_reference=filter_allow_reference,
        )
    ).parsed
