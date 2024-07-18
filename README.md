pipenv install --dev python-dotenv
pipenv install psycopg2-binary Flask-SQLAlchemy Flask-Migrate

sudo podman build -t notesapp:0.1 .
sudo podman run --privileged --rm -it -v ./migrations:/app/notes/migrations notesapp:0.1 bash 
# must run privileged so that app has appropriate permissions to perform flask db init and to read migrations folder
flask db init
flask db migrate
flask db upgrade

sudo podman exec -i notes_db_container psql -U notes_user -l

psql -h localhost -U notes_user -l

To run, enter `flask run`, optionally followed by host and port, e.g. `flask run --host=0.0.0.0 --port=3000` from the `notes` directory

to run with a gunicorn (a production-grade server), move one directory up and run `gunicorn -b 0.0.0.0:5000 "notes:create_app()"`