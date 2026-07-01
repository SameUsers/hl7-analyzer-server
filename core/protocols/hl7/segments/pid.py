from typing import Any

from pydantic import Field

from core.protocols.hl7.segments.hl7_segment import HL7Segment


class PID(HL7Segment):
    """
    HL7-сегмент PID (Patient Identification).
    Содержит демографическую информацию о пациенте, включая идентификаторы,
    имя, дату рождения, пол, адрес, контактные данные и другую информацию.
    Attributes:
        set_id: ID набора (PID.1)
        patient_id: ID пациента (PID.2)
        patient_identifier_list: Список идентификаторов пациента (PID.3)
        alternate_patient_id: Альтернативный ID пациента (PID.4)
        patient_name: Имя пациента (PID.5)
        mothers_maiden_name: Девичья фамилия матери (PID.6)
        date_time_of_birth: Дата/время рождения (PID.7)
        administrative_sex: Пол (PID.8)
        patient_alias: Псевдоним пациента (PID.9)
        race: Раса (PID.10)
        patient_address: Адрес пациента (PID.11)
        county_code: Код округа (PID.12)
        phone_number_home: Телефон дом (PID.13)
        phone_number_business: Телефон работа (PID.14)
        primary_language: Основной язык (PID.15)
        marital_status: Семейное положение (PID.16)
        religion: Религия (PID.17)
        patient_account_number: Номер счета (PID.18)
        ssn_number: Номер SSN (PID.19)
        drivers_license_number: Номер прав (PID.20)
        mothers_identifier: Идентификатор матери (PID.21)
        ethnic_group: Этническая группа (PID.22)
        birth_place: Место рождения (PID.23)
        multiple_birth_indicator: Признак многоплодия (PID.24)
        birth_order: Порядок рождения (PID.25)
        citizenship: Гражданство (PID.26)
        veterans_military_status: Военный статус (PID.27)
        nationality: Национальность (PID.28)
        patient_death_date_time: Дата смерти (PID.29)
        patient_death_indicator: Признак смерти (PID.30)
    """

    set_id: Any | None = Field(default=None)
    patient_id: Any | None = Field(default=None)
    patient_identifier_list: Any | None = Field(default=None)
    alternate_patient_id: Any | None = Field(default=None)
    patient_name: Any | None = Field(default=None)
    mothers_maiden_name: Any | None = Field(default=None)
    date_time_of_birth: Any | None = Field(default=None)
    administrative_sex: Any | None = Field(default=None)
    patient_alias: Any | None = Field(default=None)
    race: Any | None = Field(default=None)
    patient_address: Any | None = Field(default=None)
    county_code: Any | None = Field(default=None)
    phone_number_home: Any | None = Field(default=None)
    phone_number_business: Any | None = Field(default=None)
    primary_language: Any | None = Field(default=None)
    marital_status: Any | None = Field(default=None)
    religion: Any | None = Field(default=None)
    patient_account_number: Any | None = Field(default=None)
    ssn_number: Any | None = Field(default=None)
    drivers_license_number: Any | None = Field(default=None)
    mothers_identifier: Any | None = Field(default=None)
    ethnic_group: Any | None = Field(default=None)
    birth_place: Any | None = Field(default=None)
    multiple_birth_indicator: Any | None = Field(default=None)
    birth_order: Any | None = Field(default=None)
    citizenship: Any | None = Field(default=None)
    veterans_military_status: Any | None = Field(default=None)
    nationality: Any | None = Field(default=None)
    patient_death_date_time: Any | None = Field(default=None)
    patient_death_indicator: Any | None = Field(default=None)
