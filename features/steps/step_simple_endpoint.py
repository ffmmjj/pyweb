from behave import given, when, then, configuration
import urllib2

@given('I have a published hello world endpoint')
def step_impl(context):
    context.url = "http://localhost:5000/"

@when('I consume this endpoint')
def step_impl(context):
    context.response = urllib2.urlopen(context.url)

@then('I can see response http code 200')
def step_impl(context):
    assert context.response.code is 200