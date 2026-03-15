import pytest

from src.processing import (filter_by_state,  # Замените на ваш путь к файлу
                            sort_by_date)


@pytest.fixture
def sample_data():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 2, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 3, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 4, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}  # Одинаковая дата с id 2
    ]


def test_filter_by_state_executed(sample_data):
    """Проверка фильтрации по умолчанию (EXECUTED)"""
    result = filter_by_state(sample_data)
    assert len(result) == 3
    assert all(x['state'] == 'EXECUTED' for x in result)


def test_filter_by_state_canceled(sample_data):
    """Проверка фильтрации по статусу CANCELED"""
    result = filter_by_state(sample_data, state='CANCELED')
    assert len(result) == 1
    assert result[0]['id'] == 3


def test_sort_by_date_descending(sample_data):
    """Проверка сортировки по убыванию (от новых к старым)"""
    sorted_data = sort_by_date(sample_data, reverse=True)
    assert sorted_data[0]['id'] == 1  # 2019 год
    assert sorted_data[-1]['id'] in [2, 4]  # 2018 год (июнь)


def test_sort_by_date_ascending(sample_data):
    """Проверка сортировки по возрастанию (от старых к новым)"""
    sorted_data = sort_by_date(sample_data, reverse=False)
    assert sorted_data[0]['id'] in [2, 4]  # 2018 год (июнь)
    assert sorted_data[-1]['id'] == 1  # 2019 год


def test_sort_by_date_same_dates():
    """Проверка корректности при абсолютно одинаковых датах"""
    data = [
        {'id': 1, 'date': '2023-01-01T10:00:00.000'},
        {'id': 2, 'date': '2023-01-01T10:00:00.000'}
    ]
    sorted_data = sort_by_date(data)
    assert len(sorted_data) == 2
    assert sorted_data[0]['date'] == sorted_data[1]['date']


def test_sort_by_date_invalid_format():
    """Тест на некорректный формат даты (должен вызвать ValueError)"""
    invalid_data = [{'id': 1, 'date': '01.01.2023'}]
    with pytest.raises(ValueError):
        sort_by_date(invalid_data)


def test_sort_by_date_missing_key():
    """Тест на отсутствие ключа 'date' в словаре"""
    incomplete_data = [{'id': 1, 'state': 'EXECUTED'}]
    with pytest.raises(KeyError):
        sort_by_date(incomplete_data)
