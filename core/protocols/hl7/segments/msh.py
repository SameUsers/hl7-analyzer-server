from typing import Any, Optional

from pydantic import Field

from core.protocols.hl7.segments.hl7_segment import HL7Segment


class MSH(HL7Segment):
    """
    HL7-сегмент MSH (Message Header).

    Содержит заголовочную информацию сообщения, включая тип сообщения,
    отправителя, получателя, временные метки и другие метаданные.

    Этот сегмент является обязательным для всех HL7-сообщений.

    Поля соответствуют стандарту HL7 версии 2.x:
    - MSH.1  - Поле-разделитель
    - MSH.2  - Кодирующие символы
    - MSH.3  - Приложение-отправитель
    - MSH.4  - Учреждение-отправитель
    - MSH.5  - Приложение-получатель
    - MSH.6  - Учреждение-получатель
    - MSH.7  - Дата/время сообщения
    - MSH.8  - Безопасность
    - MSH.9  - Тип сообщения
    - MSH.10 - Идентификатор управления сообщением
    - MSH.11 - Идентификатор обработки
    - MSH.12 - Версия HL7
    - MSH.13 - Номер последовательности
    - MSH.14 - Указатель продолжения
    - MSH.15 - Тип подтверждения приема
    - MSH.16 - Тип подтверждения приложения
    - MSH.17 - Код страны
    - MSH.18 - Набор символов
    - MSH.19 - Основной язык сообщения
    - MSH.20 - Схема обработки альтернативного набора символов

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

    field_separator: Optional[Any] = Field(default=None)
    encoding_characters: Optional[Any] = Field(default=None)
    sending_application: Optional[Any] = Field(default=None)
    sending_facility: Optional[Any] = Field(default=None)
    receiving_application: Optional[Any] = Field(default=None)
    receiving_facility: Optional[Any] = Field(default=None)
    date_time_of_message: Optional[Any] = Field(default=None)
    security: Optional[Any] = Field(default=None)
    message_type: Optional[Any] = Field(default=None)
    message_control_id: Optional[Any] = Field(default=None)
    processing_id: Optional[Any] = Field(default=None)
    version_id: Optional[Any] = Field(default=None)
    sequence_number: Optional[Any] = Field(default=None)
    continuation_pointer: Optional[Any] = Field(default=None)
    accept_acknowledgment_type: Optional[Any] = Field(default=None)
    application_acknowledgment_type: Optional[Any] = Field(default=None)
    country_code: Optional[Any] = Field(default=None)
    character_set: Optional[Any] = Field(default=None)
    principal_language_of_message: Optional[Any] = Field(default=None)
    alternate_character_set_handling_scheme: Optional[Any] = Field(default=None)