from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.send_warn_metric_ack_json_body import SendWarnMetricAckJsonBody
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    warn_metric_id: str,
    *,
    client: Client,
    json_body: SendWarnMetricAckJsonBody,
) -> Dict[str, Any]:
    url = "{}/warn_metrics/ack/{warn_metric_id}".format(client.base_url, warn_metric_id=warn_metric_id)

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
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, StatusOK]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    warn_metric_id: str,
    *,
    client: Client,
    json_body: SendWarnMetricAckJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Acknowledge a warning of a metric status

     Acknowledge a warning for the warn_metric_id metric crossing a threshold (or some
    similar condition being fulfilled) - attempts to send an ack email to
    acknowledge@mattermost.com and sets the \"ack\" status for all the warn metrics in the system.

    __Minimum server version__: 5.26

    ##### Permissions

    Must have `manage_system` permission.

    Args:
        warn_metric_id (str):
        json_body (SendWarnMetricAckJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        warn_metric_id=warn_metric_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    warn_metric_id: str,
    *,
    client: Client,
    json_body: SendWarnMetricAckJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Acknowledge a warning of a metric status

     Acknowledge a warning for the warn_metric_id metric crossing a threshold (or some
    similar condition being fulfilled) - attempts to send an ack email to
    acknowledge@mattermost.com and sets the \"ack\" status for all the warn metrics in the system.

    __Minimum server version__: 5.26

    ##### Permissions

    Must have `manage_system` permission.

    Args:
        warn_metric_id (str):
        json_body (SendWarnMetricAckJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        warn_metric_id=warn_metric_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    warn_metric_id: str,
    *,
    client: Client,
    json_body: SendWarnMetricAckJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Acknowledge a warning of a metric status

     Acknowledge a warning for the warn_metric_id metric crossing a threshold (or some
    similar condition being fulfilled) - attempts to send an ack email to
    acknowledge@mattermost.com and sets the \"ack\" status for all the warn metrics in the system.

    __Minimum server version__: 5.26

    ##### Permissions

    Must have `manage_system` permission.

    Args:
        warn_metric_id (str):
        json_body (SendWarnMetricAckJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        warn_metric_id=warn_metric_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    warn_metric_id: str,
    *,
    client: Client,
    json_body: SendWarnMetricAckJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Acknowledge a warning of a metric status

     Acknowledge a warning for the warn_metric_id metric crossing a threshold (or some
    similar condition being fulfilled) - attempts to send an ack email to
    acknowledge@mattermost.com and sets the \"ack\" status for all the warn metrics in the system.

    __Minimum server version__: 5.26

    ##### Permissions

    Must have `manage_system` permission.

    Args:
        warn_metric_id (str):
        json_body (SendWarnMetricAckJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            warn_metric_id=warn_metric_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
