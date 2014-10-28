//entry point for the application
angular.module('studentsmeetstartup',[
	'ui.router',
	'ui.bootstrap',
	'backgroundImage',
	'whiteBuble'
])

	.config(function($stateProvider, $urlRouterProvider) {
		/*var html5Mode = (window.history && window.history.pushState);
		$locationProvider.html5Mode(html5Mode).hashPrefix('!');*/

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
		$scope.image = 'url(' + $scope.images[Math.floor(Math.random() * $scope.images.length)] + ')';
		$scope.style = {'background': $scope.image};
	}]);

angular.module('whiteBuble', [])
	.controller('bubleController', ['$scope', '$log', '$http', function($scope, $log, $http) {
		$scope.state = "greeting";
	}]);
