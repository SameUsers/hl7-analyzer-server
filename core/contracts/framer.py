from abc import ABC, abstractmethod

from core.infrastructure.tcp.buffer import DefaultBuffer


class FramerInterface(ABC):
    """
    Интерфейс фреймера для выделения сообщений из потока данных.

    Определяет контракт для классов, которые занимаются поиском
    и извлечением полных сообщений из буфера с данными.

    Фреймер должен знать структуру протокола (стартовые и конечные
    маркеры, длину сообщений и т.д.) и уметь определять момент,
    когда в буфере накопилось достаточно данных для извлечения
    целого сообщения.
    """

    @abstractmethod
    def extract_message(self, buffer: DefaultBuffer) -> bytes:
        """
        Извлекает полное сообщение из буфера.

        Ищет в буфере начало и конец сообщения согласно протоколу.
        Если полное сообщение найдено - извлекает его и удаляет
        из буфера. Если сообщение не полное - возвращает None.

        Args:
            buffer: Буфер с накопленными данными

        Returns:
            bytes: Извлеченное сообщение или None, если сообщение не полное

        Raises:
            ValueError: Если данные в буфере некорректны

        Example:
            >>> framer = Hl7Framer()
            >>> buffer = DefaultBuffer()
            >>> buffer.append(b"\\x0bMSH|...\\x1c\\x0d")
            >>> message = framer.extract_message(buffer)
            >>> message
            b'MSH|...'
        """
        pass