from dataclasses import dataclass

from core.contracts.framer import FramerInterface
from core.contracts.parser import ParserInterface
from core.infrastructure.tcp.buffer import DefaultBuffer


@dataclass(frozen=True, slots=True)
class ProtocolConfig:
    """
    Конфигурация протокола обмена данными.
    Определяет набор компонентов, необходимых для работы с конкретным
    протоколом передачи данных. Содержит классы для фрейминга, парсинга
    и буферизации данных.
    Используется в DeviceProfile для настройки обработчика под конкретный
    протокол (HL7, ASTM, MQTT и т.д.).
    """

    framer: type[FramerInterface]
    """Класс фреймера для выделения сообщений из потока данных."""

    parser: type[ParserInterface]
    """Класс парсера для преобразования текстовых сообщений."""

    buffer: type[DefaultBuffer]
    """Класс буфера для временного хранения входящих данных."""
