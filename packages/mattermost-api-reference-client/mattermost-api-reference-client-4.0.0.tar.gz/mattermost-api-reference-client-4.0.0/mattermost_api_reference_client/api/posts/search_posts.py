from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.post_list_with_search_matches import PostListWithSearchMatches
from ...models.search_posts_json_body import SearchPostsJsonBody
from ...types import Response


def _get_kwargs(
    team_id: str,
    *,
    client: Client,
    json_body: SearchPostsJsonBody,
) -> Dict[str, Any]:
    url = "{}/teams/{team_id}/posts/search".format(client.base_url, team_id=team_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, PostListWithSearchMatches]]:
    if response.status_code == 200:
        response_200 = PostListWithSearchMatches.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, PostListWithSearchMatches]]:
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
    json_body: SearchPostsJsonBody,
) -> Response[Union[Any, PostListWithSearchMatches]]:
    """Search for team posts

     Search posts in the team and from the provided terms string.
    ##### Permissions
    Must be authenticated and have the `view_team` permission.

    Args:
        team_id (str):
        json_body (SearchPostsJsonBody):

    Returns:
        Response[Union[Any, PostListWithSearchMatches]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        json_body=json_body,
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
    json_body: SearchPostsJsonBody,
) -> Optional[Union[Any, PostListWithSearchMatches]]:
    """Search for team posts

     Search posts in the team and from the provided terms string.
    ##### Permissions
    Must be authenticated and have the `view_team` permission.

    Args:
        team_id (str):
        json_body (SearchPostsJsonBody):

    Returns:
        Response[Union[Any, PostListWithSearchMatches]]
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    *,
    client: Client,
    json_body: SearchPostsJsonBody,
) -> Response[Union[Any, PostListWithSearchMatches]]:
    """Search for team posts

     Search posts in the team and from the provided terms string.
    ##### Permissions
    Must be authenticated and have the `view_team` permission.

    Args:
        team_id (str):
        json_body (SearchPostsJsonBody):

    Returns:
        Response[Union[Any, PostListWithSearchMatches]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    team_id: str,
    *,
    client: Client,
    json_body: SearchPostsJsonBody,
) -> Optional[Union[Any, PostListWithSearchMatches]]:
    """Search for team posts

     Search posts in the team and from the provided terms string.
    ##### Permissions
    Must be authenticated and have the `view_team` permission.

    Args:
        team_id (str):
        json_body (SearchPostsJsonBody):

    Returns:
        Response[Union[Any, PostListWithSearchMatches]]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
