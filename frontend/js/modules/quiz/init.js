define([
    'angular',
    './controllers',
    './services'
], function(angular) {
    'use strict';

    return angular.module('quizApp.quiz', ['quizApp.quiz.controllers',
                                           'quizApp.quiz.services']);
});
