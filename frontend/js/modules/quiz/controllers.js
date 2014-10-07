define([
    'angular'
], function(angular) {
    'use strict';

    angular.module('quizApp.quiz.controllers',
                   ['quizApp.main.services', 'quizApp.api.services'])
        .controller('QuizCtrl', ['$scope', '$location', 'Question', 'Globals',
            function($scope, $location, Question, Globals) {
                if (!Globals.active_quiz) {
                    $location.path("/intro");
                } else {
                    $scope.quiz = Globals.active_quiz;
                    $scope.questions = Question.query(
                                            {quiz: Globals.active_quiz.id});
                    $scope.select_answer = function(answer) {
                        $location.path("/submit");
                    };
                }
            }
        ]);
});
