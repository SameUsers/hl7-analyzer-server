from datetime import datetime
from pathlib import Path


def current_datetime() -> datetime:
    """
    Возвращает текущую дату и время.

    Returns:
        datetime: Текущий объект datetime

    Example:
        >>> now = current_datetime()
        >>> print(now)
        2026-06-30 14:45:23.123456
    """
    return datetime.now()


def build_analyze_filename(
    analyzer_type: str,
    dt: datetime | None = None,
) -> str:
    """
    Формирует имя файла для сохранения результата анализа.

    Имя файла строится по шаблону: YYYY-MM-DD-SS-{analyzer_type}

    Args:
        analyzer_type: Тип анализатора (например, "BAC", "OAK")
        dt: Дата и время для формирования имени.
            Если не указана - используется текущее время.

    Returns:
        str: Имя файла без расширения

    Example:
        >>> filename = build_analyze_filename("BAC")
        >>> print(filename)
        '2026-06-30-45-BAC'
    """
    dt = dt or current_datetime()
    return f"{dt:%Y-%m-%d-%S}-{analyzer_type}"


def build_analyze_directory(
    root: Path,
    analyzer_type: str,
    dt: datetime | None = None,
) -> Path:
    """
    Создает и возвращает путь к директории для сохранения результатов.

    Структура директории: {root}/{analyzer_type}/{YYYY-MM-DD}

    Args:
        root: Корневая директория для сохранения
        analyzer_type: Тип анализатора
        dt: Дата для формирования пути.
            Если не указана - используется текущая дата.

    Returns:
        Path: Путь к созданной директории

    Raises:
        OSError: Если не удалось создать директорию

    Example:
        >>> root = Path("./Analyze")
        >>> directory = build_analyze_directory(root, "BAC")
        >>> print(directory)
        'Analyze/BAC/2026-6-30'
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

    Args:
        root: Корневая директория для сохранения
        analyzer_type: Тип анализатора
        extension: Расширение файла (например, "json", "xml")
        dt: Дата и время для формирования пути.
            Если не указана - используется текущее время.

    Returns:
        Path: Полный путь к файлу

    Example:
        >>> root = Path("./Analyze")
        >>> path = build_analyze_path(root, "BAC", "json")
        >>> print(path)
        'Analyze/BAC/2026-6-30/2026-6-30-45-BAC.json'
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
