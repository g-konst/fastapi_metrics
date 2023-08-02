import logging

from app.config import settings

logger = logging.getLogger("app")
logger.setLevel(logging.getLevelName(settings.LOG_LEVEL))
