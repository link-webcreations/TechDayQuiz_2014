define([
    'angular',
    'config',
    'angular-route',
    'angular-cookies',
    'angular-resource',
    'modules/main/mainModule',
    'modules/submit/submitModule'
], function(angular, config) {
    'use strict';

    var app = angular.module('quizApp', ['ngRoute',
                                         'ngCookies',
                                         'quizApp.main',
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
            .when('/submit', {
                controller: 'SubmitCtrl',
                templateUrl: config.partials_dir + '/submit.html',
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
