define([
    'angular'
], function(angular) {
    'use strict';

    angular.module('quizApp.intro.controllers',
                   ['quizApp.main.services', 'quizApp.api.services'])
        .controller('IntroCtrl', ['$scope', '$location', 'Quiz', 'Globals',
            function($scope, $location, Quiz, Globals) {
                $scope.ERRORS = {
                    "QUIZ_FETCH": "Unable to fetch quizzes !"
                }

                Quiz.query().$promise.then(
                function(success) {
                    $scope.quizzes = success;
                    $scope.ready = true;
                },
                function(error) {
                    $scope.ready = false;
                    $scope.error = "QUIZ_FETCH";
                });

                $scope.select_quiz = function(quiz) {
                    Globals.active_quiz = quiz;
                    $location.path("/quiz");
                };
            }
        ]);
});
