from core.contracts.handler import HandlerInterface
from loguru import logger


class TCPSession:
    """
    TCP-сессия для обработки данных от одного клиента.

    Представляет собой логическое соединение с клиентом (анализатором).
    Инкапсулирует состояние сессии и делегирует обработку данных
    соответствующему обработчику.

    Attributes:
        _host (str): IP-адрес клиента
        _port (int): Порт клиента
        _handler (HandlerInterface): Обработчик данных для этого клиента
    """

    def __init__(
        self,
        client_host: str,
        client_port: int,
        handler: HandlerInterface,
    ) -> None:
        """
        Инициализация TCP-сессии.

        Args:
            client_host: IP-адрес клиента
            client_port: Порт клиента
            handler: Обработчик для управления данными от клиента
        """
        self._host = client_host
        self._port = client_port
        self._handler = handler

        logger.debug(
            "Created {} for {}:{} with handler={}",
            self,
            client_host,
            client_port,
            handler.__class__.__name__,
        )

    async def handle(self, chunk: bytes) -> None:
        """
        Обрабатывает входящий блок данных.

        Делегирует обработку данных хендлеру, который выполняет
        парсинг, валидацию и сохранение результатов.

        Args:
            chunk: Блок данных в виде байтов

        Raises:
            Exception: Пробрасывает исключения от хендлера
        """
        await self.handler.on_data(chunk=chunk)
        logger.debug(
            "Processed {} bytes from {}:{}",
            len(chunk),
            self._host,
            self._port,
        )

    @property
    def host(self) -> str:
        """Возвращает IP-адрес клиента."""
        return self._host

    @property
    def port(self) -> int:
        """Возвращает порт клиента."""
        return self._port

    @property
    def handler(self) -> HandlerInterface:
        """Возвращает обработчик данных сессии."""
        return self._handler

    def __del__(self) -> None:
        """Деструктор для логирования удаления объекта."""
        logger.debug(
            "Deleted {} for {}:{}",
            self,
            self._host,
            self._port,
        )