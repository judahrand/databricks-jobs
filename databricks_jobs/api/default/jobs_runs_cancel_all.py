from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.jobs_runs_cancel_all_json_body import JobsRunsCancelAllJsonBody
from ...models.jobs_runs_cancel_all_response_200 import JobsRunsCancelAllResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: JobsRunsCancelAllJsonBody,
) -> Dict[str, Any]:
    url = "{}/2.1/jobs/runs/cancel-all".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, JobsRunsCancelAllResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JobsRunsCancelAllResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, JobsRunsCancelAllResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: JobsRunsCancelAllJsonBody,
) -> Response[Union[Any, JobsRunsCancelAllResponse200]]:
    """Cancel all runs of a job

     Cancels all active runs of a job. The runs are canceled asynchronously, so it doesn't prevent new
    runs from being started.

    Args:
        json_body (JobsRunsCancelAllJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, JobsRunsCancelAllResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: JobsRunsCancelAllJsonBody,
) -> Optional[Union[Any, JobsRunsCancelAllResponse200]]:
    """Cancel all runs of a job

     Cancels all active runs of a job. The runs are canceled asynchronously, so it doesn't prevent new
    runs from being started.

    Args:
        json_body (JobsRunsCancelAllJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, JobsRunsCancelAllResponse200]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: JobsRunsCancelAllJsonBody,
) -> Response[Union[Any, JobsRunsCancelAllResponse200]]:
    """Cancel all runs of a job

     Cancels all active runs of a job. The runs are canceled asynchronously, so it doesn't prevent new
    runs from being started.

    Args:
        json_body (JobsRunsCancelAllJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, JobsRunsCancelAllResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: JobsRunsCancelAllJsonBody,
) -> Optional[Union[Any, JobsRunsCancelAllResponse200]]:
    """Cancel all runs of a job

     Cancels all active runs of a job. The runs are canceled asynchronously, so it doesn't prevent new
    runs from being started.

    Args:
        json_body (JobsRunsCancelAllJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, JobsRunsCancelAllResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
