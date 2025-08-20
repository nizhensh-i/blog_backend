# # src/chapter-2/test_nodeid.py
#
# import pytest
#
#
# def test_one():
#     print('test_one')
#     assert 1
#
#
# class TestNodeId:
#     def test_one(self):
#         print('TestNodeId::test_one')
#         assert 1
#
#     @pytest.mark.parametrize('x,y', [(1, 1), (3, 4)])
#     def test_two(self, x, y):
#         print(f'TestNodeId::test_two::{x} == {y}')
#         assert x == y

# def a(x):
#     return x
#
# def test_a():
#     assert a(3)%2 ==0,"value is odd,should be even"


# src/chapter-4/test_ids.py
import pytest
def idfn(fixture_value):
    if fixture_value == 0:
        return "eggs"
    elif fixture_value == 1:
        return False
    elif fixture_value == 2:
        return None
    else:
        return fixture_value


@pytest.fixture(params=[0, 1, 2, 3], ids=idfn)
def b(request):
    return request.param


def test_b(b):
    pass