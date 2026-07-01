from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict
from pydantic_settings_sources import YamlEnvSettings

from core.devices.enums import DeviceBuilderEnum, DeviceTypeEnum
from core.protocols.core.enums import ProtocolEnum


class TCPServerConfig(BaseModel):
    host: str
    port: int
    read_size: int


class StorageConfig(BaseModel):
    analyze_path: Path


class DeviceConfig(BaseModel):
    device_type: DeviceTypeEnum
    device_ip: str
    protocol: ProtocolEnum
    device_name: DeviceBuilderEnum


class Settings(YamlEnvSettings):
    server: TCPServerConfig
    storage: StorageConfig
    devices: list[DeviceConfig]

    model_config = SettingsConfigDict(
        yaml_file=Path(__file__).resolve().parents[3] / "settings.yaml",
        extra="ignore",
    )


settings = Settings()
