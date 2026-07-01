from core.application.registry import DEVICE_REGISTRY
from core.devices import DEVICE_BUILDER_REGISTRY
from core.devices.profile import DeviceProfile
from core.infrastructure.config.config import DeviceConfig
from core.protocols import PROTOCOL_REGISTRY


class DeviceProfileFactory:

    @staticmethod
    def register(device: DeviceConfig)->None:
        DEVICE_REGISTRY[device.device_ip] = DeviceProfile(
            device_ip=device.device_ip,
            protocol= PROTOCOL_REGISTRY.get(device.protocol),
            builder=DEVICE_BUILDER_REGISTRY.get(device.device_name)
            )

