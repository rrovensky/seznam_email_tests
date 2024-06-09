from pytest_bdd import scenario, given, when, then
from playwright.sync_api import Page
from pages.seznam_open_and_login import OpenSeznam, LoginToSeznam
from pages.seznam_navigation import SeznamNavigationMenu
from pages.seznam_email_handling import WriteAndSendEmail
import pytest


@scenario('../features/send_email.feature', 'User can send email from seznam account')
def test_i_can_send_email_from_my_seznam_account():
    print('starting bdd test')


@pytest.fixture
def email(page: Page):
    """Methods for composing emails in Seznam account, sending them and checking if sent"""
    return WriteAndSendEmail(page)


@given("User is logged in to Seznam account")
def seznam_logging_to_account(page: Page):
    OpenSeznam(page).open_seznam()
    login_user = LoginToSeznam(page)
    login_user.enter_login()
    login_user.enter_pwd()
    SeznamNavigationMenu(page).verify_left_menu_links()


@when("a contact is picked from Kontakty")
def contact_selected_from_kontakty(email):
    email.find_contact()


@when("email composed and sent")
def email_composed_and_sent(email):
    email.email_composed_and_sent()


@then("email is in Odeslane folder")
def email_sent(email):
    email.check_email_sent()
