#!/usr/bin/env python3
"""This module provides functions for authenticating users."""

from unittest import TestCase
from mock import patch
from mock.mock import mock_open

USER_FILE_LOCATION = '/etc/users.txt'

MOCK_FILE_DATA = "shane|pass\nben|jedi\nhannah|pink\n"

def login(username, password):
    """Check that the credentials offered are in the users file.

       username: This is the username for the user.
       password: This is the password for the user."""
    print('Opening file')
    with open(USER_FILE_LOCATION) as user_file:
        print("Reading the details")
        user_buf = user_file.read()
    print('Read: %s' % (user_buf))
    users = [line.split("|") for line in user_buf.split("\n")]
    print(users)
    if [username, password] in users:
        return True
    else:
        return False


# Add testing to ensure this module works
class AuthenticationTests(TestCase):
    """Ensure that the authentication module works as expected."""

    @patch('%s.open' % __name__, mock_open(read_data=MOCK_FILE_DATA), create=True)
    def test_login(self):
        """Test the login function."""
        open_name = '%s.open' % __name__
        print("Overloaded name for open is %s" % (open_name))

        self.assertTrue(login('shane', 'pass'))

    @patch('%s.open' % __name__, mock_open(read_data=MOCK_FILE_DATA), create=True)
    def test_login_no_user(self):
        """Test that login will fail when the user is unknown."""
        self.assertFalse(login("fred", "pass"))
        