from abc import ABC, abstractmethod

from core.protocols.schema import ProtocolMessage


class ParserInterface(ABC):
    """
    Интерфейс парсера сообщений протокола.

    Определяет контракт для классов, которые преобразуют сырое текстовое
    сообщение в структурированное представление (ProtocolMessage).

    Парсер отвечает за:
    - Разбор сообщения на составные части
    - Валидацию структуры сообщения
    - Преобразование в удобный для дальнейшей обработки формат

    Каждый конкретный парсер реализует логику разбора для
    определенного протокола (HL7, XML, JSON и т.д.).
    """

    @abstractmethod
    def process_message(self, message: str) -> ProtocolMessage:
        """
        Преобразует текстовое сообщение в структурированный формат.

        Выполняет разбор входящей строки согласно правилам протокола
        и возвращает объект ProtocolMessage, содержащий все сегменты
        и поля сообщения.

        Args:
            message: Строка с текстовым сообщением протокола

        Returns:
            ProtocolMessage: Структурированное представление сообщения

        Raises:
            ValueError: Если сообщение имеет некорректный формат
            ParseError: Если не удалось разобрать сообщение

        Example:
            >>> parser = Hl7Parser()
            >>> msg = "MSH|^~\\&|...|OBX|1|...|"
            >>> parsed = parser.process_message(msg)
            >>> parsed.segments[0]  # Доступ к сегментам
            ['MSH', '^~\\&', '...']
        """
        ...
