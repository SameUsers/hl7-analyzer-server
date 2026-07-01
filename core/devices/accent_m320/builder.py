from loguru import logger

from core.contracts.builder import BuilderInterface
from core.devices.accent_m320.schema.schema import AccentM320Result
from core.protocols.hl7.message import HL7Message
from core.shared.rounder import rounder


class Accent320Builder(BuilderInterface):
    """
    Билдер для анализатора Accent M320.
    Преобразует HL7-сообщение в структурированный результат анализа.
    Извлекает значения из OBX-сегментов, используя Observation Sub-ID
    в качестве ключей для сопоставления с полями результата.
    """

    def __init__(self) -> None:
        """Инициализация билдера."""
        logger.debug("Created {}", self)

    def build_analyze(self, message: HL7Message) -> AccentM320Result:
        """
        Строит структурированный результат из HL7-сообщения.
        Проходит по всем OBX-сегментам сообщения и собирает значения,
        используя Observation Sub-ID как идентификатор параметра.
        """
        raw = {}

        for obx in message.obx:
            # Пропускаем OBX-сегменты без Sub-ID
            if not obx.observation_sub_id:
                continue

            # Пропускаем сегменты без значения
            value = obx.observation_value
            if value is None:
                continue

            # Сохраняем значение с округлением
            raw[obx.observation_sub_id] = rounder(value)

        logger.debug(
            "Built Accent M320 result with {} parameters",
            len(raw),
        )

        # Валидируем и возвращаем результат
        return AccentM320Result(result=raw)

    def __del__(self) -> None:
        """Деструктор для логирования удаления объекта."""
        logger.debug("Deleted {}", self)
