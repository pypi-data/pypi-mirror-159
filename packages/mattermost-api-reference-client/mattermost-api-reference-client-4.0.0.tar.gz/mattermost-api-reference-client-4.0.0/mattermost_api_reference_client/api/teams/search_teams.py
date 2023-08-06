from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.search_teams_json_body import SearchTeamsJsonBody
from ...models.search_teams_response_200 import SearchTeamsResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: SearchTeamsJsonBody,
) -> Dict[str, Any]:
    url = "{}/teams/search".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, SearchTeamsResponse200]]:
    if response.status_code == 200:
        response_200 = SearchTeamsResponse200.from_dict(response.json())

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
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, SearchTeamsResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SearchTeamsJsonBody,
) -> Response[Union[Any, SearchTeamsResponse200]]:
    """Search teams

     Search teams based on search term and options provided in the request body.

    ##### Permissions
    Logged in user only shows open teams
    Logged in user with \"manage_system\" permission shows all teams

    Args:
        json_body (SearchTeamsJsonBody):

    Returns:
        Response[Union[Any, SearchTeamsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: SearchTeamsJsonBody,
) -> Optional[Union[Any, SearchTeamsResponse200]]:
    """Search teams

     Search teams based on search term and options provided in the request body.

    ##### Permissions
    Logged in user only shows open teams
    Logged in user with \"manage_system\" permission shows all teams

    Args:
        json_body (SearchTeamsJsonBody):

    Returns:
        Response[Union[Any, SearchTeamsResponse200]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SearchTeamsJsonBody,
) -> Response[Union[Any, SearchTeamsResponse200]]:
    """Search teams

     Search teams based on search term and options provided in the request body.

    ##### Permissions
    Logged in user only shows open teams
    Logged in user with \"manage_system\" permission shows all teams

    Args:
        json_body (SearchTeamsJsonBody):

    Returns:
        Response[Union[Any, SearchTeamsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: SearchTeamsJsonBody,
) -> Optional[Union[Any, SearchTeamsResponse200]]:
    """Search teams

     Search teams based on search term and options provided in the request body.

    ##### Permissions
    Logged in user only shows open teams
    Logged in user with \"manage_system\" permission shows all teams

    Args:
        json_body (SearchTeamsJsonBody):

    Returns:
        Response[Union[Any, SearchTeamsResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
