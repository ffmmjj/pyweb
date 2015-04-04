Feature: Login and logout

Scenario: Navigate to index page being a unauthenticated user
	Given I am an unauthenticated user
	When I navigate to the index page
	Then I see the login page

Scenario: Login with a valid user
	Given I am a valid user
	When I attempt to login
	Then I am redirected to the index page

Scenario: Login with a invalid user
	Given I am a invalid user
	When I attempt to login
	Then I see an error message
