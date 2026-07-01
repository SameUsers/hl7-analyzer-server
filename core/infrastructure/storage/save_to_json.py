import json
from pathlib import Path

from loguru import logger

from core.contracts.storage import StorageInterface
from core.schemas.analyze_result import AnalyzeResult
from core.shared.path import build_analyze_path


class SaveToJson(StorageInterface):
    """
    Хранилище для сохранения результатов анализа в JSON-файлы.
    Реализует сохранение результатов работы анализаторов в формате JSON.
    Использует паттерн Синглтон для обеспечения единого экземпляра
    хранилища во всем приложении.
    Файлы сохраняются в структурированную директорию:
        Analyze/
            └── {analyzer_type}/
                └── {year}-{month}-{day}/
                    └── {timestamp}-{analyzer_type}.json
    """

    _instance = None
    _initialized = False

    def __new__(cls):
        """
        Создает или возвращает существующий экземпляр синглтона.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(
        self,
        save_dir: Path | None = None,
    ) -> None:
        """
        Инициализация хранилища.
        """
        if self._initialized:
            return

        self._initialized = True
        super().__init__(save_dir)

        logger.debug("Created {} with save_dir={}", self, save_dir)

    async def save_analyze_result(
        self,
        message: AnalyzeResult,
    ) -> None:
        """
        Сохраняет результат анализа в JSON-файл.
        Строит путь для сохранения на основе типа анализатора и даты,
        создает необходимые директории и записывает данные в файл.
        """
        # Строим путь для сохранения
        save_path = build_analyze_path(
            root=self._save_dir,
            analyzer_type=message.result.analyze_type,
            extension="json",
        )

        # Создаем директорию, если её нет
        save_path.parent.mkdir(parents=True, exist_ok=True)

        # Записываем данные в файл
        with save_path.open("w", encoding="utf-8") as file:
            json.dump(
                self._model_to_dict(message),
                file,
                ensure_ascii=False,
                indent=2,
            )

        logger.debug(
            "Saved analyze result to: {}",
            save_path,
        )

    def __del__(self) -> None:
        """Деструктор для логирования удаления объекта."""
        logger.debug("Deleted {}", self)
