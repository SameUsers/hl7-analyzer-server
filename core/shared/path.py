from datetime import datetime
from pathlib import Path


def current_datetime() -> datetime:
    """
    Возвращает текущую дату и время.
    """
    return datetime.now()


def build_analyze_filename(
    analyzer_type: str,
    dt: datetime | None = None,
) -> str:
    """
    Формирует имя файла для сохранения результата анализа.
    Имя файла строится по шаблону: YYYY-MM-DD-SS-{analyzer_type}
    """
    dt = dt or current_datetime()
    return f"{dt:%Y-%m-%d-%H:%M}-{analyzer_type}"


def build_analyze_directory(
    root: Path,
    analyzer_type: str,
    dt: datetime | None = None,
) -> Path:
    """
    Создает и возвращает путь к директории для сохранения результатов.
    Структура директории: {root}/{analyzer_type}/{YYYY-MM-DD}
    """
    dt = dt or current_datetime()
    directory = root / analyzer_type / f"{dt:%Y-%m-%d}"
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def build_analyze_path(
    root: Path,
    analyzer_type: str,
    extension: str,
    dt: datetime | None = None,
) -> Path:
    """
    Формирует полный путь к файлу для сохранения результата анализа.
    Объединяет директорию и имя файла с расширением.
    """
    dt = dt or current_datetime()

    directory = build_analyze_directory(
        root=root,
        analyzer_type=analyzer_type,
        dt=dt,
    )

    filename = build_analyze_filename(
        analyzer_type=analyzer_type,
        dt=dt,
    )

    return directory / f"{filename}.{extension}"
