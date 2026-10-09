# Taxi Service — Django

Я разработал веб-приложение службы такси на Django: модели автомобилей, водителей и заказов, страницы просмотра и административный интерфейс.

## Запуск

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Устройство проекта

Приложение `taxi/`, настройки `taxi_project/`, HTML-шаблоны и миграции. Ключ приложения задайте через переменную `SECRET_KEY`; база создаётся локально. Загруженные фотографии и локальная база не включены.

Я публикую исходный код без локальных паролей, окружений, баз и журналов. Для воспроизведения анализа я указываю необходимые данные и зависимости.

## Автор

Антон Никитин — [anton-nikitin21](https://github.com/anton-nikitin21).
