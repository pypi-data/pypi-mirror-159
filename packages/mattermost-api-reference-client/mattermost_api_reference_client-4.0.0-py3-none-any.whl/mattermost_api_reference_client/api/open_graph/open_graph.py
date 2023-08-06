from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.open_graph import OpenGraph
from ...models.open_graph_json_body import OpenGraphJsonBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: OpenGraphJsonBody,
) -> Dict[str, Any]:
    url = "{}/opengraph".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, OpenGraph]]:
    if response.status_code == 200:
        response_200 = OpenGraph.from_dict(response.json())

        return response_200
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, OpenGraph]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: OpenGraphJsonBody,
) -> Response[Union[Any, OpenGraph]]:
    """Get open graph metadata for url

     Get Open Graph Metadata for a specif URL. Use the Open Graph protocol to get some generic metadata
    about a URL. Used for creating link previews.

    __Minimum server version__: 3.10

    ##### Permissions
    No permission required but must be logged in.

    Args:
        json_body (OpenGraphJsonBody):

    Returns:
        Response[Union[Any, OpenGraph]]
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
    json_body: OpenGraphJsonBody,
) -> Optional[Union[Any, OpenGraph]]:
    """Get open graph metadata for url

     Get Open Graph Metadata for a specif URL. Use the Open Graph protocol to get some generic metadata
    about a URL. Used for creating link previews.

    __Minimum server version__: 3.10

    ##### Permissions
    No permission required but must be logged in.

    Args:
        json_body (OpenGraphJsonBody):

    Returns:
        Response[Union[Any, OpenGraph]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: OpenGraphJsonBody,
) -> Response[Union[Any, OpenGraph]]:
    """Get open graph metadata for url

     Get Open Graph Metadata for a specif URL. Use the Open Graph protocol to get some generic metadata
    about a URL. Used for creating link previews.

    __Minimum server version__: 3.10

    ##### Permissions
    No permission required but must be logged in.

    Args:
        json_body (OpenGraphJsonBody):

    Returns:
        Response[Union[Any, OpenGraph]]
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
    json_body: OpenGraphJsonBody,
) -> Optional[Union[Any, OpenGraph]]:
    """Get open graph metadata for url

     Get Open Graph Metadata for a specif URL. Use the Open Graph protocol to get some generic metadata
    about a URL. Used for creating link previews.

    __Minimum server version__: 3.10

    ##### Permissions
    No permission required but must be logged in.

    Args:
        json_body (OpenGraphJsonBody):

    Returns:
        Response[Union[Any, OpenGraph]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
