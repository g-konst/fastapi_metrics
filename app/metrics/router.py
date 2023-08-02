from typing import List

from fastapi import APIRouter

from app.exceptions import ServerException
from app.metrics.exceptions import AddMetricsException
from app.metrics.schemas import SMetrics, SMetricsInfo
from app.metrics.service import MetricsService

router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"],
)


@router.post("", status_code=201)
async def add_metrics(metrics: SMetrics) -> SMetrics:
    """
    This endpoint is used to add metrics to database
    in following format:
        {
            "serviceName": "Name of the service",
            "path": "Requested path, eg. /users/me",
            "responseTimeMs": "Response time in ms"
        }
    """
    if result := await MetricsService.add(**metrics.model_dump()):
        return result
    raise AddMetricsException


@router.get("/{service_name}")
async def get_metrics(service_name: str) -> List[SMetricsInfo]:
    """
    This endpoint fetch some statistic for requested service, grouped by path:
        [
            {
                "path": "/users/me",
                "average": "Average response time in ms",
                "min": "Minimal response time in ms",
                "max": "Max response time in ms",
                "p99": "99 percentile response time"
            },
            {
                "path": "/posts",
                ...
            }
        ]
    """
    try:
        return await MetricsService.get(service_name)
    except ConnectionError:
        raise ServerException
