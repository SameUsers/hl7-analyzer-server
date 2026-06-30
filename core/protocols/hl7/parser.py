from typing import Optional

from core.contracts.parser import ParserInterface
from core.protocols.hl7.segments.msh import MSH
from core.protocols.hl7.segments.obx import OBX
from core.protocols.hl7.segments.obr import OBR
from core.protocols.hl7.segments.pid import PID
from core.protocols.hl7.message import HL7Message
from loguru import logger


class Hl7ParserV1(ParserInterface):
    """
    Парсер HL7-сообщений (версия 1).

    Преобразует текстовое HL7-сообщение в структурированный объект HL7Message.
    Разбивает сообщение на сегменты, парсит каждый сегмент и собирает
    их в единую структуру.

    Особенности:
    - Поддерживает сегменты: MSH, PID, OBR, OBX
    - Игнорирует неизвестные сегменты
    - Работает как синглтон

    Attributes:
        _segment_map (dict): Словарь соответствия имен сегментов их классам
    """

    _instance = None
    _initialized = False

    def __new__(cls):
        """
        Создает или возвращает существующий экземпляр синглтона.

        Returns:
            Hl7ParserV1: Единственный экземпляр класса
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """Инициализация парсера."""
        if self._initialized:
            return

        self._initialized = True
        self._segment_map = {
            "MSH": MSH,
            "PID": PID,
            "OBR": OBR,
            "OBX": OBX,
        }

        logger.debug("Created {}", self)

    def _extract_rows(self, message: str) -> list[str]:
        """
        Разбивает сообщение на строки-сегменты.

        Args:
            message: Текстовое HL7-сообщение

        Returns:
            list[str]: Список сегментов-строк
        """
        return [row for row in message.replace("\r", "\n").split("\n") if row]

    def _extract_fields(self, row: str) -> list[str]:
        """
        Разбивает строку сегмента на поля.

        Args:
            row: Строка сегмента

        Returns:
            list[str]: Список полей сегмента
        """
        return row.split("|")

    def _build_segment(self, segment_name: str, values: list[str]) -> Optional[object]:
        """
        Создает объект сегмента из значений.

        Args:
            segment_name: Имя сегмента (например, "MSH", "PID")
            values: Список значений полей сегмента

        Returns:
            Optional[object]: Объект сегмента или None, если сегмент неизвестен
        """
        segment_cls = self._segment_map.get(segment_name)
        if segment_cls is None:
            logger.debug("Unknown segment: {}", segment_name)
            return None

        return segment_cls.from_values(values)

    def process_message(self, message: str) -> HL7Message:
        """
        Разбирает HL7-сообщение в структурированный объект.

        Args:
            message: Текстовое HL7-сообщение

        Returns:
            HL7Message: Структурированное представление сообщения

        Raises:
            ValueError: Если в сообщении отсутствует обязательный сегмент MSH

        Example:
            >>> parser = Hl7ParserV1()
            >>> msg = "MSH|^~\\\\&|...\\rOBX|1|NM|..."
            >>> parsed = parser.process_message(msg)
            >>> parsed.msh  # Сегмент MSH
        """
        rows = self._extract_rows(message)

        msh = None
        pid = None
        obr = None
        obx_list = []

        for row in rows:
            fields = self._extract_fields(row)
            if not fields:
                continue

            segment_name = fields[0]
            values = fields[1:]

            segment = self._build_segment(segment_name, values)
            if segment is None:
                continue

            if segment_name == "MSH":
                msh = segment
            elif segment_name == "PID":
                pid = segment
            elif segment_name == "OBR":
                obr = segment
            elif segment_name == "OBX":
                obx_list.append(segment)

        if msh is None:
            raise ValueError("HL7 message must contain MSH segment")

        logger.debug(
            "Parsed HL7 message: MSH={}, PID={}, OBR={}, OBX count={}",
            msh is not None,
            pid is not None,
            obr is not None,
            len(obx_list),
        )

        return HL7Message(
            msh=msh,
            pid=pid,
            obr=obr,
            obx=obx_list,
        )

    def __del__(self) -> None:
        """Деструктор для логирования удаления объекта."""
        logger.debug("Deleted {}", self)