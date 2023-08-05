# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s newsletter.types -t test_newsletter_container.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src newsletter.types.testing.NEWSLETTER_TYPES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/newsletter/types/tests/robot/test_newsletter_container.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a NewsletterContainer
  Given a logged-in site administrator
    and an add NewsletterContainer form
   When I type 'My NewsletterContainer' into the title field
    and I submit the form
   Then a NewsletterContainer with the title 'My NewsletterContainer' has been created

Scenario: As a site administrator I can view a NewsletterContainer
  Given a logged-in site administrator
    and a NewsletterContainer 'My NewsletterContainer'
   When I go to the NewsletterContainer view
   Then I can see the NewsletterContainer title 'My NewsletterContainer'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add NewsletterContainer form
  Go To  ${PLONE_URL}/++add++NewsletterContainer

a NewsletterContainer 'My NewsletterContainer'
  Create content  type=NewsletterContainer  id=my-newsletter_container  title=My NewsletterContainer

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the NewsletterContainer view
  Go To  ${PLONE_URL}/my-newsletter_container
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a NewsletterContainer with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the NewsletterContainer title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
