define([
    'angular'
], function(angular) {
    'use strict';

    angular.module(
        'quizApp.quiz.controllers',
       ['quizApp.main.services',
        'quizApp.api.services',
        'quizApp.quiz.services']
    ).controller(
        'QuizCtrl',
        ['$scope',
         '$location',
         'Question',
         'Globals',
         'QuizResults',
         function(
            $scope,
            $location,
            Question,
            Globals,
            QuizResults
        ) {
            var questions;

            if (!Globals.active_quiz) {
                $location.path("/intro");
            } else {
                $scope.quiz = Globals.active_quiz;

                // Fetch all questions for the active quiz
                Question.query(
                    {quiz: Globals.active_quiz.id}
                ).$promise.then(function(success) {
                    questions = success;
                    angular.forEach(questions, function(question) {
                        if (question.answers.length > 0) {
                            QuizResults.results[question.id] = {"choice": null};
                        } else {
                            QuizResults.results[question.id] = {"content": null};
                        }
                    });
                    $scope.quiz_answers = QuizResults;
                    $scope.questions = questions;
                });

                // Prepare participant submission
                $scope.prepare_submit = function() {
                    if (QuizResults.validate()) {
                        // Quiz pass validation, prepare submission
                        $location.path("/submit");
                    }
                };
            }
        }
    ]);
});
