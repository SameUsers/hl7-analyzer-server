from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class AnalyzeResult[T](BaseModel):
    """
    Результат анализа с типизированными данными.
    Обобщенный контейнер для хранения результатов работы анализатора.
    Использует Generic для обеспечения типобезопасности при работе
    с различными схемами результатов.
    """

    analyzer_name: str
    """Название анализатора (например, "Accent M320", "Vet 5160")."""

    result: T
    """Данные результата анализа в типизированном виде."""
