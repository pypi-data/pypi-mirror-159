from typing import Any, Dict, List, Optional

import httpx

from ...client import Client
from ...models.integrity_check_result import IntegrityCheckResult
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/integrity".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[IntegrityCheckResult]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IntegrityCheckResult.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[IntegrityCheckResult]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[List[IntegrityCheckResult]]:
    """Perform a database integrity check

     Performs a database integrity check.


    __Note__: This check may temporarily harm system performance.


    __Minimum server version__: 5.28.0


    __Local mode only__: This endpoint is only available through [local
    mode](https://docs.mattermost.com/administration/mmctl-cli-tool.html#local-mode).

    Returns:
        Response[List[IntegrityCheckResult]]
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
) -> Optional[List[IntegrityCheckResult]]:
    """Perform a database integrity check

     Performs a database integrity check.


    __Note__: This check may temporarily harm system performance.


    __Minimum server version__: 5.28.0


    __Local mode only__: This endpoint is only available through [local
    mode](https://docs.mattermost.com/administration/mmctl-cli-tool.html#local-mode).

    Returns:
        Response[List[IntegrityCheckResult]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[List[IntegrityCheckResult]]:
    """Perform a database integrity check

     Performs a database integrity check.


    __Note__: This check may temporarily harm system performance.


    __Minimum server version__: 5.28.0


    __Local mode only__: This endpoint is only available through [local
    mode](https://docs.mattermost.com/administration/mmctl-cli-tool.html#local-mode).

    Returns:
        Response[List[IntegrityCheckResult]]
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
) -> Optional[List[IntegrityCheckResult]]:
    """Perform a database integrity check

     Performs a database integrity check.


    __Note__: This check may temporarily harm system performance.


    __Minimum server version__: 5.28.0


    __Local mode only__: This endpoint is only available through [local
    mode](https://docs.mattermost.com/administration/mmctl-cli-tool.html#local-mode).

    Returns:
        Response[List[IntegrityCheckResult]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
