from pydantic import BaseModel, Field

from core.domain.analyze_result import AnalyzeResult


class AccentM320BACResult(BaseModel):
    """
    Результаты биохимического анализа (BAC) для анализатора Accent M320.
    Содержит все измеряемые показатели, их значения и единицы измерения.
    Использует алиасы для соответствия именам полей в HL7-сообщениях.
    Attributes:
        analyze_type: Тип анализа (фиксированно "BAC")
        alanine_aminotransferase: Аланинаминотрансфераза (АЛТ) ["ALAT IIGEN"]
        alkaline_phosphatase: Щелочная фосфатаза (АЛФ) ["ALP"]
        total_protein: Общий белок ["TOTAL PROTEIN"]
        albumin: Альбумин ["ALBUMIN"]
        aspartate_aminotransferase: Аспартатаминотрансфераза (АСТ) ["ASAT IIGEN"]
        total_bilirubin: Общий билирубин ["BIL TOTAL"]
        triglycerides: Триглицериды ["TRIGLYCERIDES"]
        calcium: Кальций ["CA ARS"]
        cholesterol: Холестерин ["CHOL"]
        creatinine: Креатинин ["CREA ENZ"]
        glucose: Глюкоза ["GLUC"]
        urea: Мочевина ["UREA"]
        gamma_glutamyl_transferase: Гамма-глутамилтрансфераза (ГГТ) ["GGT LIQ"]
    """

    analyze_type: str = Field(default="BAC")
    """Тип анализа - биохимический (BAC)."""

    alanine_aminotransferase: str | float = Field(alias="ALAT IIGEN")
    """Аланинаминотрансфераза (АЛТ)."""

    alkaline_phosphatase: str | float = Field(alias="ALP")
    """Щелочная фосфатаза (АЛФ)."""

    total_protein: str | float = Field(alias="TOTAL PROTEIN")
    """Общий белок."""

    albumin: str | float = Field(alias="ALBUMIN")
    """Альбумин."""

    aspartate_aminotransferase: str | float = Field(alias="ASAT IIGEN")
    """Аспартатаминотрансфераза (АСТ)."""

    total_bilirubin: str | float = Field(alias="BIL TOTAL")
    """Общий билирубин."""

    triglycerides: str | float = Field(alias="TRIGLYCERIDES")
    """Триглицериды."""

    calcium: str | float = Field(alias="CA ARS")
    """Кальций."""

    cholesterol: str | float = Field(alias="CHOL")
    """Холестерин."""

    creatinine: str | float = Field(alias="CREA ENZ")
    """Креатинин."""

    glucose: str | float = Field(alias="GLUC")
    """Глюкоза."""

    urea: str | float = Field(alias="UREA")
    """Мочевина."""

    gamma_glutamyl_transferase: str | float = Field(alias="GGT LIQ")
    """Гамма-глутамилтрансфераза (ГГТ)."""


class AccentM320Result(AnalyzeResult[AccentM320BACResult]):
    """
    Результат анализа для анализатора Accent M320.
    Является специализированной версией AnalyzeResult с фиксированным
    именем анализатора и типом результата.
    """

    analyzer_name: str = "AccentM320"
