from core.devices.registry import DEVICE_REGISTRY
from core.application.factories.component_factory import ComponentFactory


def create_handler(host: str):
    """
    Создает обработчик для анализатора по его IP-адресу.

    Фабричная функция, которая по IP-адресу клиента определяет тип анализатора,
    получает его конфигурацию из реестра устройств и делегирует создание
    обработчика фабрике компонентов.

    Args:
        host: IP-адрес анализатора (например, "127.0.0.1")

    Returns:
        HandlerInterface: Экземпляр обработчика для указанного анализатора

    Raises:
        RuntimeError: Если для указанного хоста не найден анализатор
                      в реестре устройств

    Example:
        >>> handler = create_handler("192.168.1.100")
        >>> await handler.on_data(b"\\x0bMSH|...\\x1c\\x0d")
    """
    device_configuration = DEVICE_REGISTRY.get(host)

    if device_configuration is None:
        raise RuntimeError(
            f"Unknown analyzer for host: {host}. "
            f"Available hosts: {list(DEVICE_REGISTRY.keys())}"
        )

    return ComponentFactory.create_handler(device_configuration)