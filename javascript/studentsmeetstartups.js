//entry point for the application
angular.module('studentsmeetstartup',[
	'ui.router',
	'ui.bootstrap',
	'ui.select',
	'backgroundImage',
	'whiteBuble',
	'signup-startup',
	'signup-student'
])

	.config(function($stateProvider, $urlRouterProvider, uiSelectConfig) {
		/*var html5Mode = (window.history && window.history.pushState);
		$locationProvider.html5Mode(html5Mode).hashPrefix('!');*/
		uiSelectConfig.theme = 'bootstrap';
		$stateProvider
			.state('greeting', {
				url: '/index',
				views: {
					'content': {
						templateUrl: "static/whitebuble.html"
					}
				}
			})

			.state('browse-startup', {
				url: '/index',
				views: {
					'content': {
						templateUrl: "static/browse-startup.html"
					}
				}
			})
	});

angular.module('backgroundImage', [])
	.controller('backgroundImageController', ['$scope', '$log', '$http', function($scope, $log, $http) {
		$scope.images = ['static/fjord.jpg'];
		$scope.image = '#000 url(' + $scope.images[Math.floor(Math.random() * $scope.images.length)] + ') 0 0 no-repeat';
		$scope.style = {'background': $scope.image};
	}]);

angular.module('whiteBuble', [])
	.controller('bubleController', ['$scope', '$log', '$http', function($scope, $log, $http) {
		$scope.state = 'greeting';
		$log.info($scope.state);
		$scope.changeState = function(state){
			$scope.state = state;
		}
	}]);

angular.module('signup-startup', [])
	.controller('signupStartupController', ['$scope', '$log', '$http', function($scope, $log, $http){
		$scope.length = 0;
		$scope.maxLength = 400;
		$scope.description = "";
		$scope.characterCount = function(){
	        $scope.length = $scope.description.length;
	        $log.info($scope.length);
      	}
	}]);

angular.module('signup-student', [])
	.controller('signupStudentController', ['$scope', '$log', '$http', function($scope, $log, $http){
		$scope.length = 0;
		$scope.maxLength = 400;
		$scope.description = "";
		$scope.characterCount = function(){
	        $scope.length = $scope.description.length;
	        $log.info($scope.length);
      	}
	}]);
