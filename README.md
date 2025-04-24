# __Geekig__
[![django-version](https://img.shields.io/badge/django-3.2-green)](https://www.djangoproject.com)
[![python-version](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org)
[![postgresql-version](https://img.shields.io/badge/postgresql-12.3-orange)](https://www.postgresql.org)


> _A Django framework project template for quick & easy initialization._

---


# __Usage:__
> _This document will be using the following as an input variable: `<variable>`. Please input your own value, i.e. `<project_name>` --> My-Project_
>
> _Please make sure `git`, `python`, `postgresql` and `rabbitmq` is installed in the system._
>
> _NOTE for Windows users: Please use `Git Bash` for the following steps_


1. ### Install Django and startproject.
    - Clone Repo: https://github.com/doy1354/Geekig.git.
    ```shell script
    cd Geekig
    python3 -m venv venv
    source venv/bin/activate
    # Windows: source venv/Scripts/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

2. ### Create Database and User.
    - Using `psql`, create a `user` with encrypted `password`.
    - Create a `database` for your project.
    - Give privileges to the `user` for the `database`.
    - Alter `user` to allow for `test database` creation.
    ```shell script
    psql -U postgres
    # psql console 
    CREATE USER geekig_user WITH ENCRYPTED PASSWORD '<password>';
    CREATE DATABASE geekig_db;
    GRANT ALL PRIVILEGES ON DATABASE geekig_db TO geekig_user;
    ALTER USER geekig_user CREATEDB;
    \q
    ```

3. ### Configure the project
    - Create folders for `logs`, and `media`.
    - Copy `local_settings.example` to `local_settings.py`.
    - Update `local_settings.py` with proper `settings`, including `database`.
    ```shell script
    mkdir -p logs && mkdir -p media/uploads
    cp examples/local_settings.example Accounting/local_settings.py
    
    nano Accounting/local_settings.py
    # edit local_settings.py
    DB_NAME = 'geekig_db'
    DB_USER = 'geekig_user'
    DB_PASS = '<password>'
    ```

4. ### Run the project
    - Run `makemigrations` and `migrate`.
    - Run `tests` and `linting` to assure nothing is broken.
    - Create superuser to access the admin panel.
    - Run django `server` to view the project or application.
    - Generate `coverage` reports locally.
    ```shell script
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

    ```
   > _NOTE: Browse to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the site. Admin site is at url [/manage](http://127.0.0.1:8000/manage) changed from default to keep the project secure. Admin url can be changed in `settings.py` --> `ADMIN_URL`_

5. ### Dependency
    - Login with superuser `http://localhost:8000/manage/socialaccount/socialapp/`.
    ![image](https://github.com/user-attachments/assets/6f3efca4-e9c7-49d2-8602-26463348a04e)
