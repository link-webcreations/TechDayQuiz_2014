#!/usr/bin/make -f
# Copyright (c) 2014 Vincent BESANÇON <besancon.vincent@gmail.com>
# Copyright (c) 2014 Yves ANDOLFATTO <yves.andolfatto@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

export PATH := /opt/nodejs/bin:$(PATH)

#export http_proxy=http://127.0.1.1:3128/
#export https_proxy=http://127.0.1.1:3128/

SHELL=/bin/bash

WHEELS_CACHE=$(CURDIR)/.wheels_cache
WHEELS=$(CURDIR)/wheels
PIP_CACHE=$(CURDIR)/.pip_download_cache

VIRTUALENVS_DIR=$(CURDIR)/.virtualenvs
PY_ENV=${VIRTUALENVS_DIR}/techday
PY_ENV_ACTIVATE=${PY_ENV}/bin/activate

BACKEND_PROD_DEPS=$(CURDIR)/backend/production.pip
BACKEND_DEV_DEPS=$(CURDIR)/backend/develop.pip

define HELP_MESSAGE
Faurecia GIS TechDay 2014
=========================

Development
-----------

develop        Install all needed dependencies for development.

Cleaning
--------

clean          Clean generated files.
distclean      Clean the total project (node modules, bower,
               python...)
endef
export HELP_MESSAGE

# Default target
.PHONY: all
all: help

# Show help
.PHONY: help
help:
	@echo "$$HELP_MESSAGE"

#===============================================================================
# CLEANING
#===============================================================================
#
.PHONY: clean
clean: clean-python

.PHONY: distclean
distclean: clean-python clean-node clean-bower clean-python_env

.PHONY: clean-python
clean-python:
	@echo "Cleaning Python byte compiled files..."
	@find $(CURDIR) -name '*.pyc' -delete

.PHONY: clean-node
clean-node:
	@echo "Cleaning Node modules..."
	@rm -rf frontend/node_modules

.PHONY: clean-bower
clean-bower:
	@echo "Cleaning Bower components..."
	@rm -rf frontend/bower_components

.PHONY: clean-python_env
clean-python_env:
	@echo "Removing python virtualenv..."
	@rm -rf ${PY_ENV}
	@rm -rf ${WHEELS_CACHE}

#===============================================================================
# PYTHON ENVIRONMENT & WHEELS
#===============================================================================
#
# Create Python environment
.PHONY: python-env_create
python-env_create:
	@echo -e "\n*** CREATING NEW PYTHON ENVIRONMENT ***\n"
	@[ ! -d ${PY_ENV} ] && virtualenv ${PY_ENV} && \
		( \
			source ${PY_ENV_ACTIVATE}; \
			pip install wheel; \
			pip wheel \
				-w ${WHEELS_CACHE} \
				--download-cache ${PIP_CACHE} \
				wheel pip setuptools; \
			pip install \
				--no-index \
				--find-links=${WHEELS_CACHE} \
				--upgrade pip setuptools; \
		) || \
		echo "Python environment already created."

# Download and build wheels
wheels-download: python-env_create
	@echo -e "\n*** FETCHING PYTHON WHEELS ***\n"
	@( \
		source ${PY_ENV_ACTIVATE}; \
		pip wheel \
			-w ${WHEELS_CACHE} \
			--download-cache ${PIP_CACHE} \
			-r ${BACKEND_DEV_DEPS}; \
	)

# Install wheels used in production
install-wheels: wheels-download
	@( \
		source ${PY_ENV_ACTIVATE}; \
		pip wheel \
			-w wheels \
			--no-index \
			--find-links=${WHEELS_CACHE} \
			-r ${BACKEND_PROD_DEPS}; \
	)

#===============================================================================
# DEPENDENCIES INSTALLATION
#===============================================================================
#
.PHONY: install-deps-prod
install-deps-prod: install-deps-prod-frontend

.PHONY: install-deps-dev
install-deps-dev: install-wheels-dev install-deps-prod-frontend

.PHONY: install-deps-prod-frontend
install-deps-prod-frontend:
	@echo -e "\n*** INSTALL NPM MODULES ***\n"
	@(cd $(CURDIR)/frontend; mkdir -p $(CURDIR)/debian/tmp/usr; npm install)
	@echo -e "\n*** INSTALL BOWER COMPONENTS ***\n"
	@(cd $(CURDIR)/frontend; node_modules/.bin/bower --allow-root install)

.PHONY: install-wheels-dev
install-wheels-dev: wheels-download
	@( \
		source ${PY_ENV_ACTIVATE}; \
		pip install \
			--no-index \
			--find-links=${WHEELS_CACHE} \
			-r ${BACKEND_DEV_DEPS}; \
	)

#===============================================================================
# MAIN
#===============================================================================
#
.PHONY: develop
develop: install-deps-dev

.PHONY: install
install: develop
	@install -d $(DESTDIR)/usr/share/techday-2014/
	@cp -ra backend $(DESTDIR)/usr/share/techday-2014
	@cp -ra wheels $(DESTDIR)/usr/share/techday-2014
	@cp -ra frontend $(DESTDIR)/usr/share/techday-2014
	@rm -rf $(DESTDIR)/usr/share/techday-2014/frontend/node_modules
