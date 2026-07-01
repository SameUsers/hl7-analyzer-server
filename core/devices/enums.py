from enum import StrEnum


class DeviceBuilderEnum(StrEnum):
    """
    Для ограничения возможных названий в ямл
    """
    VET_5160 = "VET_5160"
    ACCENT_M320 = "ACCENT_M320"
    SEAMATY_SMT_120VP = "SEAMATY_SMT_120VP"

class DeviceTypeEnum(StrEnum):
    ANALIZER = 'ANALIZER'#Анализатор

