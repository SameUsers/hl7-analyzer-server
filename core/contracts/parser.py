from abc import ABC, abstractmethod

from core.protocols.core.schema import ProtocolMessage


class ParserInterface(ABC):
    """
    Интерфейс парсера сообщений протокола.
    Определяет контракт для классов, которые преобразуют сырое текстовое
    сообщение в структурированное представление (ProtocolMessage).
    """

    @abstractmethod
    def process_message(self, message: str) -> ProtocolMessage:
        """
        Преобразует текстовое сообщение в структурированный формат.
        Выполняет разбор входящей строки согласно правилам протокола
        и возвращает объект ProtocolMessage, содержащий все сегменты
        и поля сообщения.
        """
        ...
