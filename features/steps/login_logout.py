from behave import *
from selenium import webdriver
from nose.tools import *

def get_element(driver, id=None, tag=None):
	if (id):
		return driver.find_element_by_id(id)
	else:
		if (tag):
			return driver.find_element_by_tag_name(tag)

@given('I am an unauthenticated user')
def step_impl(context):
    authenticated = True

@when('I navigate to the index page')
def step_impl(context):
	context.browser.get(context.application_url + 'index')

@then('I see the login page')
def step_impl(context):
    h = get_element(context.browser, tag='h2')
    ok_(h.text == "Please sign in", 'Sign in message %r has wrong text' % h.text)