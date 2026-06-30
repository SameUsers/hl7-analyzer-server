from abc import ABC, abstractmethod
from pathlib import Path

from core.schemas.analyze_result import AnalyzeResult
from loguru import logger


class StorageInterface(ABC):
    """
    Интерфейс хранилища для сохранения результатов анализа.

    Определяет базовый контракт для всех хранилищ, которые занимаются
    сохранением результатов работы анализаторов в различные форматы
    и места (файловая система, база данных, облачное хранилище и т.д.).

    Предоставляет общие методы для работы с путями и сериализацией,
    которые могут быть переиспользованы наследниками.

    Attributes:
        _save_dir (Path): Корневая директория для сохранения файлов
    """

    def __init__(self, save_dir: Path) -> None:
        """
        Инициализация хранилища.

        Args:
            save_dir: Путь к корневой директории для сохранения
        """
        self._save_dir = save_dir
        logger.debug(
            "Created {} with save_dir={}",
            self.__class__.__name__,
            save_dir,
        )

    def _model_to_json(self, message: AnalyzeResult) -> dict:
        """
        Преобразует модель результата в словарь для JSON-сериализации.

        Использует by_alias=True для сохранения оригинальных названий полей
        (алиасов) вместо имен атрибутов.

        Args:
            message: Результат анализа для преобразования

        Returns:
            dict: Словарь с данными результата

        Example:
            >>> storage = SaveToJson()
            >>> data = storage._model_to_json(analyze_result)
            >>> json.dump(data, file)
        """
        return message.model_dump(by_alias=True)

    @abstractmethod
    async def save_analyze_result(self, message: AnalyzeResult) -> None:
        """
        Сохраняет результат анализа.

        Абстрактный метод, который должен быть реализован в наследниках.
        Определяет конкретный способ сохранения данных.

        Args:
            message: Результат анализа для сохранения

        Raises:
            IOError: При ошибке записи в файл
            PermissionError: При недостатке прав доступа

        Example:
            >>> storage = SaveToJson()
            >>> await storage.save_analyze_result(result)
        """
        pass