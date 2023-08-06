from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.patch_post_json_body import PatchPostJsonBody
from ...models.post import Post
from ...types import Response


def _get_kwargs(
    post_id: str,
    *,
    client: Client,
    json_body: PatchPostJsonBody,
) -> Dict[str, Any]:
    url = "{}/posts/{post_id}/patch".format(client.base_url, post_id=post_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Post]]:
    if response.status_code == 200:
        response_200 = Post.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Post]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    post_id: str,
    *,
    client: Client,
    json_body: PatchPostJsonBody,
) -> Response[Union[Any, Post]]:
    """Patch a post

     Partially update a post by providing only the fields you want to update. Omitted fields will not be
    updated. The fields that can be updated are defined in the request body, all other provided fields
    will be ignored.
    ##### Permissions
    Must have the `edit_post` permission.

    Args:
        post_id (str):
        json_body (PatchPostJsonBody):

    Returns:
        Response[Union[Any, Post]]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    post_id: str,
    *,
    client: Client,
    json_body: PatchPostJsonBody,
) -> Optional[Union[Any, Post]]:
    """Patch a post

     Partially update a post by providing only the fields you want to update. Omitted fields will not be
    updated. The fields that can be updated are defined in the request body, all other provided fields
    will be ignored.
    ##### Permissions
    Must have the `edit_post` permission.

    Args:
        post_id (str):
        json_body (PatchPostJsonBody):

    Returns:
        Response[Union[Any, Post]]
    """

    return sync_detailed(
        post_id=post_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    post_id: str,
    *,
    client: Client,
    json_body: PatchPostJsonBody,
) -> Response[Union[Any, Post]]:
    """Patch a post

     Partially update a post by providing only the fields you want to update. Omitted fields will not be
    updated. The fields that can be updated are defined in the request body, all other provided fields
    will be ignored.
    ##### Permissions
    Must have the `edit_post` permission.

    Args:
        post_id (str):
        json_body (PatchPostJsonBody):

    Returns:
        Response[Union[Any, Post]]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    post_id: str,
    *,
    client: Client,
    json_body: PatchPostJsonBody,
) -> Optional[Union[Any, Post]]:
    """Patch a post

     Partially update a post by providing only the fields you want to update. Omitted fields will not be
    updated. The fields that can be updated are defined in the request body, all other provided fields
    will be ignored.
    ##### Permissions
    Must have the `edit_post` permission.

    Args:
        post_id (str):
        json_body (PatchPostJsonBody):

    Returns:
        Response[Union[Any, Post]]
    """

    return (
        await asyncio_detailed(
            post_id=post_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
