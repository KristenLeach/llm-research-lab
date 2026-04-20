"""Tests for src/checks.py validation helpers."""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.checks import (
    check_equal,
    check_type,
    check_contains,
    check_not_contains,
    check_approx,
    check_length,
    check_keys,
)


# --- check_equal ---

def test_check_equal_passes(capsys):
    check_equal(42, 42, "test")
    captured = capsys.readouterr()
    assert "✓" in captured.out


def test_check_equal_fails():
    with pytest.raises(AssertionError) as exc_info:
        check_equal(1, 2, "test")
    assert "Expected" in str(exc_info.value)
    assert "Got" in str(exc_info.value)


def test_check_equal_strings():
    check_equal("hello", "hello")


def test_check_equal_strings_fails():
    with pytest.raises(AssertionError):
        check_equal("hello", "world")


# --- check_type ---

def test_check_type_passes(capsys):
    check_type(42, int, "int check")
    captured = capsys.readouterr()
    assert "✓" in captured.out


def test_check_type_fails():
    with pytest.raises(AssertionError) as exc_info:
        check_type("hello", int)
    assert "str" in str(exc_info.value)


def test_check_type_list():
    check_type([1, 2, 3], list)


def test_check_type_dict():
    check_type({"a": 1}, dict)


# --- check_contains ---

def test_check_contains_passes(capsys):
    check_contains([1, 2, 3], 2)
    captured = capsys.readouterr()
    assert "✓" in captured.out


def test_check_contains_fails():
    with pytest.raises(AssertionError):
        check_contains([1, 2, 3], 99)


def test_check_contains_string():
    check_contains("hello world", "world")


def test_check_contains_dict_keys():
    check_contains({"a": 1, "b": 2}, "a")


# --- check_not_contains ---

def test_check_not_contains_passes(capsys):
    check_not_contains([1, 2, 3], 99)
    captured = capsys.readouterr()
    assert "✓" in captured.out


def test_check_not_contains_fails():
    with pytest.raises(AssertionError):
        check_not_contains([1, 2, 3], 1)


# --- check_approx ---

def test_check_approx_passes(capsys):
    check_approx(3.14159, 3.14159)
    captured = capsys.readouterr()
    assert "✓" in captured.out


def test_check_approx_within_tolerance():
    check_approx(1.0000001, 1.0, tolerance=1e-5)


def test_check_approx_fails():
    with pytest.raises(AssertionError):
        check_approx(1.0, 2.0)


# --- check_length ---

def test_check_length_passes(capsys):
    check_length([1, 2, 3], 3)
    captured = capsys.readouterr()
    assert "✓" in captured.out


def test_check_length_fails():
    with pytest.raises(AssertionError) as exc_info:
        check_length([1, 2], 5)
    assert "Expected length" in str(exc_info.value)


def test_check_length_string():
    check_length("hello", 5)


# --- check_keys ---

def test_check_keys_passes(capsys):
    check_keys({"a": 1, "b": 2}, ["a", "b"])
    captured = capsys.readouterr()
    assert "✓" in captured.out


def test_check_keys_missing():
    with pytest.raises(AssertionError) as exc_info:
        check_keys({"a": 1}, ["a", "b"])
    assert "Missing keys" in str(exc_info.value)


def test_check_keys_extra():
    with pytest.raises(AssertionError) as exc_info:
        check_keys({"a": 1, "b": 2, "c": 3}, ["a", "b"])
    assert "Unexpected keys" in str(exc_info.value)
