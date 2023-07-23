import json
import pytest
import utils

import main


@pytest.fixture
def test_data():
    with open(main.data_file, 'rt', encoding='utf-8') as data_file:
        return json.loads("".join(data_file.readlines()))


@pytest.fixture
def test_data_ok():
    result = []
    with open(main.data_file, 'rt', encoding='utf-8') as data_file:
        for item in json.loads("".join(data_file.readlines())):
            if item:
                result.append(item)
    return result


@pytest.fixture
def test_6_items():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
    ]

def test_get_date():
    assert utils.format_date('2018-07-11T02:26:18.671407') == '11.07.2018'

def test_mask_from_to_msg():
    assert utils.add_mask('Visa Gold 9447344650495960') == 'Visa Gold 9447 34** **** 5960'
    assert utils.add_mask('Visa Platinum 2241653116508487') == 'Visa Platinum 2241 65** **** 8487'
    assert utils.add_mask('Visa Classic 7022985698476865') == 'Visa Classic 7022 98** **** 6865'
    assert utils.add_mask('Maestro 8045769817179061') == 'Maestro 8045 76** **** 9061'
    assert utils.add_mask('MasterCard 3152479541115065') == 'MasterCard 3152 47** **** 5065'
    assert utils.add_mask('МИР 8201420097886664') == 'МИР 8201 42** **** 6664'
    assert utils.add_mask('Счет 14073196441261107791') == 'Счет **7791'