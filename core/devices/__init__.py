from enum import StrEnum

from core.contracts.builder import BuilderInterface
from core.devices.accent_m320.builder import Accent320Builder
from core.devices.seamanty_smt.builder import SemantyBuilder
from core.devices.vet_5160.builder import Vet5160Builder


class DeviceBuilderEnum(StrEnum):
    VET_5160 = "VET_5160"
    ACCENT_M320 = "ACCENT_M320"
    SEAMATY_SMT_120VP = "SEAMATY_SMT_120VP"

#Тут регистрируются билдеры реализованные
#Из них потом выбирается по хосту нужный билдер для того или инонго анализатора
DEVICE_BUILDER_REGISTRY: dict[DeviceBuilderEnum, BuilderInterface] = {
    DeviceBuilderEnum.VET_5160 : Vet5160Builder,
    DeviceBuilderEnum.ACCENT_M320: Accent320Builder,
    DeviceBuilderEnum.SEAMATY_SMT_120VP: SemantyBuilder
}


