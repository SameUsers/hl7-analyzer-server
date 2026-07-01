def decode_message(message: bytes) -> str:
    """
    Декодирует байтовое сообщение в строку UTF-8.
    Преобразует входящие байтовые данные в строку для дальнейшей
    обработки парсером.
    """
    return message.decode("utf-8")
