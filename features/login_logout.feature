Feature: Login and logout

Scenario: Navigate to index page
	Given I am an authenticated user
	When I navigate to the index page
	Then I can see the welcome user message