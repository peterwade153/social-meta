[![Django CI](https://github.com/peterwade153/social-meta/actions/workflows/django.yml/badge.svg)](https://github.com/peterwade153/social-meta/actions/workflows/django.yml)
# social-meta

Requires Postgres, Redis Installed, and built with Python 3.8 

An account with Abstract API https://www.abstractapi.com/ . 

Use the free API Keys for Email Verification, IP And Holiday APIs

### Installation

1. Create and activate a virtual environment and Clone the project `https://github.com/peterwade153/social-meta.git`

2. Move into the project folder
   ```
   $ cd social-meta
   ```

3. Install dependencies 
   ```
   $ pip install -r requirements.txt
   ```

4. Create a postgres database.

5. Create a `.env` file from the `.env.sample` file. 

6. Replace the variables in the sample file with the actual variables, such the database credentials, secret key etc. 

7. Run migrations
   ```
   python manage.py migrate
   ```


## To Test

1. Start server
   ```
   python manage.py runserver
   ```


2. To run background task to verify emails, ip geolocation
    - start redis server
      ```
      redis-server
      ```
    - start the celery worker 
      ```
      celery -A app worker -l info
      ```

3. The application can be accessed via swagger docs here http://127.0.0.1:8000/

4. To run tests
   ```
   pytest
   ```
5. API Swagger docs usages, follow instructions in Docs.txt file