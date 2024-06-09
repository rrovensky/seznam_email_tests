from pytest_bdd import scenario, given, when, then, parsers
from playwright.sync_api import Page
from pages.seznam_open_and_login import OpenSeznam, LoginToSeznam
from pages.seznam_navigation import SeznamNavigationMenu


@scenario('../features/login.feature', 'Login to seznam email account')
def test_user_can_login_to_seznam():
    print('starting bdd test')


@given("seznam default login page is open")
def seznam_login_page_open(page: Page):
    OpenSeznam(page).open_seznam()


@when(parsers.parse("I enter valid Seznam {login} and {password} and hit Sign in"))
def enter_valid_login(page: Page, login, password):
    login_user = LoginToSeznam(page, login, password)
    login_user.enter_login()
    login_user.enter_pwd()


@then("I see Seznam Inbox")
def inbox_shown(page: Page):
    SeznamNavigationMenu(page).verify_left_menu_links()
