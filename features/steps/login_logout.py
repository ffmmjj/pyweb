from behave import *
from selenium import webdriver
from nose.tools import *

def get_element(driver, id=None, tag=None):
	if (id):
		return driver.find_element_by_id(id)
	else:
		if (tag):
			return driver.find_element_by_tag_name(tag)

@given('I am an authenticated user')
def step_impl(context):
    authenticated = True

@when('I navigate to the index page')
def step_impl(context):
    context.browser.get('http://localhost:5000/index')

@then('I can see the welcome user message')
def step_impl(context):
    h = get_element(context.browser, tag='h1')
    ok_(h.text.startswith("Hi,"), 'Welcome message %r has wrong text' % h.text)