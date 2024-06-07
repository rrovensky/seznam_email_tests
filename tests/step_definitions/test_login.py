from pytest_bdd import scenario, given, when, then
from playwright.sync_api import Page, expect
import pytest


from pages.seznam_navigation import SeznamNavigationMenu, EnterLoginDetails

@scenario('../features/login.feature', 'Login to seznam account')
def test_user_can_login_to_seznam():
    print('starting bdd test')


@given("seznam default login page is open")
def seznam_login_page_open(page: Page):
    page.goto("https://email.seznam.cz")
    expect(page.get_by_role("textbox", name="Email account or phone number"))


@when("I enter my valid Seznam login and Password and hit Sign in")
def enter_valid_login(page: Page):
    login_user = EnterLoginDetails(page, "roman.test@post.cz", "@TEst1234")
    login_user.enter_login()
    login_user.enter_pwd()


# Then Steps
@then("I can see my Inbox")
def inbox_shown(page: Page):
    SeznamNavigationMenu(page).verify_left_menu_links()
