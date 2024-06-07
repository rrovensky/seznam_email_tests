from playwright.sync_api import Page, expect
import os
import sys

# ROOT_DIR = os.path.dirname(os.path.abspath('__file__'))
#
# try:
#     sys.path.index(f'{ROOT_DIR}')
# except ValueError:
#     sys.path.append(f'{ROOT_DIR}')

class SeznamNavigationMenu:
    DORUCENE_LINK = 'Doručené'
    KONTAKTY_LINK = 'Kontakty'

    def __init__(self, page: Page):
        self.page = page

    def verify_left_menu_links(self):
        expect(self.page.get_by_label("Navigace ve schránce")).to_contain_text(self.DORUCENE_LINK)
        expect(self.page.get_by_label("Navigace ve schránce")).to_contain_text(self.KONTAKTY_LINK)
        expect(self.page.get_by_role("link", name=self.DORUCENE_LINK))
        expect(self.page.get_by_role("link", name=self.KONTAKTY_LINK))

    def click_dorucene_link(self):
        self.page.get_by_role("link", name=self.DORUCENE_LINK).click()

    def click_kontakty_link(self):
        self.page.get_by_role("link", name=self.KONTAKTY_LINK).click()


class EnterLoginDetails:
    def __init__(self, page: Page, user, pwd):
        self.page = page
        self.user = user
        self.pwd = pwd

    def enter_login(self):
        expect(self.page.get_by_role("textbox", name="Email account or phone number"))
        self.page.get_by_role("textbox", name="Email account or phone number").fill(self.user)
        self.page.get_by_role("button", name="Continue").click()

    def enter_pwd(self):
        expect(self.page.get_by_role("textbox", name="Password"))
        self.page.get_by_role("textbox", name="Password").fill(self.pwd)
        self.page.get_by_role("button", name="Sign in").click()
