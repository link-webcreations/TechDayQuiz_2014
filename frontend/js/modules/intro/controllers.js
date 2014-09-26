define(function() {
    'use strict';

    angular.module('quizApp.intro.controllers', [])
        .controller('IntroCtrl', ['$scope', function($scope) {
            $scope.intro_message = 'Ni hao!';
        }]);
});
