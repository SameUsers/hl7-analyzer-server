from core.devices.core.profile import DeviceProfile
from core.devices.core.registry import DEVICE_BUILDER_REGISTRY
from core.infrastructure.config.config import DeviceConfig
from core.protocols.core.registry import PROTOCOL_REGISTRY


class CreateDeviceProfile:

    @staticmethod
    def create_device_profile(device_config: DeviceConfig)->DeviceProfile:
        return DeviceProfile(
            device_ip=device_config.device_ip,
            protocol=PROTOCOL_REGISTRY.get(device_config.protocol),
            builder=DEVICE_BUILDER_REGISTRY.get(device_config.device_name)
        )
