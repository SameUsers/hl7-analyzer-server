from datetime import datetime


def get_current_day() -> int:
    """
    Возвращает текущий день месяца.
    """
    return datetime.now().day


def get_current_month() -> int:
    """
    Возвращает текущий месяц.
    """
    return datetime.now().month


def get_current_year() -> int:
    """
    Возвращает текущий год.
    """
    return datetime.now().year


def get_current_second() -> int:
    """
    Возвращает текущую секунду.
    """
    return datetime.now().second
