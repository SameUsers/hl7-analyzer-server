from typing import Any

from pydantic import Field

from core.protocols.hl7.segments.hl7_segment import HL7Segment


class OBR(HL7Segment):
    """
    HL7-сегмент OBR (Observation Request).

    Содержит информацию о запросе на исследование/наблюдение.
    Включает идентификаторы заказа, тип исследования, временные метки,
    информацию об исполнителях и статусе.

    Поля соответствуют стандарту HL7 версии 2.x:
    - OBR.1  - ID набора (Set ID)
    - OBR.2  - Номер заказа (Placer Order Number)
    - OBR.3  - Номер заказа (Filler Order Number)
    - OBR.4  - Идентификатор универсальной услуги
    - OBR.5  - Приоритет
    - OBR.6  - Запрошенная дата/время
    - OBR.7  - Дата/время наблюдения
    - OBR.8  - Дата/время окончания наблюдения
    - OBR.9  - Объем сбора
    - OBR.10 - Идентификатор сборщика
    - OBR.11 - Код действия с образцом
    - OBR.12 - Код опасности
    - OBR.13 - Релевантная клиническая информация
    - OBR.14 - Дата/время получения образца
    - OBR.15 - Источник образца
    - OBR.16 - Заказывающий провайдер
    - OBR.17 - Номер телефона для обратной связи
    - OBR.18 - Поле заказчика 1
    - OBR.19 - Поле заказчика 2
    - OBR.20 - Поле исполнителя 1
    - OBR.21 - Поле исполнителя 2
    - OBR.22 - Дата/время изменения статуса отчета
    - OBR.23 - Код оплаты практики
    - OBR.24 - ID секции диагностической службы
    - OBR.25 - Статус результата
    - OBR.26 - Родительский результат
    - OBR.27 - Количество и тайминг
    - OBR.28 - Копии результатов
    - OBR.29 - Родительский элемент
    - OBR.30 - Режим транспортировки
    - OBR.31 - Причина исследования
    - OBR.32 - Основной интерпретатор результата
    - OBR.33 - Помощник интерпретатора результата
    - OBR.34 - Техник
    - OBR.35 - Транскрипционист
    - OBR.36 - Запланированная дата/время
    - OBR.37 - Количество контейнеров для образцов
    - OBR.38 - Логистика транспортировки собранного образца
    - OBR.39 - Комментарий сборщика
    - OBR.40 - Ответственность за транспортировку
    - OBR.41 - Транспортировка организована
    - OBR.42 - Сопровождение требуется
    - OBR.43 - Комментарий к транспортировке пациента

    Attributes:
        set_id: ID набора (OBR.1)
        placer_order_number: Номер заказа от заказчика (OBR.2)
        filler_order_number: Номер заказа от исполнителя (OBR.3)
        universal_service_identifier: Идентификатор услуги (OBR.4)
        priority: Приоритет (OBR.5)
        requested_date_time: Запрошенная дата/время (OBR.6)
        observation_date_time: Дата/время наблюдения (OBR.7)
        observation_end_date_time: Окончание наблюдения (OBR.8)
        collection_volume: Объем сбора (OBR.9)
        collector_identifier: Идентификатор сборщика (OBR.10)
        specimen_action_code: Код действия с образцом (OBR.11)
        danger_code: Код опасности (OBR.12)
        relevant_clinical_information: Клиническая информация (OBR.13)
        specimen_received_date_time: Получение образца (OBR.14)
        specimen_source: Источник образца (OBR.15)
        ordering_provider: Заказывающий провайдер (OBR.16)
        order_callback_phone_number: Телефон для связи (OBR.17)
        placer_field_1: Поле заказчика 1 (OBR.18)
        placer_field_2: Поле заказчика 2 (OBR.19)
        filler_field_1: Поле исполнителя 1 (OBR.20)
        filler_field_2: Поле исполнителя 2 (OBR.21)
        results_report_status_change_date_time: Изменение статуса (OBR.22)
        charge_to_practice: Оплата практики (OBR.23)
        diagnostic_service_section_id: Секция диагностики (OBR.24)
        result_status: Статус результата (OBR.25)
        parent_result: Родительский результат (OBR.26)
        quantity_timing: Количество и тайминг (OBR.27)
        result_copies_to: Копии результатов (OBR.28)
        parent: Родительский элемент (OBR.29)
        transportation_mode: Режим транспортировки (OBR.30)
        reason_for_study: Причина исследования (OBR.31)
        principal_result_interpreter: Интерпретатор (OBR.32)
        assistant_result_interpreter: Помощник интерпретатора (OBR.33)
        technician: Техник (OBR.34)
        transcriptionist: Транскрипционист (OBR.35)
        scheduled_date_time: Запланированная дата/время (OBR.36)
        number_of_sample_containers: Контейнеры образцов (OBR.37)
        transport_logistics_of_collected_sample: Логистика (OBR.38)
        collectors_comment: Комментарий сборщика (OBR.39)
        transport_arrangement_responsibility: Транспортировка (OBR.40)
        transport_arranged: Транспортировка организована (OBR.41)
        escort_required: Сопровождение требуется (OBR.42)
        planned_patient_transport_comment: Комментарий (OBR.43)
    """

    set_id: Any | None = Field(default=None)
    placer_order_number: Any | None = Field(default=None)
    filler_order_number: Any | None = Field(default=None)
    universal_service_identifier: Any | None = Field(default=None)
    priority: Any | None = Field(default=None)
    requested_date_time: Any | None = Field(default=None)
    observation_date_time: Any | None = Field(default=None)
    observation_end_date_time: Any | None = Field(default=None)
    collection_volume: Any | None = Field(default=None)
    collector_identifier: Any | None = Field(default=None)
    specimen_action_code: Any | None = Field(default=None)
    danger_code: Any | None = Field(default=None)
    relevant_clinical_information: Any | None = Field(default=None)
    specimen_received_date_time: Any | None = Field(default=None)
    specimen_source: Any | None = Field(default=None)
    ordering_provider: Any | None = Field(default=None)
    order_callback_phone_number: Any | None = Field(default=None)
    placer_field_1: Any | None = Field(default=None)
    placer_field_2: Any | None = Field(default=None)
    filler_field_1: Any | None = Field(default=None)
    filler_field_2: Any | None = Field(default=None)
    results_report_status_change_date_time: Any | None = Field(default=None)
    charge_to_practice: Any | None = Field(default=None)
    diagnostic_service_section_id: Any | None = Field(default=None)
    result_status: Any | None = Field(default=None)
    parent_result: Any | None = Field(default=None)
    quantity_timing: Any | None = Field(default=None)
    result_copies_to: Any | None = Field(default=None)
    parent: Any | None = Field(default=None)
    transportation_mode: Any | None = Field(default=None)
    reason_for_study: Any | None = Field(default=None)
    principal_result_interpreter: Any | None = Field(default=None)
    assistant_result_interpreter: Any | None = Field(default=None)
    technician: Any | None = Field(default=None)
    transcriptionist: Any | None = Field(default=None)
    scheduled_date_time: Any | None = Field(default=None)
    number_of_sample_containers: Any | None = Field(default=None)
    transport_logistics_of_collected_sample: Any | None = Field(default=None)
    collectors_comment: Any | None = Field(default=None)
    transport_arrangement_responsibility: Any | None = Field(default=None)
    transport_arranged: Any | None = Field(default=None)
    escort_required: Any | None = Field(default=None)
    planned_patient_transport_comment: Any | None = Field(default=None)
