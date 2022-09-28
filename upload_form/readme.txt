Basic usage:

cd upload_form
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

-------- How to remove all data in the DB: ------------- 
1. python manage.py flush
2. clear up python cache manually
3. Discard current schema: rm db.sqlite3
4. Run migrations again: python manage.py migrate
