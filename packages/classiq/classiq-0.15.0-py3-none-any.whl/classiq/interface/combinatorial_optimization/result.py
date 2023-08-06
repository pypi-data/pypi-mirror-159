from typing import List

from pydantic import BaseModel

from classiq.interface.status import Status


class AnglesResult(BaseModel):
    status: Status
    details: List[float]


class PyomoObjectResult(BaseModel):
    status: Status
    details: str
