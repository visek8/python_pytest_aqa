import pytest

from main import area_calculator
from pytest import fixture, mark


@fixture()
def set_up():
    print('Start test')


class TestArea:
    @mark.usefixtures("set_up")
    def test_one(self):
        s_one, s_two, year = area_calculator(8, 9)
        assert s_one == 512
        assert s_two == 6561
        assert year == 7

    def test_two(self):
        result = area_calculator(" ", " ")
        assert result == "Error", "Arguments are None"

    @mark.parametrize('a,b,r_1,r_2,r_3', ([1, 5, 4, 45, 3],
                                          [8, 9, 512, 6561, 7]))
    def test_three(self, a, b, r_1, r_2, r_3):
        res_1, res_2, res_3 = area_calculator(a, b)
        assert res_1 == r_1
        assert res_2 == r_2
        assert res_3 == r_3


@pytest.fixture(scope="function", autouse=True)
def connect_to_db():
    print('connected')
    yield
    print('disconnect')

class TestDB:
    def test_db(self):
        assert True
    def test_db_2(self):
        assert True
    def test_db_3(self):
        assert True
