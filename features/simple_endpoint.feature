Feature: Showing off behave (tutorial01)

Scenario: Run a simple test
    Given I have a published hello world endpoint
    When I consume this endpoint
    Then I can see response http code 200
