//entry point for the application
angular.module('studentsmeetstartup',[
	'ui.router',
	'ui.bootstrap',
	'ui.select',
	'signup-startup',
	'signup-student',
	'ngSanitize',
	'scrollto'

])

	.config(function($stateProvider, $urlRouterProvider, uiSelectConfig) {
		/*var html5Mode = (window.history && window.history.pushState);
		$locationProvider.html5Mode(html5Mode).hashPrefix('!');*/
		uiSelectConfig.theme = 'bootstrap';
		$stateProvider
			.state('greeting', {
				url: '/home',
				views: {
					'welcome': {
						templateUrl: "static/greeting.html"
					},
					'student-signup':{
						templateUrl: 'static/student-signup.html'
					},
					'startup-signup':{
						templateUrl: 'static/startup-signup.html'
					}
				}
			})
	});

angular.module('signup-startup', [])
	.controller('signupStartupController', ['$scope', '$log', '$http', function($scope, $log, $http){
		$scope.length = 0;
		$scope.maxLength = 400;
		$scope.description = "";
		$scope.characterCount = function(){
	        $scope.length = $scope.description.length;
	        $log.info($scope.length);
      	}

      	$scope.address = {};
		$scope.refreshAddresses = function(address) {
			var params = {address: address, sensor: false};
			return $http.get(
				'http://maps.googleapis.com/maps/api/geocode/json',
				{params: params}
			).then(function(response) {
				$scope.addresses = response.data.results
			});
		};
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

      	$scope.address = {};
		$scope.refreshAddresses = function(address) {
			var params = {address: address, sensor: false};
			return $http.get(
				'http://maps.googleapis.com/maps/api/geocode/json',
				{params: params}
			).then(function(response) {
				$scope.addresses = response.data.results
			});
		};

	}]);
