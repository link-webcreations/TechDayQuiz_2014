define([
    'angular',
    './controllers',
    './services'
], function(angular) {
    'use strict';

    return angular.module('quizApp.main', ['quizApp.main.controllers',
                                           'quizApp.main.services']);
});
