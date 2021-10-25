import pytest

from ddg import PRESIDENTS, presidents_search
presidents_ddg = presidents_search()

def test_for_presidents():
    for president in PRESIDENTS:
        assert president in presidents_ddg