define([
    'angular',
    'config',
    'angular-route',
    'angular-cookies',
    'angular-resource',
    'modules/init'
], function(angular, config) {
    'use strict';

    var app = angular.module('quizApp', ['ngRoute',
                                         'ngCookies',
                                         'quizApp.api',
                                         'quizApp.intro',
                                         'quizApp.main',
                                         'quizApp.quiz',
                                         'quizApp.submit']);

    app.init = function () {
      angular.bootstrap(document, ['quizApp']);
    };

    app.config(['$routeProvider', '$httpProvider', function($routeProvider, $httpProvider) {
        // Routes configuration
        $routeProvider
            .when('/', {
                redirectTo: '/intro'
            })
            .when('/intro', {
                controller: 'IntroCtrl',
                templateUrl: config.partials_dir + '/intro.html',
            })
            .when('/quiz', {
                controller: 'QuizCtrl',
                templateUrl: config.partials_dir + '/quiz.html',
            })
            .when('/submit', {
                controller: 'SubmitCtrl',
                templateUrl: config.partials_dir + '/submit.html',
            })
            .when('/about', {
                templateUrl: config.partials_dir + '/about.html',
            })
            .otherwise({
                redirectTo: '/'
            });

        window.routeProvider = $routeProvider;
        window.startHash = window.location.hash.substring(1);

        // CSRF
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    }]);

    return app;
});
