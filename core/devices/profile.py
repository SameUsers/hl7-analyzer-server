from dataclasses import dataclass

from core.contracts.builder import BuilderInterface
from core.devices.enums import DeviceTypeEnum
from core.protocols.core.config import ProtocolConfig


@dataclass(frozen=True, slots=True)
class DeviceProfile:
    """
    Профиль устройства анализатора.
    Содержит всю необходимую конфигурацию для подключения и работы
    с конкретным анализатором. Используется фабриками для создания
    обработчиков.
    """
    device_type: DeviceTypeEnum
    device_ip: str
    protocol: ProtocolConfig
    builder: type[BuilderInterface]
