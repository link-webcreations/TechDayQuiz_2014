define([
    'angular',
    'angular-route'
], function(angular) {
    'use strict';

    var app = angular.module('quizApp', ['ngRoute']);

    app.init = function () {
      angular.bootstrap(document, ['quizApp']);
    };

    app.config(function($routeProvider) {
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

    return app;
});
