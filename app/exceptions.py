from fastapi import HTTPException, status


class BaseException(HTTPException):
    status_code: int = 500
    detail: str = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class ServerException(BaseException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Server is not response"
