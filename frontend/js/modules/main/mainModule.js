define([
    'modules/main/controllers',
    'modules/main/factories'
], function() {
    'use strict';

    angular.module('quizApp.main', ['quizApp.main.controllers',
                                    'quizApp.main.api']);
});
