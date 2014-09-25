var QuizCtrl = BaseCtrl.extend({

    /**
     * Initialize Quiz Controller
     * @param $scope, current controller scope
     */  
    init:function($scope,$route){
        this._super($scope)
    },
})

QuizCtrl.$inject = ['$scope','$route'];
