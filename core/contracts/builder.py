from abc import ABC, abstractmethod

from core.schemas.analyze_result import AnalyzeResult
from core.protocols.schema import ProtocolMessage


class BuilderInterface(ABC):
    """
    Интерфейс билдера для создания структурированного результата анализа.

    Определяет контракт для классов, которые преобразуют сырые данные
    сообщения в структурированный объект результата анализа.

    Каждый конкретный билдер должен реализовывать логику парсинга
    и преобразования данных для конкретного типа анализатора.
    """

    @abstractmethod
    def build_analyze(self, message: ProtocolMessage) -> AnalyzeResult:
        """
        Строит структурированный результат анализа из сообщения.

        Преобразует входное сообщение (обычно разобранное на сегменты)
        в структурированный объект AnalyzeResult, содержащий все
        необходимые параметры и измерения.

        Args:
            message: Сообщение протокола, содержащее данные для анализа

        Returns:
            AnalyzeResult: Структурированный результат анализа

        Raises:
            ValueError: Если сообщение содержит некорректные данные
            ValidationError: Если данные не проходят валидацию схемы

        Example:
            >>> builder = Accent320AnalyzeBuilder()
            >>> result = builder.build_analyze(hl7_message)
            >>> print(result.analyzer_name)
            'Accent M320'
        """
        pass