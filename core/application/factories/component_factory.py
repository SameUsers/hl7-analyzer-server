from core.application.handlers.analyzer import AnalyzerHandler
from core.devices.registry import DeviceProfile


class ComponentFactory:
    """
    Фабрика компонентов для создания обработчиков анализаторов.

    Предоставляет статические методы для создания полностью сконфигурированных
    обработчиков на основе профиля устройства. Инкапсулирует логику создания
    и сборки всех необходимых компонентов.

    Пример:
        >>> profile = DeviceProfile(
        ...     host="127.0.0.1",
        ...     name="Accent M320",
        ...     builder=Accent320Builder,
        ...     protocol=HL7Protocol(),
        ... )
        >>> handler = ComponentFactory.create_handler(profile)
    """

    @staticmethod
    def create_handler(config: DeviceProfile) -> AnalyzerHandler:
        """
        Создает обработчик для анализатора на основе профиля устройства.

        Собирает все необходимые компоненты из профиля устройства:
        - Билдер для парсинга данных
        - Парсер для разбора сообщений
        - Фреймер для выделения сообщений из потока
        - Буфер для временного хранения данных

        Args:
            config: Профиль устройства, содержащий конфигурацию
                    всех необходимых компонентов

        Returns:
            AnalyzerHandler: Полностью сконфигурированный обработчик

        Raises:
            AttributeError: Если в профиле отсутствуют обязательные компоненты

        Example:
            >>> handler = ComponentFactory.create_handler(device_profile)
            >>> result = await handler.on_data(b"\\x0bMSH|...\\x1c\\x0d")
        """
        protocol = config.protocol

        return AnalyzerHandler(
            builder=config.builder(),
            parser=protocol.parser(),
            framer=protocol.framer(),
            buffer=protocol.buffer(),
        )
