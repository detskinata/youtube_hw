import pytest
from main import Channel, Video, PLVideo


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


def test_video_init():
    video1 = Video('9lO06Zxhu88')
    assert video1.video_id == '9lO06Zxhu88'
    assert video1.video_title == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'


def test_video_str():
    video1 = Video('9lO06Zxhu88')
    video1.__str__() == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'


def test_plvideo_init():
    video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    assert video2.playlist_title == 'Литература'

def test_plvideo_str():
    video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    video2.__str__() == 'Пушкин: наше все? (Литература)'