from playwright.sync_api import Page, expect
import re
import time


class WriteAndSendEmail:
    def __init__(self, page: Page, email_to="rovensky"):
        self.page = page
        self.email_to = email_to
        self.email_title = f'title_{time.time()}'

    def find_contact(self):
        """Opens Kontakty section of Seznam email account and finds contact"""
        self.page.get_by_role("link", name="Kontakty").click()
        expect(self.page.get_by_role("textbox", name="Hledat e-mail, přílohu či"))
        self.page.get_by_role("textbox", name="Hledat e-mail, přílohu či").fill(self.email_to)
        expect(self.page.get_by_label("Výpis zpráv")).to_contain_text(self.email_to)
        self.page.get_by_role("link", name="Roman Rovensky roman.rovensky").click()

    def email_composed_and_sent(self):
        """Composes email with Title, message body and sends it"""
        self.page.locator("textarea").click()
        expect(self.page.get_by_role("button", name="Psát se vším všudy ›"))
        self.page.get_by_role("button", name="Psát se vším všudy ›").click()
        expect(self.page.get_by_placeholder("Předmět…")).to_be_visible()
        self.page.get_by_placeholder("Předmět…").click()
        self.page.get_by_placeholder("Předmět…").fill(self.email_title)
        self.page.locator("div").filter(
            has_text=re.compile(r"^PřílohyMůžete ještě přidat přílohy o velikosti \.$")).locator(
            "div").first.click()
        self.page.locator("div").filter(
            has_text=re.compile(r"^PřílohyMůžete ještě přidat přílohy o velikosti \.$")).locator(
            "div").first.fill("Ahoj,\ntoto je len test\n\nS pozdravom,\nRoman")
        self.page.get_by_label("Psaní e-mailu").get_by_role("button", name="Odeslat e-mail").click()

    def check_email_sent(self):
        """Moves to Odeslane folder of Seznam account and checks for recent email sent"""
        expect(self.page.get_by_role("link", name="Odeslané"))
        self.page.get_by_role("link", name="Odeslané").click()
        expect(self.page.get_by_role("link", name="Roman Rovensky").first)
        self.page.get_by_role("link", name="Roman Rovensky").first.click()
        expect(self.page.get_by_role("heading", name=self.email_title))
        expect(self.page.locator("#detail").get_by_text("Ahoj, toto je len test S"))
