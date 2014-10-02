define(['angular'], function(angular) {
    'use strict';

    angular.module('quizApp.submit.controllers', ['quizApp.main.api'])
        .controller('SubmitCtrl', ['$scope', 'Participant', function($scope, Participant) {
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
            }
        }]);
});