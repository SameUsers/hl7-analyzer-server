# Labaratory

Сервер для приема, обработки и сохранения результатов лабораторных анализов от медицинских анализаторов по протоколу HL7.

[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 🚀 Возможности

- **Прием данных** по TCP-протоколу от медицинских анализаторов
- **Поддержка HL7** формата сообщений (версия 2.x)
- **Автоматическое определение** типа анализатора по IP-адресу
- **Парсинг и валидация** лабораторных результатов
- **Сохранение** результатов в структурированном JSON-формате
- **Поддержка** нескольких типов анализаторов:
  - Accent M320 (биохимия)
  - Vet 5160 (гематология)
  - Seamaty SMT-120VP (многоканальный анализатор)

## 📦 Установка

### Требования

- Python 3.12 или выше
- pip или uv

### Установка через uv (рекомендуется)

```bash
# Установка uv (если еще не установлен)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Клонирование репозитория
git clone https://github.com/yourusername/labaratory.git
cd labaratory

# Установка зависимостей
uv sync
```

### Установка через pip

```bash
# Клонирование репозитория
git clone https://github.com/yourusername/labaratory.git
cd labaratory

# Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows

# Установка зависимостей
pip install -e .
```

## 🏃 Запуск

### Разработка

```bash
python main.py
```

### Production

```bash
uvicorn main:app --host 0.0.0.0 --port 8001
```

## 🏗️ Архитектура

```
┌─────────────────────────────────────────────────────────────┐
│                         TCP Server                         │
│                   (core/infrastructure/tcp)                │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                      Handler Factory                       │
│              (core/application/factories)                  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    Analyzer Handler                        │
│              (core/application/handlers)                   │
└────────────────────────┬────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
┌─────────────────┐ ┌──────────────┐ ┌──────────────────┐
│  HL7 Framer     │ │  HL7 Parser  │ │    Builder       │
│ (core/protocols)│ │(core/protocols)│ │  (core/devices)  │
└─────────────────┘ └──────────────┘ └──────────────────┘
                                                          │
                                                          ▼
                                          ┌─────────────────────────┐
                                          │   Storage (SaveToJson)  │
                                          │  (core/infrastructure)  │
                                          └─────────────────────────┘
```

### Компоненты

| Компонент | Описание |
|-----------|----------|
| **TCP Server** | Принимает входящие TCP-соединения от анализаторов |
| **Handler Factory** | Создает обработчики на основе IP-адреса клиента |
| **Analyzer Handler** | Управляет полным циклом обработки данных |
| **HL7 Framer** | Выделяет HL7-сообщения из байтового потока |
| **HL7 Parser** | Разбирает HL7-сообщения на сегменты |
| **Builder** | Преобразует HL7-данные в структурированный результат |
| **Storage** | Сохраняет результаты в JSON-файлы |

## 📁 Структура проекта

```
labaratory/
├── core/
│   ├── application/          # Прикладной слой
│   │   ├── factories/        # Фабрики для создания компонентов
│   │   └── handlers/         # Обработчики данных
│   ├── contracts/            # Интерфейсы и абстрактные классы
│   ├── devices/              # Реализации для конкретных анализаторов
│   │   ├── accent_m320/      # Accent M320
│   │   ├── seamaty_smt/      # Seamaty SMT-120VP
│   │   └── vet_5160/         # Vet 5160
│   ├── infrastructure/       # Инфраструктурный слой
│   │   ├── storage/          # Хранилище данных
│   │   └── tcp/              # TCP-сервер и буфер
│   ├── protocols/            # Реализации протоколов
│   │   └── hl7/              # HL7 протокол
│   ├── schemas/              # Pydantic схемы данных
│   └── shared/               # Общие утилиты
├── Analyze/                  # Директория с результатами (создается автоматически)
├── main.py                   # Точка входа
├── pyproject.toml           # Конфигурация проекта
└── README.md                # Этот файл
```

## 🔧 Конфигурация

### Добавление нового анализатора

1. Создайте директорию в `core/devices/`:
```bash
core/devices/new_analyzer/
```

2. Создайте билдер:
```python
# core/devices/new_analyzer/builder.py
from core.contracts.builder import BuilderInterface
from core.protocols.hl7.message import HL7Message

class NewAnalyzerBuilder(BuilderInterface):
    def build_analyze(self, message: HL7Message) -> AnalyzeResult:
        # Логика парсинга
        pass
```

3. Добавьте схему данных:
```python
# core/devices/new_analyzer/schema.py
from pydantic import BaseModel

class NewAnalyzerResult(BaseModel):
    # Поля результата
    pass
```

4. Зарегистрируйте анализатор в `core/devices/registry.py`:
```python
DEVICE_REGISTRY = {
    # ...
    "192.168.1.100": DeviceProfile(
        protocol=HL7_V1,
        builder=NewAnalyzerBuilder,
    ),
}
```

## 📊 Формат сохранения

Результаты сохраняются в структурированном виде:

```
Analyze/
└── {analyzer_type}/
    └── {YYYY-MM-DD}/
        └── {YYYY-MM-DD-SS}-{analyzer_type}.json
```

Пример:
```json
{
  "analyzer_name": "AccentM320",
  "result": {
    "analyze_type": "BAC",
    "ALAT IIGEN": 25.5,
    "GLUC": "5.6",
    "CHOL": "4.2"
  }
}
```

## 🧪 Тестирование

```bash
# Запуск всех тестов
pytest

# Запуск с покрытием
pytest --cov=core tests/
```

## 📝 Логирование

Проект использует `loguru` для логирования. Логи выводятся в консоль с уровнем DEBUG и ERROR.

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для вашей фичи (`git checkout -b feature/amazing-feature`)
3. Зафиксируйте изменения (`git commit -m 'Add some amazing feature'`)
4. Отправьте изменения в вашу ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. Подробности в файле [LICENSE](LICENSE).

## 📞 Контакты

- Автор: [Ваше имя]
- Email: [ваш email]

## 🙏 Благодарности

- [Pydantic](https://github.com/pydantic/pydantic) - валидация данных
- [Loguru](https://github.com/Delgan/loguru) - логирование
- [uv](https://github.com/astral-sh/uv) - управление зависимостями