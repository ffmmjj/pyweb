from selenium import webdriver

# -- FILE: features/environment.py
# USE: behave -D BEHAVE_DEBUG_ON_ERROR         (to enable  debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=yes     (to enable  debug-on-error)
# USE: behave -D BEHAVE_DEBUG_ON_ERROR=no      (to disable debug-on-error)

BEHAVE_DEBUG_ON_ERROR = False

def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %s" % (attr, getattr(obj, attr)))

def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("behave_debug_on_error")

def before_all(context):
	context.browser = webdriver.Chrome()

	setup_debug_on_error(context.config.userdata)

def after_all(context):  
    context.browser.quit()

def after_step(context, step):
	print('Status')
	if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
	# 	# -- ENTER DEBUGGER: Zoom in on failure location.
	# 	# NOTE: Use IPython debugger, same for pdb (basic python debugger).
		import ipdb
 		ipdb.post_mortem(step.exc_traceback)