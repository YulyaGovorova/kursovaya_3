from tests.settings import PATH_WITH_FIXTURES
from tests.utils import get_operations, get_executed_operations


def test_get_operations():
    assert isinstance(get_operations(PATH_WITH_FIXTURES), list)

def test_get_executed_operations(valid_data):
    assert get_executed_operations(valid_data) == []

