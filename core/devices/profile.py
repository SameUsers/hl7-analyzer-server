from dataclasses import dataclass

from core.contracts.builder import BuilderInterface
from core.protocols.config import ProtocolConfig


@dataclass(frozen=True, slots=True)
class DeviceProfile:
    """
    Профиль устройства анализатора.
    Содержит всю необходимую конфигурацию для подключения и работы
    с конкретным анализатором. Используется фабриками для создания
    обработчиков.
    """

    protocol: ProtocolConfig
    """Конфигурация протокола обмена данными."""

    builder: type[BuilderInterface]
    """Класс билдера для создания структурированного результата."""
