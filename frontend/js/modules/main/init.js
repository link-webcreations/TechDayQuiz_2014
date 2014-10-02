define([
    'angular',
    'modules/main/controllers',
    'modules/main/factories'
], function(angular) {
    'use strict';

    return angular.module('quizApp.main', ['quizApp.main.controllers',
                                           'quizApp.main.api']);
});
