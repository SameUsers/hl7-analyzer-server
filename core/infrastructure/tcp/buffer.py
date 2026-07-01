from loguru import logger


class DefaultBuffer:
    """
    Буфер для временного хранения входящих данных.
    Реализует накопительный буфер с ограничением максимального размера.
    Поддерживает операции поиска, извлечения и очистки данных.
    Используется для накопления данных из TCP-потока перед выделением
    полных сообщений с помощью фреймера.
    """

    def __init__(self, max_size: int = 10 * 1024 * 1024) -> None:
        """
        Инициализация буфера.

        Args:
            max_size: Максимальный размер буфера в байтах.
                     По умолчанию: 10 МБ.
        """
        self._buffer = bytearray()
        self._max_size = max_size
        logger.debug("Created {} with max_size={} bytes", self, max_size)

    def append(self, chunk: bytes) -> None:
        """
        Добавляет данные в буфер.
        """
        if len(self._buffer) + len(chunk) > self._max_size:
            raise RuntimeError(
                f"Buffer overloaded! "
                f"Current size: {len(self._buffer)}, "
                f"Adding: {len(chunk)}, "
                f"Max size: {self._max_size}"
            )
        self._buffer.extend(chunk)
        logger.debug(
            "Appended {} bytes to buffer. Current size: {} bytes",
            len(chunk),
            len(self._buffer),
        )

    def find(self, target: bytes, start: int = 0) -> int:
        """
        Ищет последовательность байтов в буфере.
        """
        return self._buffer.find(target, start)

    def extract(self, start: int, end: int) -> bytes:
        """
        Извлекает фрагмент данных из буфера.
        """
        return bytes(self._buffer[start:end])

    def clear(self) -> None:
        """Полностью очищает буфер."""
        self._buffer.clear()
        logger.debug("Buffer cleared")

    def remove_until(self, end: int) -> None:
        """
        Удаляет данные из буфера до указанной позиции.
        Используется после извлечения сообщения для удаления
        обработанных данных.

        """
        if end > 0 and end <= len(self._buffer):
            del self._buffer[:end]
            logger.debug(
                "Removed {} bytes from buffer. Remaining: {} bytes",
                end,
                len(self._buffer),
            )
        elif end > len(self._buffer):
            logger.warning(
                "Attempted to remove {} bytes but buffer size is {}",
                end,
                len(self._buffer),
            )

    @property
    def buffer(self) -> bytearray:
        """
        Возвращает внутренний буфер.

        Returns:
            bytearray: Ссылка на внутренний буфер
        """
        return self._buffer

    def __len__(self) -> int:
        """
        Возвращает текущий размер буфера.

        Returns:
            int: Количество байт в буфере
        """
        return len(self._buffer)

    def __del__(self) -> None:
        """Деструктор для логирования удаления объекта."""
        logger.debug(
            "Deleted {} with final size: {} bytes",
            self,
            len(self._buffer),
        )
