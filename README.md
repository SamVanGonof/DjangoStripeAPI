# Тестовое задание Django+StripeAPI.

### Запуск проекта
### Прежде чем продолжить необходимо зарегистрироваться и авторизоваться на https://stripe.com
Нужно зайти во вкладку - developers - -> API Keys, скопировать Public Key и Secret Key.

1. `git clone `
2. В корневой папке проекта создать файл .env и заполнить его следующим:
   - `SECRET_KEY=<django ключ>`
   - `STRIPE_PUBLIC_KEY=<Publishable key с сайта stripe.com>`
   - `STRIPE_SECRET_KEY=<Secret key с сайта stripe.com>`
3. Запустить docker-compose:
    - `docker-compose up`
4. Сгенерировать миграции и применить их:
    - `./manage.py makemigrations`
    - `./manage.py migrate`
5. Заполнить БД фикстурами:
    - `./manage.py loaddata items.json`
6. Логин/пароль от админки `admin/admin`

### Примеры некоторых запросов API:
 - Получение Stripe Session Id:
```GET /buy/1/```
 - Получение данных своей учетной записи:
```GET /item/3/```

 - Форму для отправки тестового платежа можно заполнять любыми данными, кроме номера карты. Используйте следующие номера карт для тестирования:

 - `4242 4242 4242 4242`
 - `4000 0000 0000 3220`
 - `4000 0000 0000 9995`

Выполнил: Семён Шемагонов
Ноябрь 2022
