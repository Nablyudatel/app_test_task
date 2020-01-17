#### Текст задания

Задача: реализовать API, позволяющее добавлять, изменять, просматривать и удалять данные в модели "Приложения".
"Приложения" – это модель, которая хранит в себе внешние источники, которые будут обращаться к API. Обязательные поля модели: ID, Название приложения, Ключ API. Поле "Ключ API" нельзя менять через API напрямую, должен быть метод, позволяющий создать новый ключ API.
После добавления приложения – должна быть возможность использовать "Ключ API" созданного приложения для осуществления запросов к метод /api/test, метод должен возвращать JSON, содержащий всю информацию о приложении.

-----------------------------------------------------------------------



*Чтобы запустить проект необходимо:*
* Клонировать репозиторий: git clone https://github.com/Nablyudatel/app_test_task.git
* Или просто скачать архив.
* Установить зависимости, если их нет (django, djangorestframework), об этом ниже.
* Из терминала в папке с проектом выполнить: `python manage.py runserver`


*Установка зависимостей:*
* Зайти через терминал зайти в папку с проектом
* Выполнить команду: `pip install -r requirements.txt`

-----------------------------------------------------------------------

* http://127.0.0.1:8000/api/v1/apps/  - это список объектов
* http://127.0.0.1:8000/api/v1/apps/test/api_key_7Kb5ncQcH4tmPjK7y0BXlJf2PqZMcx3s4OqrFad38pQ/ - Просмотр объекта по полю api_key