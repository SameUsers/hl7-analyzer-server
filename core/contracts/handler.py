from abc import ABC, abstractmethod
from typing import Any

from loguru import logger

from core.contracts.storage import StorageInterface
from core.infrastructure.storage.save_to_json import SaveToJson
from core.schemas.analyze_result import AnalyzeResult


class HandlerInterface(ABC):
    """
    Интерфейс обработчика данных от анализатора.
    Определяет базовый контракт для всех обработчиков, которые
    принимают данные, обрабатывают их и сохраняют результаты.
    Реализует паттерн "Шаблонный метод" (Template Method):
    - on_data() - публичный метод, определяющий общий алгоритм
    - _on_data() - абстрактный метод, реализуемый наследниками
    """

    def __init__(self, storage: StorageInterface | None = None) -> None:
        """
        Инициализация обработчика.
        """
        self._storage = storage or SaveToJson()
        logger.debug(
            "Created {} with storage={}",
            self.__class__.__name__,
            self._storage.__class__.__name__,
        )

    async def process_storage(self, message: AnalyzeResult) -> Any:
        """
        Сохраняет результат анализа в хранилище.
        """
        logger.debug(
            "Saving analyze result for {}",
            message.analyzer_name,
        )
        return await self._storage.save_analyze_result(message=message)

    async def on_data(self, chunk: bytes) -> AnalyzeResult | None:
        """
        Обрабатывает входящий блок данных.
        Реализует общий алгоритм обработки:
        1. Вызывает абстрактный метод _on_data() для обработки данных
        2. Если результат получен - сохраняет его
        3. Возвращает результат
        """
        message = await self._on_data(chunk=chunk)

        if not message:
            return None

        await self.process_storage(message=message)
        logger.debug(
            "Successfully processed and saved message for {}",
            message.analyzer_name,
        )

        return message

    @abstractmethod
    async def _on_data(self, chunk: bytes) -> AnalyzeResult | None:
        """
        Абстрактный метод для обработки данных.
        Должен быть реализован в наследниках и содержать
        специфическую логику обработки данных.
        """
        pass
