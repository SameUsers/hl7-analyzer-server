import asyncio

from loguru import logger

from core.application.factories.component_factory import handler_factory
from core.application.factories.device_registry import registry_device
from core.infrastructure.tcp.session import TCPSession


class TcpServer:
    """
    TCP-сервер для приема и обработки сообщений от анализаторов.
    Сервер принимает входящие TCP-подключения, создает для каждого клиента
    сессию и обрабатывает получаемые данные с помощью соответствующего
    обработчика, определяемого по IP-адресу клиента.
    """

    def __init__(self, host: str, port: int, read_size: int = 4096,) -> None:
        """
        Инициализация TCP-сервера.
        """
        self._port = port
        self._host = host
        self._read_size = read_size
        self._server: asyncio.Server | None = None
        logger.debug(
            "Created {} with host={}, port={}, read_size={}",
            self,
            host,
            port,
            read_size,
        )

    async def _handle_connection(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ) -> None:
        """
        Обрабатывает входящее клиентское подключение.
        Создает сессию для клиента, определяет обработчик по IP-адресу
        и обрабатывает все входящие данные до закрытия соединения.
        (TODO: заменить на конкретные типы исключений)
        """
        client_host, client_port = writer.get_extra_info("peername")

        # Создаем обработчик для конкретного клиента
        session_handler = handler_factory.create_handler(registry_device.get_device(client_host))
        session = TCPSession(
            client_host=client_host,
            client_port=client_port,
            handler=session_handler,
        )

        while True:
            chunk = await reader.read(self._read_size)
            if not chunk:
                break
            try:
                await session.handle(chunk=chunk)
            except Exception as e:
                # TODO: Заменить на конкретную обработку ошибок
                logger.error(
                    "Error processing data from {}:{} - {}",
                    client_host,
                    client_port,
                    e,
                )
                raise e from e

    async def initialize(self) -> None:
        """
        Инициализирует TCP-сервер.
        Создает ASGI-сервер и привязывает его к указанным хосту и порту.
        """
        if self._server is not None:
            raise RuntimeError(
                f"Server already initialized on {self._host}:{self._port}"
            )

        self._server = await asyncio.start_server(
            self._handle_connection,
            port=self.port,
            host=self.host,
        )
        logger.info("Server initialized on {}:{}", self._host, self._port)

    async def run(self) -> None:
        """
        Запускает сервер и начинает обработку входящих соединений.
        Блокирует выполнение до остановки сервера.
        """
        if self._server is None:
            raise RuntimeError("Server is not initialized, call initialize() first")

        logger.info("Server started on {}:{}", self._host, self._port)
        async with self._server:
            await self._server.serve_forever()

    async def stop(self) -> None:
        """
        Останавливает сервер и закрывает все активные соединения.
        """
        if self._server is None:
            logger.warning("Server already stopped or not initialized")
            return

        logger.info("Stopping server on {}:{}", self._host, self._port)
        self._server.close()
        await self._server.wait_closed()
        self._server = None
        logger.info("Server stopped")

    @property
    def port(self) -> int:
        """Возвращает порт, на котором запущен сервер."""
        return self._port

    @property
    def host(self) -> str:
        """Возвращает хост, на котором запущен сервер."""
        return self._host

    @property
    def read_size(self) -> int:
        return self._read_size

    @property
    def server(self) -> asyncio.Server | None:
        """Возвращает объект ASGI-сервера или None, если сервер не запущен."""
        return self._server
