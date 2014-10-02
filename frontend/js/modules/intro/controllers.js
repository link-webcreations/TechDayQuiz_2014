define(['angular'], function(angular) {
    'use strict';

    angular.module('quizApp.intro.controllers', ['quizApp.main.api'])
        .controller('IntroCtrl', ['$scope', '$location', 'Quiz', 'Globals',
            function($scope, $location, Quiz, Globals) {
                $scope.quizzes = Quiz.query();

                $scope.select_quiz = function(quiz_id) {
                    Globals.active_quiz = quiz_id;
                    $location.path("/quiz");
                }
            }
        ]);
});
