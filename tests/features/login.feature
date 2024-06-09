Feature: Seznam Email Account Login
    Tests for checking login to seznam email account

    Scenario Outline: Login to seznam email account
        Given seznam default login page is open
        When I enter valid Seznam <login> and <password> and hit Sign in
        Then I see Seznam Inbox

        Examples:
        |   login                       |   password    |
        |   roman.test@post.cz          |   @TEst1234   |
        |   roman.nonexistent@post.cz   |   fake1234    |