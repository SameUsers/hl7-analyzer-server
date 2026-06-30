import asyncio

from core.infrastructure.tcp.server import TcpServer


async def main() -> None:
    """
    Главная точка входа в приложение.

    Создает и запускает TCP-сервер для приема и обработки сообщений
    от анализаторов. Сервер слушает на всех интерфейсах (0.0.0.0)
    на порту 8001.

    При инициализации сервер создает необходимые структуры данных
    и подготавливается к приему подключений.

    Raises:
        RuntimeError: Если сервер не может быть инициализирован
        OSError: Если порт 8001 уже занят

    Example:
        >>> # Запуск сервера
        >>> asyncio.run(main())
        # Сервер запущен на 0.0.0.0:8001
    """
    server = TcpServer(
        port=8001,
        host="0.0.0.0",
    )

    await server.initialize()
    await server.run()


if __name__ == "__main__":
    """
    Запуск приложения при прямом выполнении скрипта.

    Позволяет запускать сервер командой:
        python main.py
    """
    asyncio.run(main())
