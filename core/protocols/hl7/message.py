from core.protocols.hl7.segments.msh import MSH
from core.protocols.hl7.segments.obr import OBR
from core.protocols.hl7.segments.obx import OBX
from core.protocols.hl7.segments.pid import PID
from core.protocols.schema import ProtocolMessage


class HL7Message(ProtocolMessage):
    """
    Структурированное представление HL7-сообщения.

    Содержит все сегменты HL7-сообщения, разобранные по типам.
    Используется для передачи данных между парсером и билдером.
    """

    protocol_type: str = "HL7V1"
    """Тип протокола - HL7 версии 1."""

    msh: MSH
    """Сегмент заголовка сообщения (Message Header)."""

    pid: PID | None = None
    """Сегмент идентификации пациента (Patient Identification)."""

    obr: OBR | None = None
    """Сегмент запроса на исследование (Observation Request)."""

    obx: list[OBX] = []
    """Список сегментов результатов исследований (Observation Result)."""
