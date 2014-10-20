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

define HELP_MESSAGE
Faurecia GIS TechDay 2014
=========================

Available targets:

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

# Cleaning targets
#
.PHONY: clean
clean: clean-python

.PHONY: distclean
distclean: clean-python clean-node clean-bower

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
