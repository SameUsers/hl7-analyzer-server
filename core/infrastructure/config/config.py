from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict
from pydantic_settings_sources import YamlEnvSettings


class TCPServerConfig(BaseModel):
    host: str
    port: int
    read_size: int


class StorageConfig(BaseModel):
    analyze_path: Path


class DeviceConfig(BaseModel):
    device_ip: str
    protocol: str
    device_name: str


class Settings(YamlEnvSettings):
    server: TCPServerConfig
    storage: StorageConfig
    devices: list[DeviceConfig]

    model_config = SettingsConfigDict(
        yaml_file=Path(__file__).resolve().parents[3] / "settings.yaml",
        extra="ignore",
    )


settings = Settings()
