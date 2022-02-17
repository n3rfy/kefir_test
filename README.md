Тестовое задание на позицию Python Junior Backend разработчик


<br>Установка:
<br>1)Склонировать репозиторий
<br>2)Отредактировать файл docker-compose.yml
  <br>&nbsp;-Изменить переменные:
    <br>&nbsp;&nbsp;1)Если нужно, то поменять все, что связано с бд DATABASE_URL, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB
    <br>&nbsp;&nbsp;2)Если нужно, то поменять JWT_SECRET, который шифрует токен куки
  <br>&nbsp;-Если нужно, то поменять порты</pre>
  <br>&nbsp;-Ecли нужно, то поменять или добавить пароль стартового юзера (подробее в п5)</pre>
<br>3)Cоздать и запустить образ docker image командой: docker-compose up -build
<br>4)После старта всех контейнеров можно переходить на localhost
<br>5)При создании проекта для удобства сразу будет доступен пользователь, 
<br>&nbsp;email - admin@admin.com и password - задается в файле src/core/settings.py или же в переменной окружения (Поумолчанию admin)
<br>6)Так как я писал api на fastapi, то он сразу предоставляет документацию по адресу http://localhost:8000/docs
<br>
<br>Сначала хочу рассказать, в чем отличие моего api от нужного тестого:
<br>&nbsp;-Убрал login, и заменил аунтификацию на email (Немного пожалел, потому что после изменения данных приходиться релогиниться)
<br>&nbsp;-Добавил создание и удаление сity, потому что никак нельзя было расширять или редактировать города
<br>&nbsp;-Убрал pk в запросе patch /user/, потому что смысла в нем нет, тк user может менять лишь свои данные, следовательно pk - бесполезен

<br>Описание:
<br>1)auth
<br>&nbsp;-login:
<br>&nbsp;&nbsp;-Делал, как было в тестовом задании, логин через cookies, хотя можно было бы через JWT.
<br>&nbsp;&nbsp;По факту, я в куки и клал JWT, дальше каждый запрос расшифровывал его
<br>&nbsp;&nbsp;-Отличие от тестого задания, аунтификация по email и password
<br>&nbsp;-logout:
<br>&nbsp;&nbsp;-Просто удаляет cookies и возвращает пользователя
<br>2)user
<br>&nbsp;"Имеет доступ на уровне пользователя"
<br>&nbsp;Перед каждым запросом проверяет на аунтифицированного пользователя
<br>&nbsp;-users/current:
<br>&nbsp;&nbsp;-Возвращает информацию о текущем пользователе, берет email из куки и уже в бд ищет всю информацию о пользователе
<br>&nbsp;-users (get):
<br>&nbsp;&nbsp;-Получает краткую информацию о всех пользователях (в отличии от admin, тут не возвращаются city)
<br>&nbsp;&nbsp;-page - неотрицательный, size - от 1 и до 10 
<br>&nbsp;-users (patch):
<br>&nbsp;&nbsp;-Отличие от тестого задания в том, что я не использую pk, тк у пользователя есть куки, и в них храниться информация о самом пользователе, тот pk - не нужен
<br>&nbsp;&nbsp;-Так как, email хранится в cookies, и его могут поменять, то приходиться удалять куки, чтобы не было ошибок
<br>3)admin
<br>&nbsp;"Имеет максимальную привелегию и доступ"
<br>&nbsp;Перед каждым запросом проверяет на is_admin
<br>&nbsp;-private/users/ (get):
<br>&nbsp;&nbsp;-Возвращает краткую информацию о всех пользователях (в отличии от user, возвращает city)
<br>&nbsp;&nbsp;-page - только положительный, size - от 1 и до 10 
<br>&nbsp;-private/users/ (create):
<br>&nbsp;&nbsp;-Если хотите привязать к user город, то сначала нужно создать данный город
<br>&nbsp;&nbsp;-Добавление пользователя, проверки на города и на повторение email
<br>&nbsp;-private/user/{pk} (get):
<br>&nbsp;&nbsp;-Получает полную информацию о текущем пользователе, в том числе и city, и additional_info
<br>&nbsp;-private/users/{pk} (delete):
<br>&nbsp;&nbsp;-Удаляет выбранного пользователя, если нет, то 404 error
<br>&nbsp;-private/users/{pk} (patch):
<br>&nbsp;&nbsp;-Обновление информации выбранного пользователя
<br>&nbsp;-private/city/{pk} (post):
<br>&nbsp;&nbsp;-Добавление нового города, если город уже создан, то 400 error
<br>&nbsp;-private/city/{pk} (delete):
<br>&nbsp;&nbsp;-Удаление выбранного города, если город привязан к какому-то пользователю, то удаление не произойдет
  
