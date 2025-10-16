import pytest
import helper
import datetime


def test_add():
    # Given: I want to add a to-do with a date
    text = "Lorem ipsum"
    date = "2023-09-02"

    # When: I add the item
    helper.add(text, date)

    # Then: The most recently added to-do should have a date
    item = helper.items[-1]
    assert isinstance(item.date, datetime.date)

def test_add_with_description():
    # Given: I want to add a to-do with a description
    text = "Test task"
    date = "2023-09-02"
    description = "This is a test description"

    # When: I add the item with description
    helper.add(text, date, description)

    # Then: The most recently added to-do should have the correct description
    item = helper.items[-1]
    assert item.description == description