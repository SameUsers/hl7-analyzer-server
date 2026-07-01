from loguru import logger

from core.contracts.builder import BuilderInterface
from core.contracts.framer import FramerInterface
from core.contracts.handler import HandlerInterface
from core.contracts.parser import ParserInterface
from core.contracts.storage import StorageInterface
from core.infrastructure.tcp.buffer import DefaultBuffer
from core.domain.analyze_result import AnalyzeResult
from core.shared.decoder import decode_message


class AnalyzerHandler(HandlerInterface):
    """
    Обработчик данных от анализаторов.
    Реализует полный цикл обработки входящих данных:
    1. Накопление данных в буфере
    2. Извлечение сообщений с помощью фреймера
    3. Декодирование и парсинг сообщений
    4. Построение структурированного результата
    5. Сохранение результата (опционально) по умолчанию в JSON
    """

    def __init__(
        self,
        builder: BuilderInterface,
        buffer: DefaultBuffer,
        parser: ParserInterface,
        framer: FramerInterface,
        storage: StorageInterface | None = None,
    ) -> None:
        """
        Инициализация обработчика анализатора.
        """
        super().__init__(storage=storage)

        if not builder:
            raise RuntimeError("Builder must be implemented for any Analyzer")

        self._builder = builder
        self._buffer = buffer
        self._parser = parser
        self._framer = framer

        logger.debug("Created {} with builder={}", self, builder.__class__.__name__)

    async def _on_data(self, chunk: bytes) -> AnalyzeResult | None:
        """
        Обрабатывает входящий блок данных.
        Выполняет полный цикл обработки: добавляет данные в буфер,
        извлекает сообщение, парсит его и строит результат.
        """
        # Добавляем данные в буфер
        self.buffer.append(chunk=chunk)

        # Пытаемся извлечь полное сообщение
        msg_bytes = self.framer.extract_message(self.buffer)
        if not msg_bytes:
            return None

        # Декодируем и парсим сообщение
        msg_str = decode_message(msg_bytes)
        hl7_message = self.parser.process_message(msg_str)

        # Строим результат анализа
        analyze_result = self.builder.build_analyze(hl7_message)

        logger.debug(
            "Successfully processed message for {}",
            self.builder.__class__.__name__,
        )

        return analyze_result

    def __del__(self) -> None:
        """Деструктор для логирования удаления объекта."""
        logger.debug(
            "Deleting {} with builder={}", self, self.builder.__class__.__name__
        )

    @property
    def buffer(self) -> DefaultBuffer:
        """Возвращает буфер данных."""
        return self._buffer

    @property
    def parser(self) -> ParserInterface:
        """Возвращает парсер сообщений."""
        return self._parser

    @property
    def framer(self) -> FramerInterface:
        """Возвращает фреймер сообщений."""
        return self._framer

    @property
    def builder(self) -> BuilderInterface:
        """Возвращает билдер результатов."""
        return self._builder
