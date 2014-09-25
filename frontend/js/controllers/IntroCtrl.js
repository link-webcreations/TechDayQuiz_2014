define(['app'], function(app) {
    'use strict';

    app.controller('IntroCtrl', ['$scope', function($scope) {
        $scope.intro_message = 'Ni hao!';
    }]);
});
