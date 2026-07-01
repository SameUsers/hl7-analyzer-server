from core.contracts.builder import BuilderInterface
from core.devices.accent_m320.builder import Accent320Builder
from core.devices.core.enums import DeviceBuilderEnum
from core.devices.seamanty_smt.builder import SemantyBuilder
from core.devices.vet_5160.builder import Vet5160Builder

DEVICE_BUILDER_REGISTRY: dict[DeviceBuilderEnum, BuilderInterface] = {
    DeviceBuilderEnum.VET_5160 : Vet5160Builder,
    DeviceBuilderEnum.ACCENT_M320: Accent320Builder,
    DeviceBuilderEnum.SEAMATY_SMT_120VP: SemantyBuilder
}


