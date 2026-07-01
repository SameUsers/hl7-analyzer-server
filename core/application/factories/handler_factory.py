from core.application.factories.component_factory import ComponentFactory
from core.devices.registry import DEVICE_REGISTRY


def create_handler(host: str):
    """
    Создает обработчик для анализатора по его IP-адресу.
    Фабричная функция, которая по IP-адресу клиента определяет тип анализатора,
    получает его конфигурацию из реестра устройств и делегирует создание
    обработчика фабрике компонентов.
    """
    device_configuration = DEVICE_REGISTRY.get(host)

    if device_configuration is None:
        raise RuntimeError(
            f"Unknown analyzer for host: {host}. "
            f"Available hosts: {list(DEVICE_REGISTRY.keys())}"
        )

    return ComponentFactory.create_handler(device_configuration)
