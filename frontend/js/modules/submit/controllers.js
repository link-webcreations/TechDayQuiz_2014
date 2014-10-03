define([
    'angular'
], function(angular) {
    'use strict';

    var module = angular.module('quizApp.submit.controllers',
                                ['quizApp.main.services',
                                 'quizApp.api.services']);

    // Submit result controller
    module.controller('SubmitCtrl',
                      ['$scope', 'Participant', function($scope, Participant) {
        $scope.submit_results = function() {
            $scope.submit_errors = null;
            $scope.submit_success = false;

            if ($scope.submitForm.$valid) {
                Participant.save($scope.participant).$promise
                    .then(
                        function(success) {
                            $scope.submit_success = true;
                        },
                        function(errorResponse) {
                            $scope.submit_errors = errorResponse.data;
                    });
            }
        };
    }]);

    // Results controller
    module.controller('ResultCtrl',
                      ['$scope', 'Result', function($scope, Result) {
        $scope.results = Result.query({quiz: 1, participant: 9});
    }]);
});
