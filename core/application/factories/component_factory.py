from core.application.handlers.analyzer import AnalyzerHandler
from core.devices.core.profile import DeviceProfile


class ComponentFactory:
    """
    Фабрика компонентов для создания обработчиков анализаторов.
    Предоставляет статические методы для создания полностью сконфигурированных
    обработчиков на основе профиля устройства. Инкапсулирует логику создания
    и сборки всех необходимых компонентов.
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
        """
        protocol = config.protocol

        return AnalyzerHandler(
            builder=config.builder(),
            parser=protocol.parser(),
            framer=protocol.framer(),
            buffer=protocol.buffer(),
        )

create_handler = ComponentFactory()
