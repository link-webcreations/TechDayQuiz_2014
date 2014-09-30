define([
    'angular',
    'angular-route',
    'modules/main/mainModule',
    'modules/intro/introModule'
], function() {
    'use strict';

    var app = angular.module('quizApp', ['ngRoute', 'quizApp.intro']);

    app.init = function () {
      angular.bootstrap(document, ['quizApp']);
    };

    app.config(function($routeProvider) {
        var partialsDir = '../partials';

        // Routes configuration
        $routeProvider
            .when('/', {
                controller: 'MainCtrl',
                redirectTo: '/intro'
            })
            .when('/intro', {
                controller: 'IntroCtrl',
                templateUrl: partialsDir + '/01_intro.html',
            })
            .when('/quiz', {
                redirectTo: partialsDir + '/02_quiz.html'
            })
            .when('/review', {
                redirectTo: partialsDir + '/03_review.html'
            })
            .when('/about', {
                redirectTo: partialsDir + '/04_about.html'
            })
            .otherwise({
                redirectTo: '/'
            });

        window.routeProvider = $routeProvider;
        window.startHash = window.location.hash.substring(1);
    });

    return app;
});
