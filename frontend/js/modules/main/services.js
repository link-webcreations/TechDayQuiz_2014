define([
    'angular'
], function(angular) {
    'use strict';

    var module = angular.module('quizApp.main.services', []);

    module.value('Globals', {
            active_quiz: null,
        }
    );
});
