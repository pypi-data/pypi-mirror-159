from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.view_channel_json_body import ViewChannelJsonBody
from ...models.view_channel_response_200 import ViewChannelResponse200
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
    json_body: ViewChannelJsonBody,
) -> Dict[str, Any]:
    url = "{}/channels/members/{user_id}/view".format(client.base_url, user_id=user_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ViewChannelResponse200]]:
    if response.status_code == 200:
        response_200 = ViewChannelResponse200.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ViewChannelResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: Client,
    json_body: ViewChannelJsonBody,
) -> Response[Union[Any, ViewChannelResponse200]]:
    """View channel

     Perform all the actions involved in viewing a channel. This includes marking channels as read,
    clearing push notifications, and updating the active channel.
    ##### Permissions
    Must be logged in as user or have `edit_other_users` permission.

    __Response only includes `last_viewed_at_times` in Mattermost server 4.3 and newer.__

    Args:
        user_id (str):
        json_body (ViewChannelJsonBody):

    Returns:
        Response[Union[Any, ViewChannelResponse200]]
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


def sync(
    user_id: str,
    *,
    client: Client,
    json_body: ViewChannelJsonBody,
) -> Optional[Union[Any, ViewChannelResponse200]]:
    """View channel

     Perform all the actions involved in viewing a channel. This includes marking channels as read,
    clearing push notifications, and updating the active channel.
    ##### Permissions
    Must be logged in as user or have `edit_other_users` permission.

    __Response only includes `last_viewed_at_times` in Mattermost server 4.3 and newer.__

    Args:
        user_id (str):
        json_body (ViewChannelJsonBody):

    Returns:
        Response[Union[Any, ViewChannelResponse200]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Client,
    json_body: ViewChannelJsonBody,
) -> Response[Union[Any, ViewChannelResponse200]]:
    """View channel

     Perform all the actions involved in viewing a channel. This includes marking channels as read,
    clearing push notifications, and updating the active channel.
    ##### Permissions
    Must be logged in as user or have `edit_other_users` permission.

    __Response only includes `last_viewed_at_times` in Mattermost server 4.3 and newer.__

    Args:
        user_id (str):
        json_body (ViewChannelJsonBody):

    Returns:
        Response[Union[Any, ViewChannelResponse200]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    *,
    client: Client,
    json_body: ViewChannelJsonBody,
) -> Optional[Union[Any, ViewChannelResponse200]]:
    """View channel

     Perform all the actions involved in viewing a channel. This includes marking channels as read,
    clearing push notifications, and updating the active channel.
    ##### Permissions
    Must be logged in as user or have `edit_other_users` permission.

    __Response only includes `last_viewed_at_times` in Mattermost server 4.3 and newer.__

    Args:
        user_id (str):
        json_body (ViewChannelJsonBody):

    Returns:
        Response[Union[Any, ViewChannelResponse200]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
