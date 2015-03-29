Feature: Login and logout

@skip
Scenario: Navigate to index page being a unauthenticated user
	Given I am an unauthenticated user
	When I navigate to the index page
	Then I see the login page