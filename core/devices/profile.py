from dataclasses import dataclass

from core.contracts.builder import BuilderInterface
from core.protocols.config import ProtocolConfig


@dataclass(frozen=True, slots=True)
class DeviceProfile:
    device_ip: str
    protocol: ProtocolConfig
    builder: type[BuilderInterface]
