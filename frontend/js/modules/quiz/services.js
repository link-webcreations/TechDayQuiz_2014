define([
    'angular'
], function(angular) {
    'use strict';

    var module = angular.module('quizApp.quiz.services',
                                ['quizApp.api.services']);

    module.service('QuizResults',
                  ['ParticipantAnswer', function(ParticipantAnswer) {
        this.in_progress = false;
        
        // Initialization of a new quiz progress
        this.init = function(questions) {
            this.participant = {};
            this.in_progress = true;
            this.results = {};

            angular.forEach(questions, function(question) {
                if (question.answers.length > 0) {
                    question = {"choice": null};
                } else {
                    question = {"content": null};
                }
            });
        }

        // Validate that participant has answered all questions
        this.validate =  function() {
            for (var answer in this.results) {
                if (!(this.results[answer].content || this.results[answer].choice)) {
                    return false
                }
            };
            return true;
        }

        // Send the results
        this.send = function() {
            if (this.validate() && this.participant) {
                console.log("Sending results...");
                for (var question_id in this.results) {
                    var result = new ParticipantAnswer();
                    result.participant = this.participant.id
                    result.question = parseInt(question_id, 10);
                    result.answer = this.results[question_id].choice;
                    result.content = this.results[question_id].content;
                    result.$save();
                };
            }
        }
    }]);
});
