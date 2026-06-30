from pydantic import BaseModel


class ProtocolMessage(BaseModel):
    """
    Структурированное представление сообщения протокола.

    Базовый класс для всех сообщений, получаемых от анализаторов.
    Содержит общую информацию о типе протокола и может быть расширен
    для конкретных протоколов с дополнительными полями.

    Attributes:
        protocol_type (str): Тип протокола (например, "HL7", "ASTM", "MQTT")

    Example:
        >>> class HL7Message(ProtocolMessage):
        ...     segments: list[list[str]] = Field(default_factory=list)
        ...     message_type: str = Field(default="")
        ...
        >>> msg = HL7Message(
        ...     protocol_type="HL7",
        ...     segments=[["MSH", "|", "^~\\&"], ["OBX", "1", "NM"]],
        ...     message_type="ORM_O01",
        ... )
    """

    protocol_type: str
    """Тип протокола обмена данными (HL7, ASTM, MQTT и т.д.)."""