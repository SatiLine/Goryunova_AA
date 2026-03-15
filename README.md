# Лабораторная работа 3
# Введение в FastAPI

1. Подготовительный этап: создание проекта и первого коммита
    1. Создайте новую директорию для проекта, назовите ее вашей фамилией с вашими инициалами и перейдите в неё
    ![alt text](image.png)
    2. Инициализируйте git-репозиторий командой git init
    ![alt text](image-1.png)
    3. Создайте файл .gitignore и добавьте в него стандартные исключения для Python проектов (можно использовать шаблон с https://github.com/github/gitignore/blob/main/Python.gitignore)
    ![alt text](image-2.png)
    ![alt text](image-3.png)
    4. Инициализируйте проект при помощи uv командой uv init
    ![alt text](image-4.png)
    5. С помощью uv создайте виртуальное окружение и установите FastAPI и Uvicorn
    ![alt text](image-5.png)
    ![alt text](image-6.png)

    Проверьте файл pyproject.toml, список dependencies.
    ![alt text](image-7.png)

    Проверьте файл uv.lock.
    ![alt text](image-8.png)
    Проверьте файл python-version.
    ![alt text](image-9.png)
    6. Создайте файл main.py с минимальным приложением FastAPI
    ![alt text](image-10.png)
    7. Запустите приложение
    ![alt text](image-11.png)
    8. Откройте http://127.0.0.1:8000 – вы должны увидеть JSON-ответ
    ![alt text](image-12.png)
    Откройте http://127.0.0.1:8000/docs – вы должны увидеть OpenAPI документацию.
    ![alt text](image-13.png)
    Откройте http://127.0.0.1:8000/redoc – вы должны увидеть Redoc документацию.
    ![alt text](image-14.png)
    9. Сделайте первый коммит
    ![alt text](image-15.png)

2. Добавление нового эндпоинта с параметрами пути и query
    1. В файл main.py добавьте новый эндпоинт /items/{item_id}, который принимает: обязательный параметр пути item_id (целое число); необязательный query-параметр q (строка) со значением по умолчанию None. Функция должна возвращать словарь с полученными значениями.
    ![alt text](image-16.png)
    2. Запустите приложение
    ![alt text](image-17.png)
    3. Перейдите в браузере по адресу http://127.0.0.1:8000/items/42?q=test
    ![alt text](image-18.png)
    4. Перейдите по адресу http://127.0.0.1:8000/docs
       Нажмите “try it out” и протестируйте работу эндпоинта там.
    ![alt text](image-21.png)
    5. Сделайте коммит:
    ![alt text](image-22.png)

3. Создание модели Pydantic и обработка POST-запроса
    1. Установите pydantic.
    ![alt text](image-23.png)
    Проверьте файл pyproject.toml, список dependencies, там должен появиться pydantic
    ![alt text](image-24.png)   
    2. В файле main.py импортируйте BaseModel из pydantic и определите модель Item
    ![alt text](image-25.png)
    3. Добавьте новый эндпоинт для создания товара (метод POST) по пути /items/, который принимает объект Item и возвращает его же (имитируем сохранения, мы специально возвращаем созданный объект, чтобы отправляющий запрос мог убедиться, что все правильно).
    ![alt text](image-26.png)
    4. Проверьте работоспособность эндпоинта (например, через /docs)
    ![alt text](image-27.png)
    ![alt text](image-28.png)
    5. Сделайте коммит
    ![alt text](image-29.png)

4. Организация кода: вынос маршрутов в отдельные роутеры
    1. Создайте директорию app и внутри неё файл routers/items.py
    ![alt text](image-30.png)
    ![alt text](image-31.png)
    ![alt text](image-32.png)
    ![alt text](image-33.png)
    ![alt text](image-34.png)
    ![alt text](image-35.png)
    2. Перенесите все эндпоинты, связанные с товарами (GET /items/{item_id}, POST /items/), в файл app/routers/items.py, используя APIRouter
    ![alt text](image-36.png)
    3. В основном файле main.py подключите роутер
    ![alt text](image-37.png)
    4. Убедитесь, что приложение по-прежнему работает (маршруты доступны по тем же адресам).
    ![alt text](image-38.png)
    5. Сделайте коммит
    ![alt text](image-39.png)

5. Добавление конфигурации через Pydantic Settings
    1. Установите pydantic-settings
    ![alt text](image-40.png)
    2. Создайте файл app/config.py с классом настроек
    ![alt text](image-41.png)
    3. В корне проекта создайте файл .env с содержимым
    ![alt text](image-42.png)
    4. В main.py создайте экземпляр настроек и передайте title в FastAPI
    ![alt text](image-43.png)
    5. Добавьте эндпоинт, который возвращает информацию о настройках (например, /info)
    ![alt text](image-44.png)
    6. Проверьте, что значение items_per_page подхватилось из .env (должно быть 20)
    ![alt text](image-45.png)
    7. Сделайте коммит
    ![alt text](image-46.png)

6.  Обработка ошибок и улучшение документации
    1. Модифицируйте эндпоинт GET /items/{item_id} так, чтобы он имитировал поиск товара в базе данных. Для простоты создайте словарь-заглушку внутри функции или на уровне модуля. Если товар с указанным item_id не найден – вызывайте HTTPException с кодом 404.
    ![alt text](image-47.png)

    У меня в БД находится только 1 объект.  
    Проверяю работу эндпоинта:  
    1 объект:

    http://127.0.0.1:8000/items/1
    ![alt text](image-48.png)

    99 объект:  
    http://127.0.0.1:8000/items/99
    ![alt text](image-49.png)

    2. Добавьте описание для эндпоинтов и параметров, используя аннотации и встроенные классы Path, Query
    ![alt text](image-50.png)
    3. Для модели Item добавьте примеры и описания полей через Field
    ![alt text](image-51.png)
    4. В основной app (в main.py) укажите общие метаданные: description, version, contact и т.п.
    ![alt text](image-52.png)
    5. Запустите приложение и откройте /docs. Убедитесь, что появились все описания, примеры, а при запросе несуществующего товара возвращается 404.
    ![alt text](image-53.png)
    ![alt text](image-54.png)
    ![alt text](image-55.png)
    ![alt text](image-56.png)
    ![alt text](image-57.png)
    6. Сделайте коммит
    ![alt text](image-58.png)

7. Самостоятельная работа
    1. Добавьте эндпоинт для обновления товара (PUT /items/{item_id}) с проверкой существования
    ![alt text](image-59.png)
    ![alt text](image-60.png)
    ![alt text](image-61.png)
    ![alt text](image-62.png)
    ![alt text](image-63.png)
    ![alt text](image-64.png)
    2. Реализуйте валидацию на уникальность имени товара
    ![alt text](image-65.png)
    ![alt text](image-66.png)
    ![alt text](image-67.png)
    ![alt text](image-68.png)
    ![alt text](image-69.png)
    3. Сделайте коммит с нужным префиксом и сообщением
    ![alt text](image-70.png)

8. Самостоятельная работа
    1. Добавьте логирование (можно использовать стандартную библиотеку logging, можно установить внешнюю библиотеку loguru)
    ![alt text](image-71.png)
    ![alt text](image-72.png)
    2. Сделайте коммит с нужным префиксом и сообщением
    ![alt text](image-73.png)