import asyncio

from core.infrastructure.config.config import settings
from core.infrastructure.tcp.server import TcpServer
from core.boot.device_registry import registry_device


async def main() -> None:
    devices_configs = settings.devices
    for device in devices_configs:
        registry_device.register(device=device)
    
    print(registry_device._device_registry)

    server = TcpServer(
        port=settings.server.port,
        host=settings.server.host,
        read_size=settings.server.read_size,
    )
    await server.initialize()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())
