from pydantic import BaseModel, Field

from core.schemas.analyze_result import AnalyzeResult


class RedSchema(BaseModel):
    """
    Схема результатов для анализатора RED (коагулологические исследования).
    Содержит показатели свертываемости крови:
    - АЧТВ (активированное частичное тромбопластиновое время)
    - ПВ (протромбиновое время)
    - ТВ (тромбиновое время)
    - Фибриноген
    """

    analyze_type: str = Field(default="RED")
    APTT: str | float = Field(alias="APTT")
    PT: str | float = Field(alias="PT")
    TT: str | float = Field(alias="TT")
    Fib: str | float = Field(alias="Fib")


class PinkSchema(BaseModel):
    """
    Схема результатов для анализатора PINK (газы крови и электролиты).
    Содержит показатели кислотно-щелочного состояния и электролитов.
    Attributes:
        analyze_type: Тип анализа (фиксированно "PINK")
        Crea: Креатинин
        BUN: Мочевина (Blood Urea Nitrogen)
        BUN_CREA: Отношение BUN к креатинину
        GLU: Глюкоза
        LAC: Лактат
        tCO2: Общий углекислый газ
        Ca: Кальций
        PHOS: Фосфор
        Mg: Магний
        pH: Водородный показатель
        K: Калий
        Na: Натрий
        Cl: Хлор
    """

    analyze_type: str = Field(default="PINK")
    Crea: str | float = Field(alias="Crea")
    BUN: str | float = Field(alias="BUN")
    BUN_CREA: str | float = Field(alias="BUN/CREA")
    GLU: str | float = Field(alias="GLU")
    LAC: str | float = Field(alias="LAC")
    tCO2: str | float = Field(alias="tCO2")
    Ca: str | float = Field(alias="Ca")
    PHOS: str | float = Field(alias="PHOS")
    Mg: str | float = Field(alias="Mg")
    pH: str | float = Field(alias="pH")
    K: str | float = Field(alias="K")
    Na: str | float = Field(alias="Na")
    Cl: str | float = Field(alias="Cl")


class YellowSchema(BaseModel):
    """
    Схема результатов для анализатора YELLOW (биохимия).
    Содержит биохимические показатели сыворотки крови.
    Attributes:
        analyze_type: Тип анализа (фиксированно "YELLOW")
        ALB: Альбумин
        TP: Общий белок
        GLOB: Глобулин
        A_G: Отношение альбумин/глобулин
        TB: Общий билирубин
        ALT: Аланинаминотрансфераза
        ALP: Щелочная фосфатаза
        CHE: Холинэстераза
        AMY: Амилаза
        Crea: Креатинин
        UA: Мочевая кислота
        BUN: Мочевина
        BUN_CREA: Отношение BUN к креатинину
        GLU: Глюкоза
        K: Калий
        Na: Натрий
    """

    analyze_type: str = Field(default="YELLOW")
    ALB: str | float = Field(alias="ALB")
    TP: str | float = Field(alias="TP")
    GLOB: str | float = Field(alias="GLOB")
    A_G: str | float = Field(alias="A/G")
    TB: str | float = Field(alias="TB")
    ALT: str | float = Field(alias="ALT")
    ALP: str | float = Field(alias="ALP")
    CHE: str | float = Field(alias="CHE")
    AMY: str | float = Field(alias="AMY")
    Crea: str | float = Field(alias="Crea")
    UA: str | float = Field(alias="UA")
    BUN: str | float = Field(alias="BUN")
    BUN_CREA: str | float = Field(alias="BUN/CREA")
    GLU: str | float = Field(alias="GLU")
    K: str | float = Field(alias="K")
    Na: str | float = Field(alias="Na")


class GreenSchema(BaseModel):
    """
    Схема результатов для анализатора GREEN (биохимия расширенная).
    Содержит расширенный набор биохимических показателей.
    Attributes:
        analyze_type: Тип анализа (фиксированно "GREEN")
        ALB: Альбумин
        TP: Общий белок
        GLOB: Глобулин
        A_G: Отношение альбумин/глобулин
        TB: Общий билирубин
        AST: Аспартатаминотрансфераза
        ALT: Аланинаминотрансфераза
        AMY: Амилаза
        CK: Креатинкиназа
        Crea: Креатинин
        BUN: Мочевина
        BUN_CREA: Отношение BUN к креатинину
        GLU: Глюкоза
        TG: Триглицериды
        Ca: Кальций
        PHOS: Фосфор
    """

    analyze_type: str = Field(default="GREEN")
    ALB: str | float = Field(alias="ALB")
    TP: str | float = Field(alias="TP")
    GLOB: str | float = Field(alias="GLOB")
    A_G: str | float = Field(alias="A/G")
    TB: str | float = Field(alias="TB")
    AST: str | float = Field(alias="AST")
    ALT: str | float = Field(alias="ALT")
    AMY: str | float = Field(alias="AMY")
    CK: str | float = Field(alias="CK")
    Crea: str | float = Field(alias="Crea")
    BUN: str | float = Field(alias="BUN")
    BUN_CREA: str | float = Field(alias="BUN/CREA")
    GLU: str | float = Field(alias="GLU")
    TG: str | float = Field(alias="TG")
    Ca: str | float = Field(alias="Ca")
    PHOS: str | float = Field(alias="PHOS")


class BrownSchema(BaseModel):
    """
    Схема результатов для анализатора BROWN (биохимия полная).
    Содержит наиболее полный набор биохимических показателей.
    Attributes:
        analyze_type: Тип анализа (фиксированно "BROWN")
        ALB: Альбумин
        TP: Общий белок
        GLOB: Глобулин
        A_G: Отношение альбумин/глобулин
        TB: Общий билирубин
        GGT: Гамма-глутамилтрансфераза
        AST: Аспартатаминотрансфераза
        ALT: Аланинаминотрансфераза
        ALP: Щелочная фосфатаза
        TBA: Желчные кислоты
        AMY: Амилаза
        LPS: Липаза
        LDH: Лактатдегидрогеназа
        CK: Креатинкиназа
        Crea: Креатинин
        UA: Мочевая кислота
        BUN: Мочевина
        BUN_CREA: Отношение BUN к креатинину
        GLU: Глюкоза
        TC: Общий холестерин
        TG: Триглицериды
        tCO2: Общий углекислый газ
        Ca: Кальций
        PHOS: Фосфор
    """

    analyze_type: str = Field(default="BROWN")
    ALB: str | float = Field(alias="ALB")
    TP: str | float = Field(alias="TP")
    GLOB: str | float = Field(alias="GLOB")
    A_G: str | float = Field(alias="A/G")
    TB: str | float = Field(alias="TB")
    GGT: str | float = Field(alias="GGT")
    AST: str | float = Field(alias="AST")
    ALT: str | float = Field(alias="ALT")
    ALP: str | float = Field(alias="ALP")
    TBA: str | float = Field(alias="TBA")
    AMY: str | float = Field(alias="AMY")
    LPS: str | float = Field(alias="LPS")
    LDH: str | float = Field(alias="LDH")
    CK: str | float = Field(alias="CK")
    Crea: str | float = Field(alias="Crea")
    UA: str | float = Field(alias="UA")
    BUN: str | float = Field(alias="BUN")
    BUN_CREA: str | float = Field(alias="BUN/CREA")
    GLU: str | float = Field(alias="GLU")
    TC: str | float = Field(alias="TC")
    TG: str | float = Field(alias="TG")
    tCO2: str | float = Field(alias="tCO2")
    Ca: str | float = Field(alias="Ca")
    PHOS: str | float = Field(alias="PHOS")


# Тип для объединения всех схем Seamaty
SeamatyResultData = RedSchema | PinkSchema | YellowSchema | GreenSchema | BrownSchema

class SeamantyResult(AnalyzeResult[SeamatyResultData]):
    """
    Результат анализа для анализатора Seamaty SMT-120VP.
    Поддерживает пять типов анализов:
    - RED: Коагулологические исследования
    - PINK: Газы крови и электролиты
    - YELLOW: Биохимия (стандарт)
    - GREEN: Биохимия (расширенная)
    - BROWN: Биохимия (полная)
    """
    analyzer_name: str = "Seamanty"
