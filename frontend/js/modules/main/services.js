define([
    'angular'
], function(angular) {
    'use strict';

    var module = angular.module('quizApp.main.services', []);

    module.service('Globals', function() {
        return {
            active_quiz: null,
        };
    });
});
