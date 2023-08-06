from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    name: Union[Unset, None, str] = "standard",
    team_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/analytics/old".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["name"] = name

    params["team_id"] = team_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    name: Union[Unset, None, str] = "standard",
    team_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get analytics

     Get some analytics data about the system. This endpoint uses the old format, the `/analytics` route
    is reserved for the new format when it gets implemented.

    The returned JSON changes based on the `name` query parameter but is always key/value pairs.

    __Minimum server version__: 4.0

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        name (Union[Unset, None, str]):  Default: 'standard'.
        team_id (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        team_id=team_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    name: Union[Unset, None, str] = "standard",
    team_id: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get analytics

     Get some analytics data about the system. This endpoint uses the old format, the `/analytics` route
    is reserved for the new format when it gets implemented.

    The returned JSON changes based on the `name` query parameter but is always key/value pairs.

    __Minimum server version__: 4.0

    ##### Permissions
    Must have `manage_system` permission.

    Args:
        name (Union[Unset, None, str]):  Default: 'standard'.
        team_id (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        team_id=team_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
