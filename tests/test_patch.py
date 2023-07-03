from pytest_mock import MockerFixture

from notes.not_reliable_func import DbConnector
from notes import not_reliable_func

import pytest


def test_fail(mocker):
    connector = DbConnector()

    def custom_random():
        return 0.3

    # not_reliable_func.random = custom_random
    mocker.patch.object(not_reliable_func, 'random', side_effect=custom_random)

    with pytest.raises(AssertionError, match='connection error'):
        connector.get_data()

    not_reliable_func.random.called
    not_reliable_func.random.call_count


def test_success(mocker: MockerFixture):
    connector = DbConnector()

    def connector_stub():
        ...

    # connector.connect = connector_stub
    mocker.patch.object(connector, 'connect', side_effect=connector_stub)

    assert connector.get_data() == 'some data'


# def test__():
#     connector = DbConnector()
#
#     connector.get_data()


def test_fail_monkey(monkeypatch):
    connector = DbConnector()

    def custom_random():
        return 0.3

    # not_reliable_func.random = custom_random
    monkeypatch.setattr(not_reliable_func, 'random', value=custom_random)

    with pytest.raises(AssertionError, match='connection error'):
        connector.get_data()
