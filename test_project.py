import pytest
from project import showOptions, funCaller

def test_showOptions():
    assert showOptions(["View", "Insert", "Search"], "1") == 0
    assert showOptions(["View", "Insert", "Search"], "View") == 0

def test_funCaller():
    assert funCaller([1, 2, 3], 0) == "1()"
    assert funCaller(["View", 2, 3], 0) == "View()"