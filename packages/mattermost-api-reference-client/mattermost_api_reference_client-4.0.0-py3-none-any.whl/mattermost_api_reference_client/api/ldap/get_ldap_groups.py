from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.ldap_groups_paged import LDAPGroupsPaged
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Dict[str, Any]:
    url = "{}/ldap/groups".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["q"] = q

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[LDAPGroupsPaged]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LDAPGroupsPaged.from_dict(response_200_item_data)

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
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[LDAPGroupsPaged]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Response[Union[Any, List[LDAPGroupsPaged]]]:
    """Returns a list of LDAP groups

     ##### Permissions
    Must have `manage_system` permission.
    __Minimum server version__: 5.11

    Args:
        q (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Returns:
        Response[Union[Any, List[LDAPGroupsPaged]]]
    """

    kwargs = _get_kwargs(
        client=client,
        q=q,
        page=page,
        per_page=per_page,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Optional[Union[Any, List[LDAPGroupsPaged]]]:
    """Returns a list of LDAP groups

     ##### Permissions
    Must have `manage_system` permission.
    __Minimum server version__: 5.11

    Args:
        q (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Returns:
        Response[Union[Any, List[LDAPGroupsPaged]]]
    """

    return sync_detailed(
        client=client,
        q=q,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Response[Union[Any, List[LDAPGroupsPaged]]]:
    """Returns a list of LDAP groups

     ##### Permissions
    Must have `manage_system` permission.
    __Minimum server version__: 5.11

    Args:
        q (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Returns:
        Response[Union[Any, List[LDAPGroupsPaged]]]
    """

    kwargs = _get_kwargs(
        client=client,
        q=q,
        page=page,
        per_page=per_page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Optional[Union[Any, List[LDAPGroupsPaged]]]:
    """Returns a list of LDAP groups

     ##### Permissions
    Must have `manage_system` permission.
    __Minimum server version__: 5.11

    Args:
        q (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Returns:
        Response[Union[Any, List[LDAPGroupsPaged]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            page=page,
            per_page=per_page,
        )
    ).parsed
