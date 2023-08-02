from fastapi import FastAPI

from app.metrics.router import router as router_metrics

app = FastAPI(
    title="Metrics API",
    version="0.1.0",
)

app.include_router(router_metrics)
