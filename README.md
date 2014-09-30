# Faurecia - TechDay Quiz 2014

A web quiz using Django and AngularJS for the TechDay by Faurecia.

The project is composed of both **backend** and **frontend** components, for respectively the server side and the client side.

## Requirements

The project needs some tools used for the development and for the deployment. Ensure you have the following installed:

* NodeJS >= 0.10.32
* Python 2.7.x (with development headers)
    * Ubuntu: `sudo apt-get install python2.7-dev`
* [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/)
    * Ubuntu: `sudo apt-get install virtualenvwrapper`

## Developer Guide

This will guide you to the setup of all needed dependencies used during the development.

### Backend requirements

To install the development dependencies for the backend:

```
$ cd backend/
$ mkvirtualenv techday_quiz_2014 -r requirements-dev.txt
```

We assume that the python development virtual environment is **techday_quiz_2014**.

### Frontend requirements

To install the development dependencies for the frontend:

```
$ cd frontend/
$ npm install
$ bower install
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

Open your browser to http://localhost:8000/.
