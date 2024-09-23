"""Tests for the app module."""

import pytest
from src.app import get_message


def test_get_message_contains_hello():
    message = get_message().lower()
    pytest.assume("hello" in message)


def test_get_message_contains_world():
    message = get_message().lower()
    pytest.assume("world" in message)


if __name__ == "__main__":
    pytest.main()
