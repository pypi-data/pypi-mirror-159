from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.autocomplete_suggestion import AutocompleteSuggestion
from ...types import UNSET, Response


def _get_kwargs(
    team_id: str,
    *,
    client: Client,
    user_input: str,
) -> Dict[str, Any]:
    url = "{}/teams/{team_id}/commands/autocomplete_suggestions".format(client.base_url, team_id=team_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["user_input"] = user_input

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[AutocompleteSuggestion]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AutocompleteSuggestion.from_dict(response_200_item_data)

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[AutocompleteSuggestion]]]:
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
    user_input: str,
) -> Response[Union[Any, List[AutocompleteSuggestion]]]:
    """List commands' autocomplete data

     List commands' autocomplete data for the team.
    ##### Permissions
    `view_team` for the team.
    __Minimum server version__: 5.24

    Args:
        team_id (str):
        user_input (str):

    Returns:
        Response[Union[Any, List[AutocompleteSuggestion]]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        user_input=user_input,
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
    user_input: str,
) -> Optional[Union[Any, List[AutocompleteSuggestion]]]:
    """List commands' autocomplete data

     List commands' autocomplete data for the team.
    ##### Permissions
    `view_team` for the team.
    __Minimum server version__: 5.24

    Args:
        team_id (str):
        user_input (str):

    Returns:
        Response[Union[Any, List[AutocompleteSuggestion]]]
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        user_input=user_input,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    *,
    client: Client,
    user_input: str,
) -> Response[Union[Any, List[AutocompleteSuggestion]]]:
    """List commands' autocomplete data

     List commands' autocomplete data for the team.
    ##### Permissions
    `view_team` for the team.
    __Minimum server version__: 5.24

    Args:
        team_id (str):
        user_input (str):

    Returns:
        Response[Union[Any, List[AutocompleteSuggestion]]]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        client=client,
        user_input=user_input,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    team_id: str,
    *,
    client: Client,
    user_input: str,
) -> Optional[Union[Any, List[AutocompleteSuggestion]]]:
    """List commands' autocomplete data

     List commands' autocomplete data for the team.
    ##### Permissions
    `view_team` for the team.
    __Minimum server version__: 5.24

    Args:
        team_id (str):
        user_input (str):

    Returns:
        Response[Union[Any, List[AutocompleteSuggestion]]]
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            user_input=user_input,
        )
    ).parsed
