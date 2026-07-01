from pydantic import BaseModel


class HL7Segment(BaseModel):
    """
    Базовый класс для всех HL7-сегментов.
    Предоставляет общую логику для создания объектов сегментов из
    списка значений полей. Каждый конкретный сегмент должен наследовать
    этот класс и определять свои поля.
    Особенности:
    - Автоматически сопоставляет поля по порядку из значений
    - Если значений меньше чем полей - недостающие поля становятся None
    - Если значений больше чем полей - лишние игнорируются
    """

    @classmethod
    def from_values(cls, values: list[str]) -> "HL7Segment":
        """
        Создает объект сегмента из списка значений полей.
        """
        fields = list(cls.model_fields)
        field_values = {}
        for i, field_name in enumerate(fields):
            if i < len(values):
                field_values[field_name] = values[i] if values[i] != "" else None
            else:
                field_values[field_name] = None

        return cls(**field_values)
