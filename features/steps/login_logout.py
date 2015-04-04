from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions
from nose.tools import *
import time

def wait_for(condition_function):
    start_time = time.time()
    while time.time() < start_time + 3:
        if condition_function():
            return True
        else:
            time.sleep(0.1)
    raise Exception(
        'Timeout waiting for {}'.format(condition_function.__name__)
    )

class wait_for_page_load(object):

    def __init__(self, browser):
        self.browser = browser

    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')

    def page_has_loaded(self):
        new_page = self.browser.find_element_by_tag_name('html')
        return new_page.id != self.old_page.id

    def __exit__(self, *_):
        wait_for(self.page_has_loaded)

def get_element(driver, id=None, tag=None, text=None):
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

username = ''
password = ''

@given('I am a valid user')
def step_impl(context):
    global username
    global password
    username = 'valid_user'
    password = 'valid_password'

@when('I attempt to login')
def step_impl(context):
	try:
		get_element(context.browser, id='logout').click()
	except:
		pass

	context.browser.get(context.application_url + 'login')
	get_element(context.browser, id='login').send_keys(username)
	get_element(context.browser, id='password').send_keys(password)
	get_element(context.browser, id='submit').click()

@then('I am redirected to the index page')
def step_impl(context):
    h = get_element(context.browser, id="welcome-message")
    ok_(h.text.startswith("Hi"), 'Hello message %r has wrong text' % h.text)

@given('I am a invalid user')
def step_impl(context):
    global username
    global password
    username = 'invalid_user'
    password = 'invalid_password'

@then('I see an error message')
def step_impl(context):
    h = get_element(context.browser, id="error-message")
    ok_(h.text.startswith("Invalid"), 'Error message %r has wrong text' % h.text)
