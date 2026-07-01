from core.application.handlers.analyzer import AnalyzerHandler
from core.contracts.handler import HandlerInterface
from core.devices.profile import DeviceProfile


class HandlerFactory:

    @staticmethod
    def create_handler(config: DeviceProfile) -> HandlerInterface:
        protocol = config.protocol
        return AnalyzerHandler(
            builder=config.builder(),
            parser=protocol.parser(),
            framer=protocol.framer(),
            buffer=protocol.buffer())

handler_factory = HandlerFactory()
