define([
    'angular',
    'config'
], function(angular, config) {
    'use strict';

    var module = angular.module('quizApp.main.services', ['ngResource']);

    module.service('Globals', function() {
        return {
            active_quiz: null,
        };
    });
});
