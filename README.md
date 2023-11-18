# API for Telegram

Тестовое задание для Go Global.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/TrokhinMaxim/api_for_tg.git
    cd api_for_tg
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

3. Примените миграции:

    ```bash
    python manage.py migrate
    ```

4. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

## Использование

Проект предоставляет несколько эндпоинтов для взаимодействия:

- `/api/register/` - Регистрация нового пользователя.
- `/api/user/profile/` - Получение профиля пользователя.
- `/api/get_currency/` - Получение текущего курса доллара.
- `/api/history/<int:user_id>/` - Получение истории запросов пользователя.
- `/api/subscribe/` - Подписка на рассылку курса.
- `/api/unsubscribe/` - Отписка от рассылки курса.
- `/api/greeting/` - Получение персонализированного приветствия.
- `/api/currency_template/` - Получение шаблона для курса доллара.
- `/api/user_history_template/<str:user_username>/` - Получение шаблона для истории запросов пользователя.

## Дополнительные настройки

- Вы можете настроить тексты приветствия, шаблонов для курса и истории запросов в админке.


