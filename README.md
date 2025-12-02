# FastAPI DDD Clean Architecture

> A pure DDD-like structure for a FastAPI project. Use is allowed for everyone's delight, developer needs.

## Описание

Этот проект представляет собой чистую архитектуру на основе Domain-Driven Design (DDD) для FastAPI приложений. Структура организована таким образом, чтобы обеспечить разделение ответственности, тестируемость и масштабируемость.

## Архитектура

Проект следует принципам Clean Architecture и DDD:

```
api/
├── domain/          # Доменный слой (бизнес-логика)
│   └── example/
│       ├── entities/      # Сущности домена
│       ├── exceptions/    # Доменные исключения
│       ├── repositories/  # Интерфейсы репозиториев
│       └── services/      # Доменные сервисы
│
├── infrastructure/  # Инфраструктурный слой
│   ├── clients/          # HTTP клиенты
│   ├── database/          # Работа с БД
│   ├── dependencies/      # Dependency Injection
│   └── interfaces/        # Интерфейсы
│
├── presentation/    # Слой представления (API)
│   └── example/
│       ├── models/        # Pydantic модели
│       └── router/        # FastAPI роутеры
│
└── general/         # Общие утилиты
    ├── enums.py
    └── utils.py
```

## Быстрый старт

### Требования

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (рекомендуется) или pip

### Установка

```bash
git clone <repository-url>
cd fastapi-ddd-clean

# Установите зависимости (с uv)
uv sync
```

### Запуск

```bash
# С помощью uv
uv run --env-file=.env main.py
```

Приложение будет доступно по адресу: `http://localhost:8000`

### Docker

```bash
docker-compose up --build
```

## Технологии

- **FastAPI** - современный веб-фреймворк
- **Pydantic** - валидация данных
- **Dishka** - Dependency Injection контейнер
- **AsyncPG** - асинхронный драйвер PostgreSQL
- **HTTPX** - асинхронный HTTP клиент
- **Loguru** - логирование
- **Uvicorn** - ASGI сервер

## Основные принципы

- **Разделение ответственности** - каждый слой имеет четко определенную роль
- **Независимость от фреймворков** - бизнес-логика не зависит от FastAPI
- **Тестируемость** - легко писать unit и интеграционные тесты
- **Масштабируемость** - структура поддерживает рост проекта


## Вклад

Проект находится в общественном достоянии. Используйте, модифицируйте и распространяйте свободно.
