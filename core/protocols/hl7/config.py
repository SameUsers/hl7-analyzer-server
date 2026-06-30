from core.infrastructure.tcp.buffer import DefaultBuffer
from core.protocols.hl7.framer import Hl7FramerV1
from core.protocols.hl7.parser import Hl7ParserV1
from core.protocols.config import ProtocolConfig


# Конфигурация протокола HL7 версии 1
#
# Определяет набор компонентов для работы с протоколом HL7:
#   - Framer: Выделяет сообщения из потока по маркерам 0x0B и 0x1C0D
#   - Parser: Разбирает HL7-сообщения на сегменты
#   - Buffer: Стандартный буфер для накопления данных
#
# Используется в DeviceProfile для конфигурации обработчиков
# анализаторов, работающих по протоколу HL7.
#
# Пример:
#     profile = DeviceProfile(
#         protocol=HL7_V1,
#         builder=Accent320Builder,
#     )
HL7_V1 = ProtocolConfig(
    framer=Hl7FramerV1,
    parser=Hl7ParserV1,
    buffer=DefaultBuffer,
)