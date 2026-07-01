from enum import StrEnum

from core.protocols.hl7.config import HL7_V1, ProtocolConfig


class ProtocolEnum(StrEnum):
    HL7_V1 = "HL7_V1"


PROTOCOL_REGISTRY: dict[ProtocolEnum, ProtocolConfig] = {
    ProtocolEnum.HL7_V1 : HL7_V1
}
