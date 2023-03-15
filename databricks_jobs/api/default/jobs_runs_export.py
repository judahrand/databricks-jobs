from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.jobs_runs_export_response_200 import JobsRunsExportResponse200
from ...models.views_to_export import ViewsToExport
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    run_id: int,
    views_to_export: Union[Unset, None, ViewsToExport] = ViewsToExport.CODE,
) -> Dict[str, Any]:
    url = "{}/2.0/jobs/runs/export".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["run_id"] = run_id

    json_views_to_export: Union[Unset, None, str] = UNSET
    if not isinstance(views_to_export, Unset):
        json_views_to_export = views_to_export.value if views_to_export else None

    params["views_to_export"] = json_views_to_export

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, JobsRunsExportResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JobsRunsExportResponse200.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, JobsRunsExportResponse200]]:
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
    views_to_export: Union[Unset, None, ViewsToExport] = ViewsToExport.CODE,
) -> Response[Union[Any, JobsRunsExportResponse200]]:
    """Export and retrieve a job run

     Export and retrieve the job run task.

    Args:
        run_id (int):  Example: 455644833.
        views_to_export (Union[Unset, None, ViewsToExport]): * `CODE`: Code view of the notebook.
            * `DASHBOARDS`: All dashboard views of the notebook.
            * `ALL`: All views of the notebook. Default: ViewsToExport.CODE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, JobsRunsExportResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        run_id=run_id,
        views_to_export=views_to_export,
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
    views_to_export: Union[Unset, None, ViewsToExport] = ViewsToExport.CODE,
) -> Optional[Union[Any, JobsRunsExportResponse200]]:
    """Export and retrieve a job run

     Export and retrieve the job run task.

    Args:
        run_id (int):  Example: 455644833.
        views_to_export (Union[Unset, None, ViewsToExport]): * `CODE`: Code view of the notebook.
            * `DASHBOARDS`: All dashboard views of the notebook.
            * `ALL`: All views of the notebook. Default: ViewsToExport.CODE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, JobsRunsExportResponse200]]
    """

    return sync_detailed(
        client=client,
        run_id=run_id,
        views_to_export=views_to_export,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    run_id: int,
    views_to_export: Union[Unset, None, ViewsToExport] = ViewsToExport.CODE,
) -> Response[Union[Any, JobsRunsExportResponse200]]:
    """Export and retrieve a job run

     Export and retrieve the job run task.

    Args:
        run_id (int):  Example: 455644833.
        views_to_export (Union[Unset, None, ViewsToExport]): * `CODE`: Code view of the notebook.
            * `DASHBOARDS`: All dashboard views of the notebook.
            * `ALL`: All views of the notebook. Default: ViewsToExport.CODE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, JobsRunsExportResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        run_id=run_id,
        views_to_export=views_to_export,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    run_id: int,
    views_to_export: Union[Unset, None, ViewsToExport] = ViewsToExport.CODE,
) -> Optional[Union[Any, JobsRunsExportResponse200]]:
    """Export and retrieve a job run

     Export and retrieve the job run task.

    Args:
        run_id (int):  Example: 455644833.
        views_to_export (Union[Unset, None, ViewsToExport]): * `CODE`: Code view of the notebook.
            * `DASHBOARDS`: All dashboard views of the notebook.
            * `ALL`: All views of the notebook. Default: ViewsToExport.CODE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, JobsRunsExportResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            run_id=run_id,
            views_to_export=views_to_export,
        )
    ).parsed
