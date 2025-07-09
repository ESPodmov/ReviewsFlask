# Установка и настройка проекта

## 1. Создание и активация виртуального окружения

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Применение миграций базы данных
```bash
alembic upgrade head
```

### 4. Запуск
```bash
python app.py
```
