define(function() {
    'use strict';

    angular.module('quizApp.main.controllers', [])
        .controller('MainCtrl', ['$scope', '$location', function($scope, $location) {
            $scope.isActive = function(route) {
                return route === $location.path();
            }
        }]);
});
