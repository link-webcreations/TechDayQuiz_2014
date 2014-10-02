define([
    'angular'
], function(angular) {
    'use strict';

    angular.module('quizApp.main.controllers', [])
        .controller('MainCtrl', ['$scope',
                                 '$location', function($scope, $location) {
            $scope.section = $location.path();
            $scope.isActive = function(route) {
                return route === $location.path();
            }
        }]);
});
