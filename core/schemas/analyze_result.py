from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class AnalyzeResult[T](BaseModel):
    """
    Результат анализа с типизированными данными.

    Обобщенный контейнер для хранения результатов работы анализатора.
    Использует Generic для обеспечения типобезопасности при работе
    с различными схемами результатов.

    Type Parameters:
        T: Тип результата анализа, должен быть наследником BaseModel

    Attributes:
        analyzer_name: Название анализатора, выполнившего анализ
        result: Данные результата анализа (типизированный объект)

    Example:
        >>> from core.devices.accent_m320.schema import BACAccentM320Schema
        >>>
        >>> result_data = BACAccentM320Schema(
        ...     analyzer_type="BAC",
        ...     glucose="5.6",
        ...     cholesterol="4.2",
        ... )
        >>>
        >>> analyze_result = AnalyzeResult[BACAccentM320Schema](
        ...     analyzer_name="Accent M320",
        ...     result=result_data,
        ... )
        >>>
        >>> # Типизация сохраняется
        >>> glucose = analyze_result.result.glucose
        >>> print(glucose)
        '5.6'

    Примечание:
        Использование Generic позволяет статической типизации (mypy, PyCharm)
        корректно определять типы полей в зависимости от переданной схемы.
    """

    analyzer_name: str
    """Название анализатора (например, "Accent M320", "Vet 5160")."""

    result: T
    """Данные результата анализа в типизированном виде."""
