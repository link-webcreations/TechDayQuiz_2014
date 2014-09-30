define(function() {
    'use strict';

    angular.module('quizApp.main.api', ['ngResource'])
        .factory('Person', ['$resource', function($resource) {
            return $resource('http://localhost:8000/api/persons/:personId', {personId: '@id'});
        }]);
});
