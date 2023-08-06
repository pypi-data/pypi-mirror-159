from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
    field_: Union[Unset, None, float] = UNSET,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/image".format(client.base_url, user_id=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["_"] = field_

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
    user_id: str,
    *,
    client: Client,
    field_: Union[Unset, None, float] = UNSET,
) -> Response[Any]:
    """Get user's profile image

     Get a user's profile image based on user_id string parameter.
    ##### Permissions
    Must be logged in.

    Args:
        user_id (str):
        field_ (Union[Unset, None, float]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        field_=field_,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    user_id: str,
    *,
    client: Client,
    field_: Union[Unset, None, float] = UNSET,
) -> Response[Any]:
    """Get user's profile image

     Get a user's profile image based on user_id string parameter.
    ##### Permissions
    Must be logged in.

    Args:
        user_id (str):
        field_ (Union[Unset, None, float]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        field_=field_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
