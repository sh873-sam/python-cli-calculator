import pytest

from app.calculator.repl import Session, handle_command, parse_number


def test_parse_number_valid():
    assert parse_number("2") == 2.0
    assert parse_number("2.5") == 2.5


def test_parse_number_invalid():
    with pytest.raises(ValueError):
        parse_number("abc")


def test_handle_command_help():
    session = Session()
    out = handle_command("help", session)
    assert out is not None
    assert "Commands" in out


def test_handle_command_history_empty():
    session = Session()
    assert handle_command("history", session) == "No calculations yet."


def test_handle_command_history_with_items():
    session = Session()
    session.add_history("add(1, 2) = 3")
    assert "add(1, 2) = 3" in handle_command("history", session)


def test_handle_command_exit():
    session = Session()
    assert handle_command("exit", session) == "exit"


def test_handle_command_unknown_returns_none():
    session = Session()
    assert handle_command("add", session) is None
