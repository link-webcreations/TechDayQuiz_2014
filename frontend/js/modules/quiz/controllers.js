define([
    'angular'
], function(angular) {
    'use strict';

    angular.module('quizApp.quiz.controllers',
                   ['quizApp.main.services', 'quizApp.api.services'])
        .controller('QuizCtrl', ['$scope', 'Question', 'Globals',
            function($scope, Question, Globals) {
                $scope.questions = Question.query({quiz: Globals.active_quiz});
            }
        ]);
});
