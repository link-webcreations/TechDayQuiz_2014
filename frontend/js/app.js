'use strict';

angular.module('quiz', [''])
    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.otherwise({redirectTo: '/intro'});

        window.routeProvider = $routeProvider;
        window.startHash = window.location.hash.substring(1);
    }])
