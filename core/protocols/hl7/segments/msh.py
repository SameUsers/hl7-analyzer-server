from typing import Any

from pydantic import Field

from core.protocols.hl7.segments.hl7_segment import HL7Segment


class MSH(HL7Segment):
    """
    HL7-сегмент MSH (Message Header).
    Содержит заголовочную информацию сообщения, включая тип сообщения,
    отправителя, получателя, временные метки и другие метаданные.
    Этот сегмент является обязательным для всех HL7-сообщений.
    Attributes:
        field_separator: Разделитель полей (MSH.1)
        encoding_characters: Кодирующие символы (MSH.2)
        sending_application: Приложение-отправитель (MSH.3)
        sending_facility: Учреждение-отправитель (MSH.4)
        receiving_application: Приложение-получатель (MSH.5)
        receiving_facility: Учреждение-получатель (MSH.6)
        date_time_of_message: Дата/время сообщения (MSH.7)
        security: Безопасность (MSH.8)
        message_type: Тип сообщения (MSH.9)
        message_control_id: Идентификатор управления (MSH.10)
        processing_id: Идентификатор обработки (MSH.11)
        version_id: Версия HL7 (MSH.12)
        sequence_number: Номер последовательности (MSH.13)
        continuation_pointer: Указатель продолжения (MSH.14)
        accept_acknowledgment_type: Тип подтверждения приема (MSH.15)
        application_acknowledgment_type: Тип подтверждения приложения (MSH.16)
        country_code: Код страны (MSH.17)
        character_set: Набор символов (MSH.18)
        principal_language_of_message: Основной язык сообщения (MSH.19)
        alternate_character_set_handling_scheme: Схема обработки символов (MSH.20)
    """

    field_separator: Any | None = Field(default=None)
    encoding_characters: Any | None = Field(default=None)
    sending_application: Any | None = Field(default=None)
    sending_facility: Any | None = Field(default=None)
    receiving_application: Any | None = Field(default=None)
    receiving_facility: Any | None = Field(default=None)
    date_time_of_message: Any | None = Field(default=None)
    security: Any | None = Field(default=None)
    message_type: Any | None = Field(default=None)
    message_control_id: Any | None = Field(default=None)
    processing_id: Any | None = Field(default=None)
    version_id: Any | None = Field(default=None)
    sequence_number: Any | None = Field(default=None)
    continuation_pointer: Any | None = Field(default=None)
    accept_acknowledgment_type: Any | None = Field(default=None)
    application_acknowledgment_type: Any | None = Field(default=None)
    country_code: Any | None = Field(default=None)
    character_set: Any | None = Field(default=None)
    principal_language_of_message: Any | None = Field(default=None)
    alternate_character_set_handling_scheme: Any | None = Field(default=None)
