define([
    'angular'
], function(angular) {
    'use strict';

    angular.module('quizApp.intro.controllers',
                   ['quizApp.main.services', 'quizApp.api.services'])
        .controller('IntroCtrl', ['$scope', '$location', 'Quiz', 'Globals',
            function($scope, $location, Quiz, Globals) {
                $scope.quizzes = Quiz.query();

                $scope.select_quiz = function(quiz) {
                    Globals.active_quiz = quiz;
                    $location.path("/quiz");
                };
            }
        ]);
});
