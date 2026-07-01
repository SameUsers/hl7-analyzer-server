from core.devices.core.profile import DeviceProfile
from core.devices.core.registry import DEVICE_BUILDER_REGISTRY
from core.infrastructure.config.config import DeviceConfig
from core.protocols.core.registry import PROTOCOL_REGISTRY


class DeviceRegistry:
    def __init__(self)->None:
        self._device_registry: dict[str, DeviceProfile] = {}

    def register(self, device: DeviceConfig)->None:
        self._device_registry[device.device_ip] = DeviceProfile(
            device_ip=device.device_ip,
            protocol= PROTOCOL_REGISTRY.get(device.protocol),
            builder=DEVICE_BUILDER_REGISTRY.get(device.device_name)
            )

    def get_device(self, host: str)->DeviceProfile:
        device = self._device_registry.get(host)
        if device is None:
            raise RuntimeError(
            f"Unknown analyzer for host: {host}. "
            f"Available hosts: {list(self._device_registry.keys())}")
        return device


registry_device = DeviceRegistry()
