from sqlalchemy import func, insert, select
from sqlalchemy.exc import SQLAlchemyError

from app.database import async_session_maker
from app.logger import logger
from app.metrics.models import Metrics


class MetricsService:
    @classmethod
    async def get(cls, service_name: str):
        async with async_session_maker() as session:
            query = (
                select(
                    Metrics.path,
                    func.avg(Metrics.response_time_ms).label('average'),
                    func.min(Metrics.response_time_ms).label('min'),
                    func.max(Metrics.response_time_ms).label('max'),
                    func.percentile_cont(0.99).within_group(
                        Metrics.response_time_ms).label('p99'),
                )
                .where(Metrics.service_name == service_name)
                .group_by(Metrics.path)
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add(cls, **values):
        try:
            query = insert(Metrics).values(**values).returning(
                Metrics.id,
                Metrics.service_name,
                Metrics.path,
                Metrics.response_time_ms
            )
            async with async_session_maker() as session:
                result = await session.execute(query)
                await session.commit()
                return result.mappings().first()
        except Exception as e:
            if isinstance(e, SQLAlchemyError):
                msg = "Database error: Can't insert data into table"
            elif isinstance(e, Exception):
                msg = "Unknown error: Can't insert data into table"

            logger.error(
                msg, extra={"table": Metrics.__tablename__}, exc_info=True)
            return None
