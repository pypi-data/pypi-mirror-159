from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.incoming_webhook import IncomingWebhook
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    team_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/hooks/incoming".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["per_page"] = per_page

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[IncomingWebhook]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IncomingWebhook.from_dict(response_200_item_data)

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[IncomingWebhook]]]:
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
    team_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, List[IncomingWebhook]]]:
    """List incoming webhooks

     Get a page of a list of incoming webhooks. Optionally filter for a specific team using query
    parameters.
    ##### Permissions
    `manage_webhooks` for the system or `manage_webhooks` for the specific team.

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        team_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, List[IncomingWebhook]]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
        team_id=team_id,
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
    team_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, List[IncomingWebhook]]]:
    """List incoming webhooks

     Get a page of a list of incoming webhooks. Optionally filter for a specific team using query
    parameters.
    ##### Permissions
    `manage_webhooks` for the system or `manage_webhooks` for the specific team.

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        team_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, List[IncomingWebhook]]]
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        team_id=team_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    team_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, List[IncomingWebhook]]]:
    """List incoming webhooks

     Get a page of a list of incoming webhooks. Optionally filter for a specific team using query
    parameters.
    ##### Permissions
    `manage_webhooks` for the system or `manage_webhooks` for the specific team.

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        team_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, List[IncomingWebhook]]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
        team_id=team_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    team_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, List[IncomingWebhook]]]:
    """List incoming webhooks

     Get a page of a list of incoming webhooks. Optionally filter for a specific team using query
    parameters.
    ##### Permissions
    `manage_webhooks` for the system or `manage_webhooks` for the specific team.

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        team_id (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, List[IncomingWebhook]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            team_id=team_id,
        )
    ).parsed
