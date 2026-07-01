import asyncio

from core.application.factories.device_registry import device_profile_factory
from core.infrastructure.config.config import settings
from core.infrastructure.tcp.server import TcpServer


async def main() -> None:
    devices_configs = settings.devices#Забрал девайся из ямла

    for device in devices_configs:
        device_profile_factory.register(device=device)#Заргеал

    server = TcpServer(
        port=settings.server.port,
        host=settings.server.host,
        read_size=settings.server.read_size,
    )
    await server.initialize()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())
