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

    Attributes:
        protocol: Конфигурация протокола обмена (HL7, ASTM и т.д.)
        builder: Класс билдера для парсинга данных анализатора

    Example:
        >>> profile = DeviceProfile(
        ...     protocol=HL7_V1,
        ...     builder=Accent320Builder,
        ... )
        >>> handler = ComponentFactory.create_handler(profile)
    """

    protocol: ProtocolConfig
    """Конфигурация протокола обмена данными."""

    builder: type[BuilderInterface]
    """Класс билдера для создания структурированного результата."""