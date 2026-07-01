from pydantic import BaseModel, Field

from core.schemas.analyze_result import AnalyzeResult


class Vet5160OAKResult(BaseModel):
    """
    Результаты общего анализа крови (OAK) для анализатора Vet 5160.

    Содержит все показатели гематологического анализа, включая:
    - Лейкоцитарную формулу (проценты и абсолютные значения)
    - Эритроцитарные показатели
    - Тромбоцитарные показатели
    - Индексы эритроцитов

    Attributes:
        analyzer_type: Тип анализа (фиксированно "OAK")
        wbc: Лейкоциты (WBC)
        lymphocytes_percent: Лимфоциты % (LYM%)
        monocytes_percent: Моноциты % (MON%)
        neutrophils_percent: Нейтрофилы % (NEU%)
        eosinophils_percent: Эозинофилы % (EOS%)
        basophils_percent: Базофилы % (BASO%)
        lymphocytes_absolute: Лимфоциты # (LYM#)
        monocytes_absolute: Моноциты # (MON#)
        neutrophils_absolute: Нейтрофилы # (NEU#)
        eosinophils_absolute: Эозинофилы # (EOS#)
        basophils_absolute: Базофилы # (BASO#)
        rbc: Эритроциты (RBC)
        hemoglobin: Гемоглобин (HGB)
        hematocrit: Гематокрит (HCT)
        mean_corpuscular_volume: Средний объем эритроцита (MCV)
        mean_corpuscular_hemoglobin: Среднее содержание Hb в эритроците (MCH)
        mean_corpuscular_hemoglobin_concentration: Средняя концентрация Hb (MCHC)
        red_cell_distribution_width_cv: RDW-CV
        red_cell_distribution_width_sd: RDW-SD
        platelets: Тромбоциты (PLT)
        mean_platelet_volume: Средний объем тромбоцита (MPV)
        platelet_distribution_width: Ширина распределения тромбоцитов (PDW)
        plateletcrit: Тромбокрит (PCT)
        platelet_large_cell_ratio: Отношение крупных тромбоцитов (P_LCR)
        platelet_large_cell_count: Количество крупных тромбоцитов (P_LCC)
    """

    analyze_type: str = Field(default="OAK")
    """Тип анализа - общий анализ крови (OAK)."""

    # Лейкоцитарная формула (проценты)
    wbc: str | float = Field(alias="WBC")
    """Общее количество лейкоцитов."""

    lymphocytes_percent: str | float = Field(alias="LYM%")
    """Лимфоциты (проценты)."""

    monocytes_percent: str | float = Field(alias="MON%")
    """Моноциты (проценты)."""

    neutrophils_percent: str | float = Field(alias="NEU%")
    """Нейтрофилы (проценты)."""

    eosinophils_percent: str | float = Field(alias="EOS%")
    """Эозинофилы (проценты)."""

    basophils_percent: str | float = Field(alias="BASO%")
    """Базофилы (проценты)."""

    # Лейкоцитарная формула (абсолютные значения)
    lymphocytes_absolute: str | float = Field(alias="LYM#")
    """Лимфоциты (абсолютное количество)."""

    monocytes_absolute: str | float = Field(alias="MON#")
    """Моноциты (абсолютное количество)."""

    neutrophils_absolute: str | float = Field(alias="NEU#")
    """Нейтрофилы (абсолютное количество)."""

    eosinophils_absolute: str | float = Field(alias="EOS#")
    """Эозинофилы (абсолютное количество)."""

    basophils_absolute: str | float = Field(alias="BASO#")
    """Базофилы (абсолютное количество)."""

    # Эритроцитарные показатели
    rbc: str | float = Field(alias="RBC")
    """Эритроциты (RBC)."""

    hemoglobin: str | float = Field(alias="HGB")
    """Гемоглобин (HGB)."""

    hematocrit: str | float = Field(alias="HCT")
    """Гематокрит (HCT)."""

    # Эритроцитарные индексы
    mean_corpuscular_volume: str | float = Field(alias="MCV")
    """Средний объем эритроцита (MCV)."""

    mean_corpuscular_hemoglobin: str | float = Field(alias="MCH")
    """Среднее содержание гемоглобина в эритроците (MCH)."""

    mean_corpuscular_hemoglobin_concentration: str | float = Field(alias="MCHC")
    """Средняя концентрация гемоглобина в эритроците (MCHC)."""

    # Показатели распределения эритроцитов
    red_cell_distribution_width_cv: str | float = Field(alias="RDW_CV")
    """Ширина распределения эритроцитов (RDW-CV)."""

    red_cell_distribution_width_sd: str | float = Field(alias="RDW_SD")
    """Ширина распределения эритроцитов (RDW-SD)."""

    # Тромбоцитарные показатели
    platelets: str | float = Field(alias="PLT")
    """Тромбоциты (PLT)."""

    mean_platelet_volume: str | float = Field(alias="MPV")
    """Средний объем тромбоцита (MPV)."""

    platelet_distribution_width: str | float = Field(alias="PDW")
    """Ширина распределения тромбоцитов (PDW)."""

    plateletcrit: str | float = Field(alias="PCT")
    """Тромбокрит (PCT)."""

    platelet_large_cell_ratio: str | float = Field(alias="P_LCR")
    """Отношение крупных тромбоцитов (P-LCR)."""

    platelet_large_cell_count: str | float = Field(alias="P_LCC")
    """Количество крупных тромбоцитов (P-LCC)."""


class Vet5160Result(AnalyzeResult[Vet5160OAKResult]):
    """
    Результат анализа для гематологического анализатора Vet 5160.
    Является специализированной версией AnalyzeResult с фиксированным
    именем анализатора и типом результата (OAK).
    """

    analyzer_name: str = "5160Vet"
