from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.notice import Notice
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_id: str,
    *,
    client: Client,
    client_version: str,
    locale: Union[Unset, None, str] = UNSET,
    client: str,
) -> Dict[str, Any]:
    url = "{}/system/notices/{teamId}".format(client.base_url, teamId=team_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["clientVersion"] = client_version

    params["locale"] = locale

    params["client"] = client

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[Notice]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Notice.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[Notice]]]:
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
    client_version: str,
    locale: Union[Unset, None, str] = UNSET,
    client: str,
) -> Response[Union[Any, List[Notice]]]:
    """Get notices for logged in user in specified team

     Will return appropriate product notices for current user in the team specified by teamId parameter.
    __Minimum server version__: 5.26
    ##### Permissions
    Must be logged in.

    Args:
        team_id (str):
        client_version (str):
        locale (Union[Unset, None, str]):
        client (str):

    Returns:
        Response[Union[Any, List[Notice]]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        client_version=client_version,
        locale=locale,
        client=client,
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
    client_version: str,
    locale: Union[Unset, None, str] = UNSET,
    client: str,
) -> Optional[Union[Any, List[Notice]]]:
    """Get notices for logged in user in specified team

     Will return appropriate product notices for current user in the team specified by teamId parameter.
    __Minimum server version__: 5.26
    ##### Permissions
    Must be logged in.

    Args:
        team_id (str):
        client_version (str):
        locale (Union[Unset, None, str]):
        client (str):

    Returns:
        Response[Union[Any, List[Notice]]]
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        client_version=client_version,
        locale=locale,
        client=client,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    *,
    client: Client,
    client_version: str,
    locale: Union[Unset, None, str] = UNSET,
    client: str,
) -> Response[Union[Any, List[Notice]]]:
    """Get notices for logged in user in specified team

     Will return appropriate product notices for current user in the team specified by teamId parameter.
    __Minimum server version__: 5.26
    ##### Permissions
    Must be logged in.

    Args:
        team_id (str):
        client_version (str):
        locale (Union[Unset, None, str]):
        client (str):

    Returns:
        Response[Union[Any, List[Notice]]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        client_version=client_version,
        locale=locale,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    team_id: str,
    *,
    client: Client,
    client_version: str,
    locale: Union[Unset, None, str] = UNSET,
    client: str,
) -> Optional[Union[Any, List[Notice]]]:
    """Get notices for logged in user in specified team

     Will return appropriate product notices for current user in the team specified by teamId parameter.
    __Minimum server version__: 5.26
    ##### Permissions
    Must be logged in.

    Args:
        team_id (str):
        client_version (str):
        locale (Union[Unset, None, str]):
        client (str):

    Returns:
        Response[Union[Any, List[Notice]]]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            client_version=client_version,
            locale=locale,
            client=client,
        )
    ).parsed
