/*
Copyright (c) 2014 Vincent BESANÇON <besancon.vincent@gmail.com>
Copyright (c) 2014 Yves ANDOLFATTO <yves.andolfatto@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

(function() {
    'use strict';

    requirejs.config({
        baseUrl: '/js',

        // For DEBUG only
        urlArgs: "bust=" + (new Date()).getTime(),

        // Vendor modules
        paths: {
            'angular': '../bower_components/angular/angular.min',
            'angular-route': '../bower_components/angular-route/angular-route.min',
            'angular-cookies': '../bower_components/angular-cookies/angular-cookies.min',
            'angular-resource': '../bower_components/angular-resource/angular-resource.min',
            'jquery': '../bower_components/jquery/dist/jquery.min',
            'bootstrap': '../bower_components/bootstrap/dist/js/bootstrap.min',
            'sweetalert': '../bower_components/sweetalert/lib/sweet-alert.min'
        },

        // angular does not support AMD out of the box, put it in a shim
        shim: {
            'bootstrap': {
                deps: ['jquery']
            },
            'angular': {
                exports: 'angular'
            },
            'angular-route':{
                deps: ['angular']
            },
            'angular-cookies':{
                deps: ['angular']
            },
            'angular-resource':{
                deps: ['angular']
            }
        }
    });

    // Start the application.
    requirejs([
        'jquery',
        'bootstrap',
        'sweetalert',
        'app'
    ], function ($, _bootstrap, _sweetalert, app) {
      app.init();
    });
}());
