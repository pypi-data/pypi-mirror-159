from typing import Any, Dict

import httpx

from ...client import Client
from ...models.remove_recent_custom_status_json_body import RemoveRecentCustomStatusJsonBody
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
    json_body: RemoveRecentCustomStatusJsonBody,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/status/custom/recent".format(client.base_url, user_id=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: RemoveRecentCustomStatusJsonBody,
) -> Response[Any]:
    """Delete user's recent custom status

     Deletes a user's recent custom status by removing the specific status from the recentCustomStatuses
    in the user's props and updates the user.
    ##### Permissions
    Must be logged in as the user whose recent custom status is being deleted.

    Args:
        user_id (str):
        json_body (RemoveRecentCustomStatusJsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
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
    json_body: RemoveRecentCustomStatusJsonBody,
) -> Response[Any]:
    """Delete user's recent custom status

     Deletes a user's recent custom status by removing the specific status from the recentCustomStatuses
    in the user's props and updates the user.
    ##### Permissions
    Must be logged in as the user whose recent custom status is being deleted.

    Args:
        user_id (str):
        json_body (RemoveRecentCustomStatusJsonBody):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
