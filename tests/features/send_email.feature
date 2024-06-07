Feature: Seznam Account Login
    Tests for checking login to seznam account

    Scenario: Sending email from Seznam account
        Given user is logged in to his/her Seznam account
        When a contact is picked from Kontakty
        And email composed and sent
        Then this email is visible in Odoslane folder