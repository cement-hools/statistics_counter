# statistics_counter
Микросервис для счетчиков статистики.

<!---
https://github.com/cement-hools/statistics_counter/badge.svg
--->
![example workflow](https://github.com/cement-hools/statistics_counter/actions/workflows/project_test.yml/badge.svg)
### Используется GitHub Actions для автоматического тестирования при изменении кода в репозитории

## stack
- python 3.9
- django
- django REST framework
- PostgreSQL
- Docker-compose

### Описание v1
- **GET**```/api/v1/statistic/``` Показать все записи статистики событий.
```
date - дата события
views - количество показов (опционально)
clicks - количество кликов (опционально)
cost - стоимость кликов (опционально, в рублях с точностью до копеек)
cpc - cost/clicks (средняя стоимость клика)
cpm - cost/views * 1000 (средняя стоимость 1000 показов)
```
Ответ
```
[
    {
        "id": 1,
        "cpc": "1.00",
        "cpm": "2000.00",
        "date": "2021-10-03",
        "views": 1,
        "clicks": 2,
        "cost": "2.00"
    },
    {
        "id": 2,
        "cpc": "0.20",
        "cpm": "78.33",
        "date": "2021-10-02",
        "views": 30,
        "clicks": 12,
        "cost": "2.35"
    }
]
```
**Параметры запроса**
```
Формат даты YYYY-MM-DD
- date: string - вывести статистику по событию за указанную дату
- from_date: string - вывести статистику по событиям начиная с указанной даты
- to_date: string - вывести статистику по событиям по указанную дату
- date_range: string - статистика за период. 
Возможные варианьты:
    today - за сегодняшний день
    yesterday - за вчерашний день
    week - за последние 7 дней
    month - за текущий месяц
    year - за текущий год
- ordering: string - отсортировать события по выбранному полю
    Возможные варианьты:
    id - по возрастанию(id), по убыванию(-id)
    date - по возрастанию(date), по убыванию(-date) 
    views - по возрастанию(views), по убыванию(-views) 
    clicks - по возрастанию(clicks), по убыванию(-clicks) 
    cost - по возрастанию(cost), по убыванию(-cost) 
    cpc - по возрастанию(cpc), по убыванию(-cpc) 
    cpm - по возрастанию(cpm), по убыванию(-cpm) 
```
- **POST**```/api/v1/statistic/``` Добавить событие в БД

**Параметры запроса**
```
{
date*: string($date) - Дата события (required)
views: integer - Количество показов
clicks:	integer - Количество кликов
cost:	string($decimal) - Стоимость кликов
}
```
Ответ
```
{
    "id": 12,
    "date": "2021-10-02",
    "views": 30,
    "clicks": 12,
    "cost": "12.50"
}
```
- **DELETE**```/api/v1/statistic/``` удалить все записи событий из БД
Ответ
```
{
    "status": 204,
    "data": "statistic is cleared"
}
```
### Описание v2
Второй вариант. Поля cpc и cpm вычисляются при добавлении события в БД

Все параметры аналогичны с v1
- **GET**```/api/v2/statistic/``` Показать все записи статистики событий.
- **POST**```/api/v2/statistic/``` Добавить событие в БД
- **DELETE**```/api/v2/statistic/``` удалить все записи событий из БД

## Установка и запуск на сервере разработчика
1. Клонировать репозиторий
    ```
    git clone https://github.com/cement-hools/statistics_counter
    ```
2. Перейдите в директорию statistics_counter
    ```
   cd statistics_counter
    ```
3. Создать виртуальное окружение, активировать и установить зависимости
    ``` 
   python -m venv venv
    ```
   Варианты активации окружения:
   - windows ``` venv/Scripts/activate ```
   - linux ``` venv/bin/activate ```
     <br><br>
   ```
   python -m pip install -U pip
   ```
   ```
   pip install -r requirements.txt
   ```
4. Выполните миграции
   ```
   python manage.py migrate
   ```
5. Создать супер юзера
   ```
   python manage.py createsuperuser
   ```
6. Запустить приложение на сервере разработчика
   ```
   python manage.py runserver
   ```
7. Проект доступен 
   ```
   http://127.0.0.1:8000/
   http://localhost:8000/
   ```

## Тесты
```
python manage.py test
```

## Запуск в трех контейнерах (PostgreSQL, Web, Nginx)

1. Клонировать репозиторий
    ```
    git clone https://github.com/cement-hools/statistics_counter
    ```
2. Перейдите в директорию statistics_counter
    ```
   cd statistics_counter
    ```
3. Запустить docker-compose
    ```
    docker-compose up --build
    ```
4. Зайти в контейнер и выполнить миграции
    ```
    docker-compose exec web python manage.py migrate --noinput
    ```
5. Зайти в контейнер и создать супер юзера.
    ```
    docker-compose exec web python manage.py createsuperuser
    ```
7. Проект доступен 
   ```
   http://127.0.0.1/
   http://localhost/
   ```


