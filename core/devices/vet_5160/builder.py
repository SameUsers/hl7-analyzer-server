from loguru import logger

from core.contracts.builder import BuilderInterface
from core.devices.vet_5160.schema.schemas import Vet5160Result
from core.protocols.hl7.message import HL7Message


class Vet5160Builder(BuilderInterface):
    """
    Билдер для гематологического анализатора Vet 5160.

    Преобразует HL7-сообщение в структурированный результат анализа.
    Извлекает значения из OBX-сегментов, используя Observation Identifier
    в качестве ключей для сопоставления с полями результата.

    Особенности:
    - Использует Observation Identifier как ключ
    - Пропускает значения с "Image" в идентификаторе (графические данные)
    - Пропускает сегменты без значения
    - Возвращает OAK (общий анализ крови) результат

    Пример:
        >>> builder = Vet5160Builder()
        >>> message = HL7Message(...)
        >>> result = builder.build_analyze(message)
        >>> print(result.result.wbc)
        '7.5'
    """

    def __init__(self) -> None:
        """Инициализация билдера."""
        logger.debug("Created {}", self)

    def build_analyze(self, message: HL7Message) -> Vet5160Result:
        """
        Строит структурированный результат из HL7-сообщения.

        Проходит по всем OBX-сегментам сообщения и собирает значения,
        используя Observation Identifier как идентификатор параметра.

        Фильтры:
        - Игнорирует OBX-сегменты без Observation Identifier
        - Игнорирует OBX-сегменты с пустым значением
        - Игнорирует сегменты с "Image" в идентификаторе (графика)

        Args:
            message: Разобранное HL7-сообщение

        Returns:
            Vet5160Result: Структурированный результат анализа (OAK)

        Raises:
            ValueError: Если в сообщении нет OBX-сегментов
            ValidationError: Если собранные данные не проходят валидацию

        Note:
            Использует Observation Identifier для сопоставления с полями
            схемы OAKSchemaVet5160. Например:
                - "WBC" -> wbc
                - "RBC" -> rbc
                - "HGB" -> hemoglobin
                - "PLT" -> platelets
                - "LYM%" -> lymphocytes_percent
                - "NEU#" -> neutrophils_absolute
                - ...
        """
        raw = {}

        for obx in message.obx:
            # Пропускаем OBX-сегменты без идентификатора
            if not obx.observation_identifier:
                continue

            # Пропускаем сегменты без значения
            if obx.observation_value is None:
                continue

            # Пропускаем графические данные (гистограммы, скаттерограммы)
            if "Image" in str(obx.observation_identifier):
                logger.debug(
                    "Skipping image data: {}",
                    obx.observation_identifier,
                )
                continue

            raw[obx.observation_identifier] = obx.observation_value

        logger.debug(
            "Built Vet 5160 result with {} parameters",
            len(raw),
        )

        # Валидируем и возвращаем результат
        return Vet5160Result(result=raw)

    def __del__(self) -> None:
        """Деструктор для логирования удаления объекта."""
        logger.debug("Deleted {}", self)
