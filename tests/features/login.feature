Feature: Seznam Account Login
    Tests for checking login to seznam account

    Scenario: Login to seznam account
        Given seznam default login page is open
        When I enter my valid Seznam login and Password and hit Sign in
        Then I can see my Inbox
