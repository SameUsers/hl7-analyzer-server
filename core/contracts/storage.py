from abc import ABC, abstractmethod
from pathlib import Path

from loguru import logger

from core.infrastructure.config.config import settings
from core.domain.analyze_result import AnalyzeResult


class StorageInterface(ABC):
    """
    Интерфейс хранилища для сохранения результатов анализа.
    Определяет базовый контракт для всех хранилищ, которые занимаются
    сохранением результатов работы анализаторов в различные форматы
    и места (файловая система, база данных, облачное хранилище и т.д.).
    Предоставляет общие методы для работы с путями и сериализацией,
    которые могут быть переиспользованы наследниками.
    """

    def __init__(self, save_dir: Path | None = None) -> None:
        """
        Инициализация хранилища.
        """
        self._save_dir = save_dir or Path(settings.storage.analyze_path)
        logger.debug(
            "Created {} with save_dir={}",
            self.__class__.__name__,
            save_dir,
        )

    def _model_to_dict(self, message: AnalyzeResult) -> dict:
        """
        Преобразует модель результата в словарь для JSON-сериализации.
        Использует by_alias=True для сохранения оригинальных названий полей
        (алиасов) вместо имен атрибутов.
        """
        return message.model_dump(by_alias=True)

    @abstractmethod
    async def save_analyze_result(self, message: AnalyzeResult) -> None:
        """
        Сохраняет результат анализа.
        Абстрактный метод, который должен быть реализован в наследниках.
        Определяет конкретный способ сохранения данных.
        """
        pass
