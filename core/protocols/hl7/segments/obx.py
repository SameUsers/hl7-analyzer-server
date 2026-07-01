from core.protocols.hl7.segments.hl7_segment import HL7Segment


class OBX(HL7Segment):
    """
    HL7-сегмент OBX (Observation Result).
    Содержит результаты наблюдений/исследований. Является одним из
    наиболее важных сегментов для передачи лабораторных результатов.
    Attributes:
        set_id: ID набора (OBX.1)
        value_type: Тип значения (OBX.2)
        observation_identifier: Идентификатор наблюдения (OBX.3)
        observation_sub_id: ID под-наблюдения (OBX.4)
        observation_value: Значение наблюдения (OBX.5)
        units: Единицы измерения (OBX.6)
        reference_range: Референтный диапазон (OBX.7)
        abnormal_flags: Флаги аномалий (OBX.8)
        probability: Вероятность (OBX.9)
        nature_of_abnormal_test: Природа аномалии (OBX.10)
        observation_result_status: Статус результата (OBX.11)
        effective_date_of_reference_range: Дата действия диапазона (OBX.12)
        user_defined_access_checks: Проверки доступа (OBX.13)
        date_time_of_observation: Дата/время наблюдения (OBX.14)
        producers_id: ID производителя (OBX.15)
        responsible_observer: Ответственный наблюдатель (OBX.16)
        observation_method: Метод наблюдения (OBX.17)
        equipment_instance_identifier: ID оборудования (OBX.18)
        date_time_of_analysis: Дата/время анализа (OBX.19)
    """
    set_id: str | None = None
    value_type: str | None = None
    observation_identifier: str | None = None
    observation_sub_id: str | None = None
    observation_value: str | None = None
    units: str | None = None
    reference_range: str | None = None
    abnormal_flags: str | None = None
    probability: str | None = None
    nature_of_abnormal_test: str | None = None
    observation_result_status: str | None = None
    effective_date_of_reference_range: str | None = None
    user_defined_access_checks: str | None = None
    date_time_of_observation: str | None = None
    producers_id: str | None = None
    responsible_observer: str | None = None
    observation_method: str | None = None
    equipment_instance_identifier: str | None = None
    date_time_of_analysis: str | None = None
