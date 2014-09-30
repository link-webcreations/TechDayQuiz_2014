define(['angular', 'config'], function(angular, config) {
    'use strict';

    angular.module('quizApp.main.api', ['ngResource'])
        .factory('Person', ['$resource', function($resource) {
            return $resource(
                config.api_entry_point+'/persons/:personId',
                {personId: '@id'}
            );
        }]);
});
