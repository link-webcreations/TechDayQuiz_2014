define(['angular', 'config'], function(angular, config) {
    'use strict';

    var module = angular.module('quizApp.main.api', ['ngResource']);

    module.factory('Participant', ['$resource', function($resource) {
        return $resource(
            config.api_entry_point+'/participants/:participantId',
            {participantId: '@id'}
        )
    }]);

    module.factory('Quiz', ['$resource', function($resource) {
        return $resource(
            config.api_entry_point+'/quizzes/:quizId',
            {quizId: '@id'}
        )
    }]);

    module.factory('Question', ['$resource', function($resource) {
        return $resource(
            config.api_entry_point+'/questions/:questionId',
            {questionId: '@id'}
        )
    }]);

    module.factory('Globals', function() {
        return {
            active_quiz: null,
        }
    });
});
