# Проект Django-приложение "Образовательные модули с поисковиком для учебного материала"

Разработано приложение для образовательной онлайн-школы с подключением backend- и frontend-части.

Backend-часть разработана с помощью Django DRF.
Frontend-часть разработана с помощью React.

Проект использует Poetry для управления зависимостями и средой виртуализации Python.

Стек: Django, DRF, CORS, Celery, unittest, flake8, Docker, PostgreSQL, Elasticsearch, React


## В приложении реализована:

1. Аутентификация и авторизация пользователей.
2. Реализован CRUD для работы с пользователем.
3. Созданы и разграничены права.(Пользователи могут редактировать только свой профиль и 
просматривать купленные курсы. Не могут просматривать 
подробную информацию о других пользователях и не купленных уроках. 
Только персонал может создавать, удалять, редактировать курсы, модули, уроки и платежи.
4. CRUD для работы с курсами и уроками.
5. Настроена токенизация.
6. Покупка курсов через Stripe.
7. Создание и удаление подписки на курс (подписка возможна только после покупки курса).
8. Оповещение об изменении материала курса (письмо на почту, асинхронная рассылка).
9. Блокировка пользователей, которые не входили на сервис более 4 месяца.
10. Настроена CORS.
11. CRUD для работы с текстами документов.
12. Подключен поиск по пользовательскому запросу по тестам документов через подключение Elasticsearch. 
В случае удачного запроса пользователю выводится первые 20 текстовых документов с точным совпадение по поисковому слову, в случае
неудачного запроса пользователь получит уведомление, что точных совпадений нет. 
13. Реализована frontend часть визуализации всего проекта с подключением React.
14. Frontend часть представляет собой красивую стартовую страницу, в которой содержится информация о курсах и видеоуроки.
В заголовке главной страницы есть кнопки:
- Поисковик - переход на страницу с поисковиком учебных материалов.
- Мои курсы - переход на страницу с оплаченными пользователем курсами.
- Мой профиль - переход на страницу с информацией о пользователе.
- На главную - возвращение на стартовую страницу
- Войти/выйти - авторизация.
15. Проект покрыт автоматизированными тестами c подключением unitest. Процент покрытия тестами - 94%.
16. Проект завернут в Docker.
17. Описана документация для проекта.

## Запуск проекта:

1. Установите Docker и Docker Compose

2. Настройте файл .env.docker:

Заполните файл .env.sample своими данными и переименуйте его в .env.docker

3. Запустите Docker Compose:
```
 docker-compose up -d --build
```
4. Создание курсов через веб-страницу или postman:
```
http://localhost:8000/materials/course/create/
```
5. Создание модулей через веб-страницу или postman:
```
http://localhost:8000/materials/modules/create/
```
6. Создание уроков через веб-страницу или postman:
```
http://localhost:8000/materials/lesson/create/
```
7. CRUD для курсов, модулей и уроков реализуется по адресам в соответствии со ссылками, описанными в urls.py.
8. Оплата курса пользователем происходит через подключение тестового режима Stripe. После оплаты
в профиле пользователя будут отображаться оплаченные курсы, где пользователь будет иметь к ним доступ.
9. Реализована автоматическая рассылка сообщений пользователям, которые подписаны на обновления материала курса.
10. Создание текстов через веб-страницу или postman:
```
http://localhost:8000/search_engine/text/create/
```
11. CRUD для текста реализуется по адресам в соответствии со ссылками, описанными в urls.py.
12. Запуск периодических задач:
```
celery -A config worker -l info -P eventlet
celery -A config beat -l info
```
13. Запуск Redis на Windows:
```
cd redis
redis-server
```
На MacOS и Linux-подобных системах redis подключается автоматически.
14. Запуск Elasticsearch:
```
.\elasticsearch-8.12.2-windows-x86_64\elasticsearch-8.12.2\bin>elasticsearch -E xpack.security.enabled=false
```
15. Поиск точного совпадения по пользовательскому запросу:
```
http://127.0.0.1:8000/search_engine/text/search/
```
Ответ приходит в postman в формате json, в терминал в формате str, а также на веб-страницу в формате карточек,
описанных в React с подключением стилей css.


