from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    user_id: str,
    team_id: str,
    thread_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/teams/{team_id}/threads/{thread_id}".format(
        client.base_url, user_id=user_id, team_id=team_id, thread_id=thread_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
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
    team_id: str,
    thread_id: str,
    *,
    client: Client,
) -> Response[Any]:
    """Get a thread followed by the user

     Get a thread

    __Minimum server version__: 5.29

    ##### Permissions
    Must be logged in as the user or have `edit_other_users` permission.

    Args:
        user_id (str):
        team_id (str):
        thread_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        team_id=team_id,
        thread_id=thread_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    user_id: str,
    team_id: str,
    thread_id: str,
    *,
    client: Client,
) -> Response[Any]:
    """Get a thread followed by the user

     Get a thread

    __Minimum server version__: 5.29

    ##### Permissions
    Must be logged in as the user or have `edit_other_users` permission.

    Args:
        user_id (str):
        team_id (str):
        thread_id (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        team_id=team_id,
        thread_id=thread_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
