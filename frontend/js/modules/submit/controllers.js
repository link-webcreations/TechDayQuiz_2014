define([
    'angular'
], function(angular) {
    'use strict';

    var module = angular.module('quizApp.submit.controllers',
                                ['quizApp.main.services',
                                 'quizApp.api.services',
                                 'quizApp.quiz.services']);

    // Controller for submitting the results
    module.controller(
        'SubmitCtrl',
        ['$scope', '$location', 'Globals', 'Participant', 'QuizResults',
        function($scope, $location, Globals, Participant, QuizResults) {
            if (!Globals.active_quiz) {
                $location.path("/intro");
            }

            $scope.submit_results = function() {
                $scope.submit_errors = null;

                if ($scope.submitForm.$valid) {
                    Participant.save($scope.participant).$promise.then(
                        function(new_participant) {
                            QuizResults.participant = new_participant;
                            QuizResults.send();
                            $location.path("/done");
                        },
                        function(errorResponse) {
                            $scope.submit_errors = errorResponse.data;
                        }
                    );
                }
            };
        }
    ]);

    // Controller for showing results
    module.controller(
        'ResultCtrl',
        ['$scope', '$location', 'Result', 'Globals', 'QuizResults',
        function($scope, $location, Result, Globals, QuizResults) {
            if (!Globals.active_quiz) {
                $location.path("/intro");
            } else {
                Result.query({
                    quiz: Globals.active_quiz.id,
                    participant: QuizResults.participant.id
                }).$promise.then(function(results) {
                    $scope.results = results;
                    QuizResults.in_progress = false;
                    Globals.active_quiz = null;
                });
            }
        }
    ]);
});
