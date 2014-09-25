'use strict';

window.quiz = angular.module('quiz', ['ngRoute'])
    .config(function($routeProvider) {
        var partialsDir = '../partials';

        // Routes configuration
        $routeProvider
            .when('/', {
                redirectTo: '/intro'
            })
            .when('/intro', {
                controller: 'IntroCtrl',
                templateUrl: partialsDir + '/01_intro.html',
            })
            .otherwise({
                redirectTo: '/'
            });

        window.routeProvider = $routeProvider;
        window.startHash = window.location.hash.substring(1);
    });
