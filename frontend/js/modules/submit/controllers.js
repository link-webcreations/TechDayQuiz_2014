define([
    'angular'
], function(angular) {
    'use strict';

    var module = angular.module('quizApp.submit.controllers',
                                ['quizApp.main.services',
                                 'quizApp.api.services']);

    // Submit result controller
    module.controller(
        'SubmitCtrl',
        ['$scope', '$location', 'Participant',
        function($scope, $location, Participant) {
            $scope.submit_results = function() {
                $scope.submit_errors = null;
                $scope.submit_success = false;

                swal({
                    title: "Are you sure?",
                    text: "You will not be able to change anything!",
                    type: "warning",
                    showCancelButton: true,
                    confirmButtonColor: "#89C068",
                    confirmButtonText: "Yes, send my answers!"
                },function() {
                    if ($scope.submitForm.$valid) {
                    Participant.save($scope.participant).$promise
                        .then(
                            function(success) {
                                $scope.submit_success = true;
                                $location.path("/done");
                            },
                            function(errorResponse) {
                                $scope.submit_errors = errorResponse.data;
                        });
                    }
                });
            };
        }
    ]);

    // Results controller
    module.controller(
        'ResultCtrl',
        ['$scope', 'Result',
        function($scope, Result) {
            $scope.results = Result.query({quiz: 1, participant: 1});
        }
    ]);
});
