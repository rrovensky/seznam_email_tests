Feature: Sending email from Seznam Account
    Tests for checking the ability to send email from Seznam account

    Scenario: User can send email from seznam account
        Given User is logged in to Seznam account
        When a contact is picked from Kontakty
        When email composed and sent
        Then email is in Odeslane folder
