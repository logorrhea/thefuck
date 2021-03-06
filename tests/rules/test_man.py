import pytest
from thefuck.rules.man import match, get_new_command
from tests.utils import Command


@pytest.mark.parametrize('command', [
    Command('man read'),
    Command('man 2 read'),
    Command('man 3 read'),
    Command('man -s2 read'),
    Command('man -s3 read'),
    Command('man -s 2 read'),
    Command('man -s 3 read')])
def test_match(command):
    assert match(command, None)


@pytest.mark.parametrize('command', [
    Command('man'),
    Command('man ')])
def test_not_match(command):
    assert not match(command, None)


@pytest.mark.parametrize('command, new_command', [
    (Command('man read'), ['man 3 read', 'man 2 read']),
    (Command('man 2 read'), 'man 3 read'),
    (Command('man 3 read'), 'man 2 read'),
    (Command('man -s2 read'), 'man -s3 read'),
    (Command('man -s3 read'), 'man -s2 read'),
    (Command('man -s 2 read'), 'man -s 3 read'),
    (Command('man -s 3 read'), 'man -s 2 read')])
def test_get_new_command(command, new_command):
    assert get_new_command(command, None) == new_command
