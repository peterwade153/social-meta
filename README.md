# social-meta

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

6. Replace the variables in the sample file with the actual variables, such the database credentials and secret key. 

7. Run migrations
   ```
   python manage.py migrate
   ```

8. To start server
   ```
   python manage.py runserver
   ```

8. To run tests
   ```
   pytest
