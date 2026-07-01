from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class AnalyzeResult[T](BaseModel):
    analyzer_name: str
    result: T
