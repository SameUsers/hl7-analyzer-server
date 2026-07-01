from core.devices.profile import DeviceProfile

DEVICE_REGISTRY: dict[str, DeviceProfile] = {}

def get_device(host: str)->DeviceProfile:
    device = DEVICE_REGISTRY.get(host)
    if device is None:
        raise RuntimeError(
        f"Unknown analyzer for host: {host}. "
        f"Available hosts: {list(DEVICE_REGISTRY.keys())}")
    return device
