from core.contracts.framer import FramerInterface
from core.infrastructure.tcp.buffer import DefaultBuffer
from loguru import logger


class Hl7FramerV1(FramerInterface):
    """
    Фреймер для выделения HL7-сообщений из потока данных (версия 1).

    Реализует извлечение сообщений формата HL7 из байтового потока.
    Использует стандартные маркеры HL7:
        - START_BLOCK: 0x0B (VT - Vertical Tab)
        - END_BLOCK:   0x1C 0x0D (FS + CR)

    Работает как синглтон для предотвращения множественных экземпляров.

    Attributes:
        START_BLOCK (bytes): Маркер начала сообщения (0x0B)
        END_BLOCK (bytes): Маркер конца сообщения (0x1C 0x0D)
        _initialized (bool): Флаг инициализации синглтона
    """

    _instance = None
    _initialized = False

    START_BLOCK = b"\x0b"
    """Маркер начала HL7-сообщения (VT - Vertical Tab)."""

    END_BLOCK = b"\x1c\x0d"
    """Маркер конца HL7-сообщения (FS + CR)."""

    def __new__(cls):
        """
        Создает или возвращает существующий экземпляр синглтона.

        Returns:
            Hl7FramerV1: Единственный экземпляр класса
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """Инициализация фреймера."""
        if self._initialized:
            return
        self._initialized = True
        logger.debug("Created {}", self)

    def extract_message(self, buffer: DefaultBuffer) -> bytes | None:
        """
        Извлекает полное HL7-сообщение из буфера.

        Ищет маркеры начала и конца сообщения. Если оба найдены,
        извлекает сообщение без маркеров и удаляет его из буфера.

        Args:
            buffer: Буфер с накопленными данными

        Returns:
            bytes | None: Извлеченное сообщение или None,
                         если сообщение не полное

        Example:
            >>> framer = Hl7FramerV1()
            >>> buffer = DefaultBuffer()
            >>> buffer.append(b"\\x0bMSH|...\\x1c\\x0d")
            >>> message = framer.extract_message(buffer)
            >>> message
            b'MSH|...'
        """
        # Ищем маркеры начала и конца
        start = buffer.find(self.START_BLOCK)
        end = buffer.find(self.END_BLOCK)

        # Если маркеры не найдены - сообщение не полное
        if start == -1 or end == -1:
            return None

        # Извлекаем сообщение без маркеров
        message = buffer.extract(
            start + len(self.START_BLOCK),
            end,
        )

        # Удаляем из буфера обработанные данные (включая маркеры)
        buffer.remove_until(end + len(self.END_BLOCK))

        logger.debug(
            "Extracted HL7 message of {} bytes from buffer",
            len(message),
        )

        return message

    def __del__(self) -> None:
        """Деструктор для логирования удаления объекта."""
        logger.debug("Deleted {}", self)