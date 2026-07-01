from abc import ABC, abstractmethod

from core.protocols.schema import ProtocolMessage
from core.domain.analyze_result import AnalyzeResult


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
        """
        ...
