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
    if result := await MetricsService.add(**metrics.model_dump()):
        return result
    raise AddMetricsException


@router.get("/{service_name}")
async def get_metrics(service_name: str) -> List[SMetricsInfo]:
    try:
        return await MetricsService.get(service_name)
    except ConnectionError:
        raise ServerException
