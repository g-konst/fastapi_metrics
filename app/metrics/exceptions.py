from fastapi import status

from app.exceptions import BaseException


class AddMetricsException(BaseException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Can't add metrics to database"
