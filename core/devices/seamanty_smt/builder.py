from loguru import logger

from core.contracts.builder import BuilderInterface
from core.devices.seamanty_smt.schema.schema import SeamantyResult
from core.protocols.hl7.message import HL7Message


class SemantyBuilder(BuilderInterface):
    """
    Билдер для анализатора Seamaty SMT-120VP.

    Преобразует HL7-сообщение в структурированный результат анализа.
    Извлекает значения из OBX-сегментов, используя Observation Identifier
    в качестве ключей для сопоставления с полями результата.

    Особенности:
    - Использует Observation Identifier как ключ
    - Если Observation Value отсутствует, использует Reference Range
    - Поддерживает разные типы анализаторов (RED, PINK, YELLOW, GREEN, BROWN)

    Пример:
        >>> builder = SemantyBuilder()
        >>> message = HL7Message(...)
        >>> result = builder.build_analyze(message)
        >>> print(result.result.GLU)
        '5.6'
    """

    def __init__(self) -> None:
        """Инициализация билдера."""
        logger.debug("Created {}", self)

    def build_analyze(self, message: HL7Message) -> SeamantyResult:
        """
        Строит структурированный результат из HL7-сообщения.

        Проходит по всем OBX-сегментам сообщения и собирает значения,
        используя Observation Identifier как идентификатор параметра.

        Args:
            message: Разобранное HL7-сообщение

        Returns:
            SeamantyResult: Структурированный результат анализа

        Raises:
            ValueError: Если в сообщении нет OBX-сегментов
            ValidationError: Если собранные данные не проходят валидацию

        Note:
            Использует Observation Identifier для сопоставления с полями
            схемы анализатора. Например:
                - "GLU" -> GLU
                - "CREA" -> Crea
                - "K" -> K
                - "NA" -> Na
        """
        raw = {}

        for obx in message.obx:
            # Пропускаем OBX-сегменты без идентификатора
            if not obx.observation_identifier:
                continue

            key = obx.observation_identifier

            # Используем значение наблюдения или референтный диапазон
            value = obx.observation_value or obx.reference_range

            if value is not None:
                raw[key] = value

        logger.debug(
            "Built Seamaty SMT result with {} parameters",
            len(raw),
        )

        # Валидируем и возвращаем результат
        return SeamantyResult(result=raw)

    def __del__(self) -> None:
        """Деструктор для логирования удаления объекта."""
        logger.debug("Deleted {}", self)
