Feature: Home page

Scenario: Navigate to home page with no messages loaded
	Given I am a valid user with messages
	When I navigate to the home page
	Then I see the home page with no messages displayed