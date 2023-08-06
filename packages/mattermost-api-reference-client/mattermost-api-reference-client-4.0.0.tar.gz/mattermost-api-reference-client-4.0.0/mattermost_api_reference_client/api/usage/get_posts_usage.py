from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.posts_usage import PostsUsage
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/usage/posts".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, PostsUsage]]:
    if response.status_code == 200:
        response_200 = PostsUsage.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, PostsUsage]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, PostsUsage]]:
    """Get current usage of posts

     Retrieve rounded off total no. of posts for this instance. Example: returns 4000 instead of 4321
    ##### Permissions
    Must be authenticated.
    __Minimum server version__: 7.0

    Returns:
        Response[Union[Any, PostsUsage]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[Any, PostsUsage]]:
    """Get current usage of posts

     Retrieve rounded off total no. of posts for this instance. Example: returns 4000 instead of 4321
    ##### Permissions
    Must be authenticated.
    __Minimum server version__: 7.0

    Returns:
        Response[Union[Any, PostsUsage]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, PostsUsage]]:
    """Get current usage of posts

     Retrieve rounded off total no. of posts for this instance. Example: returns 4000 instead of 4321
    ##### Permissions
    Must be authenticated.
    __Minimum server version__: 7.0

    Returns:
        Response[Union[Any, PostsUsage]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[Any, PostsUsage]]:
    """Get current usage of posts

     Retrieve rounded off total no. of posts for this instance. Example: returns 4000 instead of 4321
    ##### Permissions
    Must be authenticated.
    __Minimum server version__: 7.0

    Returns:
        Response[Union[Any, PostsUsage]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
