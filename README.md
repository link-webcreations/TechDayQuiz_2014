# Faurecia - TechDay Quiz 2014

A web quiz using Django and AngularJS for the TechDay by Faurecia.

The project is composed of both **backend** and **frontend** components, for
respectively the server side and the client side.

## Requirements

The project needs some tools used for the development and for the deployment.
Ensure you have the following installed:

* NodeJS >= 0.10.32
* GNU Make
    * Ubuntu: `sudo apt-get install make`
* Python 2.7.x (with development headers)
    * Ubuntu: `sudo apt-get install python2.7-dev`
* [virtualenv](http://virtualenv.readthedocs.org/)
    * Ubuntu: `sudo apt-get install python-virtualenv`

## Developer Guide

This will guide you to the setup of all needed dependencies used during the
development.

To install all the needed dependencies for development:

```
$ make develop
```

This will creates:

* A python virtualenv in `.virtualenvs/techday/`.
* A cache directory containing pip's wheels in `.wheels_cache/`.
* A download cache for pip in `.pip_download_cache/`.

Enable the Python virtualenv using:

```
$ . .virtualenvs/techday/bin/activate
```

### Start the backend

Change to the backend's techday django project directory:

```
$ cd backend/techday/
```

Create the database and run the migrations. You will be asked to create a
superuser:

```
$ ./manage.py syncdb
```

Start the backend that provides the RESTful API. Start a web server listening
on port 8000:

```
$ ./manage.py runserver
```

### Start the frontend

Change to the frontend directory:

```
$ cd frontend/
```

Start the HTTP server:

```
$ ./node_modules/.bin/http-server
```

Open your browser to http://localhost:8080/.
