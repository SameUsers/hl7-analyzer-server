from core.devices.accent_m320.builder import Accent320Builder
from core.devices.profile import DeviceProfile
from core.devices.seamanty_smt.builder import SemantyBuilder
from core.devices.vet_5160.builder import Vet5160Builder
from core.protocols.hl7.config import HL7_V1

# Реестр устройств с привязкой IP-адресов к профилям анализаторов
#
# Содержит соответствие между IP-адресами анализаторов и их конфигурациями.
# Каждый профиль определяет:
#   - Протокол обмена (HL7_V1, HL7_V2 и т.д.)
#   - Билдер для парсинга данных конкретного анализатора
#
# При добавлении нового анализатора необходимо:
#   1. Создать билдер в соответствующей директории
#   2. Добавить запись в реестр с IP-адресом устройства
#
# Пример:
#     "192.168.1.100": DeviceProfile(
#         protocol=HL7_V1,
#         builder=NewAnalyzerBuilder
#     )
DEVICE_REGISTRY = {
    "127.0.0.2": DeviceProfile(
        protocol=HL7_V1,
        builder=Accent320Builder,
    ),
    "127.0.0.1": DeviceProfile(
        protocol=HL7_V1,
        builder=Vet5160Builder,
    ),
    "127.0.0.3": DeviceProfile(
        protocol=HL7_V1,
        builder=SemantyBuilder,
    ),
}
