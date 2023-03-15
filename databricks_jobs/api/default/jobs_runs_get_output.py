from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.jobs_runs_get_output_response_200 import JobsRunsGetOutputResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    run_id: int,
) -> Dict[str, Any]:
    url = "{}/2.1/jobs/runs/get-output".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["run_id"] = run_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, Error, JobsRunsGetOutputResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JobsRunsGetOutputResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

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


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, Error, JobsRunsGetOutputResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    run_id: int,
) -> Response[Union[Any, Error, JobsRunsGetOutputResponse200]]:
    """Get the output for a single run

     Retrieve the output and metadata of a single task run. When a notebook task returns a value through
    the dbutils.notebook.exit() call, you can use this endpoint to retrieve that value. Azure Databricks
    restricts this API to return the first 5 MB of the output. To return a larger result, you can store
    job results in a cloud storage service.
    This endpoint validates that the run_id parameter is valid and returns an HTTP status code 400 if
    the run_id parameter is invalid.
    Runs are automatically removed after 60 days. If you to want to reference them beyond 60 days, you
    must save old run results before they expire. To export using the UI, see Export job run results. To
    export using the Jobs API, see Runs export.

    Args:
        run_id (int):  Example: 455644833.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, JobsRunsGetOutputResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        run_id=run_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    run_id: int,
) -> Optional[Union[Any, Error, JobsRunsGetOutputResponse200]]:
    """Get the output for a single run

     Retrieve the output and metadata of a single task run. When a notebook task returns a value through
    the dbutils.notebook.exit() call, you can use this endpoint to retrieve that value. Azure Databricks
    restricts this API to return the first 5 MB of the output. To return a larger result, you can store
    job results in a cloud storage service.
    This endpoint validates that the run_id parameter is valid and returns an HTTP status code 400 if
    the run_id parameter is invalid.
    Runs are automatically removed after 60 days. If you to want to reference them beyond 60 days, you
    must save old run results before they expire. To export using the UI, see Export job run results. To
    export using the Jobs API, see Runs export.

    Args:
        run_id (int):  Example: 455644833.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, JobsRunsGetOutputResponse200]]
    """

    return sync_detailed(
        client=client,
        run_id=run_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    run_id: int,
) -> Response[Union[Any, Error, JobsRunsGetOutputResponse200]]:
    """Get the output for a single run

     Retrieve the output and metadata of a single task run. When a notebook task returns a value through
    the dbutils.notebook.exit() call, you can use this endpoint to retrieve that value. Azure Databricks
    restricts this API to return the first 5 MB of the output. To return a larger result, you can store
    job results in a cloud storage service.
    This endpoint validates that the run_id parameter is valid and returns an HTTP status code 400 if
    the run_id parameter is invalid.
    Runs are automatically removed after 60 days. If you to want to reference them beyond 60 days, you
    must save old run results before they expire. To export using the UI, see Export job run results. To
    export using the Jobs API, see Runs export.

    Args:
        run_id (int):  Example: 455644833.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, JobsRunsGetOutputResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        run_id=run_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    run_id: int,
) -> Optional[Union[Any, Error, JobsRunsGetOutputResponse200]]:
    """Get the output for a single run

     Retrieve the output and metadata of a single task run. When a notebook task returns a value through
    the dbutils.notebook.exit() call, you can use this endpoint to retrieve that value. Azure Databricks
    restricts this API to return the first 5 MB of the output. To return a larger result, you can store
    job results in a cloud storage service.
    This endpoint validates that the run_id parameter is valid and returns an HTTP status code 400 if
    the run_id parameter is invalid.
    Runs are automatically removed after 60 days. If you to want to reference them beyond 60 days, you
    must save old run results before they expire. To export using the UI, see Export job run results. To
    export using the Jobs API, see Runs export.

    Args:
        run_id (int):  Example: 455644833.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, JobsRunsGetOutputResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            run_id=run_id,
        )
    ).parsed
