define([
    'angular'
], function(angular) {
    'use strict';

    angular.module(
        'quizApp.intro.controllers',
        ['quizApp.main.services', 'quizApp.api.services']
    ).controller(
        'IntroCtrl',
        ['$scope', '$location', 'Quiz', 'Globals',
        function($scope, $location, Quiz, Globals) {
            $scope.ERRORS = {
                "QUIZ_FETCH": "Unable to fetch quizzes !",
                "QUIZ_NOT_FOUND": "There is no quiz available !"
            }

            Quiz.query().$promise.then(
            function(success) {
                if (success.length > 0) {
                    $scope.quizzes = success;
                    $scope.ready = true;
                } else {
                    $scope.ready = false;
                    $scope.error = "QUIZ_NOT_FOUND";
                }
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
