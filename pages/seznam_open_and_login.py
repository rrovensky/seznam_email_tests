from playwright.sync_api import Page, expect
import os
import sys


# ROOT_DIR = os.path.dirname(os.path.abspath('__file__'))
#
# try:
#     sys.path.index(f'{ROOT_DIR}')
# except ValueError:
#     sys.path.append(f'{ROOT_DIR}')

class OpenSeznam:
    def __init__(self, page: Page):
        self.page = page

    def open_seznam(self):
        """Opens the default Seznam email login page"""
        self.page.goto("https://email.seznam.cz")
        expect(self.page.get_by_role("textbox", name="Email account or phone number"))


class LoginToSeznam:
    def __init__(self, page: Page, user="roman.test@post.cz ", pwd="@TEst1234"):
        self.page = page
        self.user = user
        self.pwd = pwd

    def enter_login(self):
        """Method checks if field for entering account ID present, fills in the ID and confirms"""
        expect(self.page.get_by_role("textbox", name="Email account or phone number"))
        self.page.get_by_role("textbox", name="Email account or phone number").fill(self.user)
        self.page.get_by_role("button", name="Continue").click()

    def enter_pwd(self):
        """Method checks if field for entering password present, fills in the pwd and confirms"""
        expect(self.page.get_by_role("textbox", name="Password"))
        self.page.get_by_role("textbox", name="Password").fill(self.pwd)
        self.page.get_by_role("button", name="Sign in").click()
