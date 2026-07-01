from core.protocols.core.enums import ProtocolEnum
from core.protocols.hl7.config import HL7_V1, ProtocolConfig

PROTOCOL_REGISTRY: dict[ProtocolEnum, ProtocolConfig] = {
    ProtocolEnum.HL7_V1 : HL7_V1
}
