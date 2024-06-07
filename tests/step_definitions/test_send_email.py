import time
import re
import pytest

from pytest_bdd import scenario, given, when, then
from playwright.sync_api import Page, expect


@scenario('../features/send_email.feature', 'Sending email from Seznam account')
def test_user_can_send_email_from_seznam_account():
    print('starting bdd test')


@given("seznam default login page is open")
def seznam_login_page_open(page: Page):
    page.goto("https://email.seznam.cz")
    expect(page.get_by_role("textbox", name="Email account or phone number"))


@when("I enter my valid Seznam login and Password and hit Sign in")
def enter_valid_login(page: Page):
    page.get_by_role("textbox", name="Email account or phone number").fill("roman.test@post.cz")
    page.get_by_role("button", name="Continue").click()
    expect(page.get_by_role("textbox", name="Password"))
    page.get_by_role("textbox", name="Password").fill("@TEst1234")
    page.get_by_role("button", name="Sign in").click()
    expect(page.get_by_label("Navigace ve schránce")).to_contain_text("Doručené")
    # expect(page.get_by_role("link", name="Doručené")).to_be_focused()
    expect(page.get_by_label("Navigace ve schránce")).to_contain_text("Kontakty")
    page.get_by_role("link", name="Kontakty").click()
    expect(page.get_by_role("textbox", name="Hledat e-mail, přílohu či"))
    page.get_by_role("textbox", name="Hledat e-mail, přílohu či").fill("roven")
    expect(page.get_by_label("Výpis zpráv")).to_contain_text("Roman Rovenskyroman.rovensky@gmail.com")
    page.get_by_role("link", name="Roman Rovensky roman.rovensky").click()
    page.locator("textarea").click()
    expect(page.get_by_role("button", name="Psát se vším všudy ›"))
    page.get_by_role("button", name="Psát se vším všudy ›").click()
    expect(page.get_by_placeholder("Předmět…")).to_be_visible()
    page.get_by_placeholder("Předmět…").click()
    page.get_by_placeholder("Předmět…").fill("testovny email")
    page.locator("div").filter(has_text=re.compile(r"^PřílohyMůžete ještě přidat přílohy o velikosti \.$")).locator("div").first.click()
    page.locator("div").filter(has_text=re.compile(r"^PřílohyMůžete ještě přidat přílohy o velikosti \.$")).locator("div").first.fill("Ahoj,\ntoto je len test\n\n\nS pozdravom,\nRoman")
    page.get_by_label("Psaní e-mailu").get_by_role("button", name="Odeslat e-mail").click()
    expect(page.get_by_role("link", name="Odeslané"))
    page.get_by_role("link", name="Odeslané").click()
    expect(page.get_by_role("link", name="Roman Rovensky").first)
    page.get_by_role("link", name="Roman Rovensky").first.click()
    expect(page.get_by_role("heading", name="testovny email"))
    expect(page.locator("#detail").get_by_text("Ahoj, toto je len test S"))


# Then Steps
@then("I can see my Inbox")
def inbox_shown(page: Page):
    expect(page.get_by_role("link", name="Doručené"))


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://playwright.dev/")
    yield

    print("after the test runs")