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