from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    job_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/jobs/{job_id}/cancel".format(client.base_url, job_id=job_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, StatusOK]]:
    if response.status_code == 200:
        response_200 = StatusOK.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, StatusOK]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: Client,
) -> Response[Union[Any, StatusOK]]:
    """Cancel a job.

     Cancel a job.
    __Minimum server version: 4.1__
    ##### Permissions
    Must have `manage_jobs` permission.

    Args:
        job_id (str):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    job_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, StatusOK]]:
    """Cancel a job.

     Cancel a job.
    __Minimum server version: 4.1__
    ##### Permissions
    Must have `manage_jobs` permission.

    Args:
        job_id (str):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: Client,
) -> Response[Union[Any, StatusOK]]:
    """Cancel a job.

     Cancel a job.
    __Minimum server version: 4.1__
    ##### Permissions
    Must have `manage_jobs` permission.

    Args:
        job_id (str):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    job_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, StatusOK]]:
    """Cancel a job.

     Cancel a job.
    __Minimum server version: 4.1__
    ##### Permissions
    Must have `manage_jobs` permission.

    Args:
        job_id (str):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
        )
    ).parsed
