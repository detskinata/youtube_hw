import pytest
from main import *


def test_str():
    ch1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    assert ch1.__str__() == ('Youtube-канал: вДудь')


def test_lt():
    ch1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    ch2 = Channel('UC1eFXmJNkjITxPFWTy6RsWg')
    assert (ch1.subscriber_count > ch2.subscriber_count) is True


def test_add():
    ch1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    ch2 = Channel('UC1eFXmJNkjITxPFWTy6RsWg')
    assert ch1.subscriber_count + ch2.subscriber_count == 14010000
