# stepbox
Django REST Framework на практике

**Установка**

Установите python 3.9, создайте виртуальное окружение, активируйте его. 

В окружении с помощью pip -r requirements.txt установите пакеты: Django и Django REST framework и др. нужные пакеты.

Выполните миграцию: python manage migrate

Создайте superuser: python manage createsuperuser и измениете его id в БД на 0.

Через консоль выполните первоначальное заполнение БД: python manage import_users, python manage import_items, python manage import_reviews

Проект уже имеет предзаполненную базу данных - суперюзер: admin, пароль: admin.
