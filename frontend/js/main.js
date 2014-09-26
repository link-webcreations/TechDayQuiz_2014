'use strict';

requirejs.config({
    baseUrl: '/js',

    // For DEBUG only
    urlArgs: "bust=" + (new Date()).getTime(),

    // Vendor modules
    paths: {
        'angular': '../bower_components/angular/angular.min',
        'angular-route': '../bower_components/angular-route/angular-route.min',
        'jquery': '../bower_components/jquery/dist/jquery.min',
        'bootstrap': '../bower_components/bootstrap/dist/js/bootstrap.min'
    },

    // angular does not support AMD out of the box, put it in a shim
    // Checkout more about AMD: https://github.com/amdjs/amdjs-api/blob/master/AMD.md
    shim: {
        'bootstrap': {
            deps: ['jquery']
        },
        'angular': {
            exports: 'angular'
        },
        'angular-route':{
            deps: ['angular']
        }
    }
});

// Start the application.
requirejs([
    'jquery',
    'bootstrap',
    'app'
], function ($, _bootstrap, app) {
  app.init();
});
