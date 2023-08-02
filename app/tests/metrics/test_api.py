import pytest
from httpx import AsyncClient

from app.metrics.schemas import SMetricsInfo


@pytest.mark.parametrize("service_name,metrics_count", [
    ("users", 2),
    ("blog", 1),
    ("news", 0),
])
async def test_get_metrics(
    service_name: str,
    metrics_count: int,
    ac: AsyncClient,
):
    response = await ac.get(f"/metrics/{service_name}")
    metrics = response.json()
    assert len(metrics) == metrics_count

    for field in SMetricsInfo.model_fields:
        for metric in metrics:
            assert field in metric
            assert metric[field]


@pytest.mark.parametrize("service_name,path,response_time_ms,status_code", [
    ("users", "/me", 12, 201),
    ("blog", "/wall", 10, 201),
    ("news", "/feed", "new", 422),
])
async def test_add_metrics(
    service_name: str,
    path: str,
    response_time_ms: int,
    status_code: int,
    ac: AsyncClient
):
    initial_response = await ac.get(f"/metrics/{service_name}")
    initial_metrics_count = len(initial_response.json())

    response = await ac.post("/metrics", json={
        "service_name": service_name,
        "path": path,
        "response_time_ms": response_time_ms,
    })
    assert response.status_code == status_code

    response = await ac.get(f"/metrics/{service_name}")
    metrics_count = len(initial_response.json())
    if response.status_code == 201:
        assert metrics_count == initial_metrics_count + 1
    else:
        assert metrics_count == initial_metrics_count
