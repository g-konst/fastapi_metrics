import uuid

from sqlalchemy import UUID, Column, Integer, String

from app.database import Base


class Metrics(Base):
    __tablename__ = "metrics"

    id = Column(UUID(), primary_key=True, default=uuid.uuid4)

    service_name = Column(String, nullable=False)
    path = Column(String, nullable=False)
    response_time_ms = Column(Integer, nullable=False)
