define(['angular', 'config'], function(angular, config) {
    'use strict';

    angular.module('quizApp.main.api', ['ngResource'])
        .factory('Participant', ['$resource', function($resource) {
            return $resource(
                config.api_entry_point+'/participants/:participantId',
                {participantId: '@id'}
            );
        }]);
});
