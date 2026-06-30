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

    Example:
        >>> class MSH(HL7Segment):
        ...     field_separator: str
        ...     encoding_characters: str
        ...     sending_application: Optional[str] = None
        ...
        >>> values = ["|", "^~\\&", "LAB", "CLINIC"]
        >>> msh = MSH.from_values(values)
        >>> msh.field_separator
        '|'
        >>> msh.sending_application
        'LAB'
    """

    @classmethod
    def from_values(cls, values: list[str]) -> "HL7Segment":
        """
        Создает объект сегмента из списка значений полей.

        Args:
            values: Список значений полей сегмента в порядке их определения

        Returns:
            HL7Segment: Экземпляр сегмента с заполненными полями

        Example:
            >>> segment = MSH.from_values(["|", "^~\\&", "LAB"])
        """
        fields = list(cls.model_fields)

        # Сопоставляем поля со значениями
        field_values = {}
        for i, field_name in enumerate(fields):
            if i < len(values):
                field_values[field_name] = values[i]
            else:
                field_values[field_name] = None

        return cls(**field_values)