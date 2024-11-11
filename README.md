### ClothingStore

Интерактивное веб-приложение для интернет-магазина одежды, созданное с использованием Django и PostgreSQL.

## Как запустить проект локально

1. Клонируйте репозиторий:

    ```bash
    git clone <URL вашего репозитория>
    cd clothing_store
    ```

2. Создайте виртуальное окружение и установите зависимости:

    **Windows**:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    ```

    **Mac/Linux**:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3. Создайте базу данных PostgreSQL:

    Убедитесь, что PostgreSQL установлен и запущен. Создайте базу данных с именем `clothing-store`:

    ```bash
    createdb clothing-store
    ```

4. Импортируйте данные в базу данных:

    ```bash
    psql -U postgres -d clothing-store < db_dump.sql
    ```

    Пароль для PostgreSQL: 1111


5. Выполните миграции:

    ```bash
    python manage.py migrate
    ```

6. Соберите статические файлы:

    ```bash
    python manage.py collectstatic
    ```

7. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

8. Откройте ваш браузер и перейдите по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).
