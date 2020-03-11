import os
import tempfile

import pytest

def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ))


def logout(client):
    return client.get('/logout')

def test_login_logout(client):
    """Make sure login and logout works."""

    rv = login(client, os.environ.get("USERNAME_TEST"), os.environ.get("PASSWORD_TEST"))
    assert b'You were logged in' in rv.data

    rv = logout(client)
    assert b'logged out' in rv.data

    rv = login(client, os.environ.get("USERNAME_TEST") + 'x', os.environ.get("PASSWORD_TEST"))
    assert b'wrong username or password' in rv.data

    rv = login(client, os.environ.get("USERNAME_TEST"), os.environ.get("PASSWORD_TEST") + 'x')
    assert b'wrong username or password' in rv.data