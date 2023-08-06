from typing import Any, Dict

import httpx

from ...client import Client
from ...models.publish_user_typing_json_body import PublishUserTypingJsonBody
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
    json_body: PublishUserTypingJsonBody,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/typing".format(client.base_url, user_id=user_id)

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
    json_body: PublishUserTypingJsonBody,
) -> Response[Any]:
    """Publish a user typing websocket event.

     Notify users in the given channel via websocket that the given user is typing.
    __Minimum server version__: 5.26
    ##### Permissions
    Must have `manage_system` permission to publish for any user other than oneself.

    Args:
        user_id (str):
        json_body (PublishUserTypingJsonBody):

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
    json_body: PublishUserTypingJsonBody,
) -> Response[Any]:
    """Publish a user typing websocket event.

     Notify users in the given channel via websocket that the given user is typing.
    __Minimum server version__: 5.26
    ##### Permissions
    Must have `manage_system` permission to publish for any user other than oneself.

    Args:
        user_id (str):
        json_body (PublishUserTypingJsonBody):

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
