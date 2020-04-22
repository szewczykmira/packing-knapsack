from math import comb  # type: ignore

from ..combinations_v1 import create_all as algorithm1
from ..combinations_v2 import create_all as algorithm2


def test_generate_all_combinations_returns_proper_amount(items):
    items_len = len(items)
    combinations = algorithm1(items)
    expected_output = sum([comb(items_len, i) for i in range(1, items_len + 1)])
    assert len(combinations) == expected_output


def test_generate_all_combinations_with_itertools(items):
    items_len = len(items)
    combinations = algorithm2(items)
    expected_output = sum([comb(items_len, i) for i in range(1, items_len + 1)])
    assert len(combinations) == expected_output