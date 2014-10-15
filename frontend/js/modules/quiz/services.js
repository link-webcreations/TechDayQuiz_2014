define([
    'angular'
], function(angular) {
    'use strict';

    var module = angular.module('quizApp.quiz.services', []);

    module.service('QuizResults', function() {
        // Store the quiz results
        this.results = {};

        // Validate that participant has answered all questions
        this.validate =  function() {
            for (var answer in this.results) {
                if (!(this.results[answer].content || this.results[answer].choice)) {
                    return false
                }
            };
            return true;
        }
    });
});
