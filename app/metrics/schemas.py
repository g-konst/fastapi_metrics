from pydantic import BaseModel, ConfigDict


class SMetrics(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    service_name: str
    path: str
    response_time_ms: int


class SMetricsInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    path: str
    average: float
    min: int
    max: int
    p99: float
