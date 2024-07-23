# About
A python flask application for creating, updating, and deleting markdown notes, including user creation and login/logout functionality

# Running the application
Regardless of your method of running, you'll want to create a `.env` file in the root directory of this project to ensure that you've defined the variables used in the project's `config.py` file. E.g., 

```bash
export DB_NAME='notes'
export DB_USERNAME='postgres'
export DB_PASSWORD='my_awesome_password'
export DB_PORT='5432'
```
etc.

## Running from a container
This project uses podman and podman compose for containerization, a rootless, daemonless alternative to docker. 

`cd` into the project's root directory, then run `podman compose up`. 

Next, in a separate terminal, run `podman exec -it notes_web_1 sh`. Once in the container's shell, run `flask db init`, `flask db migrate` and `flask db upgrade`. Then `exit`.

Finally, navigate to localhost:5000 in a web browser.

### Note on running with docker 
The podman cli is nearly identical to that for docker. Consequently, if you wish to run with docker, substituting `docker` for `podman` in the commands above should suffice (No guarantees, though).

## Running locally
Ensure Pipenv is installed on your machine. Then run 
`pipenv shell` from the project's root directory. Next, run

```bash
bash up.sh
flask db init
flask db migrate
flask db upgrade
```

This will create an instance of the db running in a container (provided podman is installed - if it isn't, you can modify the script to use docker instead), then initialize it.

From there, to run, enter `flask run`, optionally followed by host and port, e.g. `flask run --host=0.0.0.0 --port=3000` from the `notes` directory. then navigate to localhost:3000 in a browser

Alternately, to run with a gunicorn (a production-grade server), move one directory up and run `gunicorn -b 0.0.0.0:5000 "notes:create_app()"`. Then navigate to localhost:5000 in a browser