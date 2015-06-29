# pyweb  [![Build Status](https://snap-ci.com/tmssoares/pyweb/branch/master/build_image)](https://snap-ci.com/tmssoares/pyweb/branch/master)

YummyBox is a natural processing language application for analyzing email boxes in order to group emails by topic. The technologies used in its development are Python2.7, Flask, Jinja2, Behave and MongoDB. For CI and deploy we're using Snap-ci and Heroku.


Running the application:

`python manage.py runserver`

Running acceptance tests:

`behave`

Running unit tests:

`python -m unittest unit_tests`

The production url for YummyBox is:

http://paiweb.herokuapp.com/
