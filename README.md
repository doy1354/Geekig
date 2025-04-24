# __Django Kick start__
[![django-version](https://img.shields.io/badge/django-3.2-green)](https://www.djangoproject.com)
[![python-version](https://img.shields.io/badge/python-3.8-blue)](https://www.python.org)
[![postgresql-version](https://img.shields.io/badge/postgresql-12.3-orange)](https://www.postgresql.org)


> _A Django framework project template for quick & easy initialization._

---

## **Key Features**

- **User Model with Profile**: Utilizes email addresses as usernames for seamless authentication and user management.  
- **Environment-Specific Settings**: Separate configurations for development and production environments to ensure secure and efficient deployment.  
- **Logging System**: Comprehensive logging enabled with daily log rotation at midnight. Log entries are accessible via Django Admin and can be reused throughout the application.  
- **Data Import/Export**: Integrated `import_export` plugin for seamless data handling in various formats, including CSV, XLS, XLSX, and JSON.  
- **Django REST Framework (DRF)**: Built-in API endpoints and view sets for creating robust RESTful APIs.  
- **Cross-Origin Resource Sharing (CORS)**: Enabled via `Django-Cors-Headers` to facilitate secure and efficient API interactions across domains.  
- **Dynamic Query Filtering**: Utilizes `Django-filter` to enable dynamic queryset filtering based on URL parameters.  
- **Automatic File Cleanup**: Integrated `Django-cleanup` to automatically remove unused or unlinked files and images, ensuring optimal storage management.  
- **Celery Integration**: Supports asynchronous task processing using RabbitMQ (Redis is also supported as an alternative).  
- **Test-Driven Development (TDD)**: All code is developed following TDD principles to ensure reliability and maintainability.  
- **Testing and Code Quality**:  
  - Test coverage analysis using `coverage`.  
  - Code linting with `flake8` to enforce coding standards.  
- **Continuous Integration/Continuous Deployment (CI/CD)**:  
  - GitHub Actions for automated CI workflows.  
  - Jenkins CI/CD pipelines with Docker support for scalable and reproducible deployments.  
- **Monitoring and Metrics**: Integrated Prometheus for real-time monitoring of application performance, including model and middleware metrics.  

---

## Demo  
<img src="https://github.com/user-attachments/assets/a3ba47a0-d61b-42a5-86f0-067ddc73835b" width="400" />
<img src="https://github.com/user-attachments/assets/32e91cb1-921a-4568-bd74-334ae9cf664a" width="400" />
<img src="https://github.com/user-attachments/assets/057acaf4-3b02-4e05-9363-439b6872efc4" width="400" />
<img src="https://github.com/user-attachments/assets/738a3bd3-3d37-49d1-8e0b-e3d01edb0ed6" width="400" />
<img src="https://github.com/user-attachments/assets/e4468def-618b-454a-80a3-06d23f0fa49c" width="400" />



# __Usage:__
> _This document will be using the following as an input variable: `<variable>`. Please input your own value, i.e. `<project_name>` --> My-Project_
>
> _Please make sure `git`, `python`, `postgresql` and `rabbitmq` is installed in the system._
>
> _NOTE for Windows users: Please use `Git Bash` for the following steps_

1. ### Prepare project directory
    - Make your project directory (must be the same name as your github repository name)
    - Work from the project directory as current directory using `cd`.
    - Create a virtual environment using `python`. (Test via `python -V`. Must be python 3.6+)
    - `Activate` the virtual environment. (Windows: `source venv/Scripts/activate`)
    - Install `Django` using `pip`.
    ```shell script
    mkdir <project_name> && cd $_
    python3 -m venv venv
    source venv/bin/activate
    # Windows: source venv/Scripts/activate
    python -m pip install --upgrade pip
    ```

2. ### Install Django and startproject.
    - Install `Django` v3 using `pip` within your `venv`
    - Download the __[DjangoKickstart.zip](https://github.com/Rayhun/DjangoKickstart/archive/refs/heads/main.zip)__. _(Please save as template.zip in your project directory)_
    - Start your project using `django-admin` and the template.
    ```shell script
    pip install django
    # download the DjangoKickstart-main.zip linked above
    django-admin startproject \
        --template DjangoKickstart-main.zip \
        --extension py,md,yml,example \
        --name Dockerfile,Jenkinsfile \
        <project_name> .
    pip install -r requirements.txt
    rm -f DjangoKickstart-main.zip
    ```
    > _NOTE: `<project_name>` must be the exact same name as your project repository name. The period `.` at the end of `django-admin` starts the project in the current directory._

3. ### Create Database and User.
    - Using `psql`, create a `user` with encrypted `password`.
    - Create a `database` for your project.
    - Give privileges to the `user` for the `database`.
    - Alter `user` to allow for `test database` creation.
    ```shell script
    psql -U postgres
    # psql console 
    CREATE USER <project_name>_user WITH ENCRYPTED PASSWORD '<password>';
    CREATE DATABASE <project_name>_db;
    GRANT ALL PRIVILEGES ON DATABASE <project_name>_db TO <project_name>_user;
    ALTER USER <project_name>_user CREATEDB;
    \q
    ```

4. ### Configure the project
    - Create folders for `logs`, and `media`.
    - Copy `local_settings.example` to `local_settings.py`.
    - Update `local_settings.py` with proper `settings`, including `database`.
    ```shell script
    mkdir -p logs && mkdir -p media/uploads
    cp examples/local_settings.example <project_name>/local_settings.py
    
    nano <project_name>/local_settings.py
    # edit local_settings.py
    DB_NAME = '<project_name>_db'
    DB_USER = '<project_name>_user'
    DB_PASS = '<password>'
    ```

5. ### Run the project
    - Run `makemigrations` and `migrate`.
    - Run `tests` and `linting` to assure nothing is broken.
    - Create superuser to access the admin panel.
    - Run django `server` to view the project or application.
    - Generate `coverage` reports locally.
    ```shell script
    python manage.py makemigrations
    python manage.py migrate
    python manage.py test && flake8
    python manage.py createsuperuser
    python manage.py runserver
    
    # coverage reports
    coverage run manage.py test
    coverage xml -o coverage.xml
    coverage report
    ```
   > _NOTE: Browse to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the site. Admin site is at url [/manage](http://127.0.0.1:8000/manage) changed from default to keep the project secure. Admin url can be changed in `settings.py` --> `ADMIN_URL`_

6. ### Git setup with actions
    - Setup GitHub actions workflow.
    - `Initialize` your project with `git`.
    - Make first `commit`.
    - Add to remote `git` link.
    - `Push` your project to `git`.
    - Make `release` branch and `push`.
    ```shell script
    # setup actions workflow
    mkdir -p .github/workflows
    cp examples/github_ci.example .github/workflows/github_ci.yml
    
    # setup github
    git init
    git add .
    git commit -m "initialize project"
    git branch -M main
    git remote add origin git@github.com:rayhun/<project_name>.git
    git push -u origin main
    
    # setup release branch
    git checkout -b release
    git push -u origin release
    git checkout main  # back to dev branch, happy coding!
    ```
    ### File Structure
    ```
    API/
        migrations/
        models/
        serializers/
        tests/
        views/
        __init__.py
        apps.py
        urls.py
    Core/
        admin.py
        apps.py
        forms/
        management/
        migrations/
        models/
        tasks.py
        tests/
        urls.py
        views/
    docker-compose.yml
    Dockerfile
    examples/
        celery-beat.example
        celery-worker.example
        daphne.example
        ...
    logs/
    .coveragerc
    .flake8
    .gitignore
    manage.py
    project_name/
    README.md
    requirements.txt
    scripts/
    site_settings/
    staticfiles/
    templates/
    utils.py
    ```
