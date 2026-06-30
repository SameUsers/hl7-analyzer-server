from datetime import datetime


def get_current_day() -> int:
    """
    Возвращает текущий день месяца.

    Returns:
        int: Текущий день (1-31)

    Example:
        >>> day = get_current_day()
        >>> print(day)
        30
    """
    return datetime.now().day


def get_current_month() -> int:
    """
    Возвращает текущий месяц.

    Returns:
        int: Текущий месяц (1-12)

    Example:
        >>> month = get_current_month()
        >>> print(month)
        6
    """
    return datetime.now().month


def get_current_year() -> int:
    """
    Возвращает текущий год.

    Returns:
        int: Текущий год (например, 2026)

    Example:
        >>> year = get_current_year()
        >>> print(year)
        2026
    """
    return datetime.now().year


def get_current_second() -> int:
    """
    Возвращает текущую секунду.

    Используется для создания уникальных имен файлов с точностью до секунды.

    Returns:
        int: Текущая секунда (0-59)

    Example:
        >>> second = get_current_second()
        >>> print(second)
        45
    """
    return datetime.now().second
