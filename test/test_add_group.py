# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from data.group_data import constant as testdata


@pytest.mark.parametrize("input_group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, input_group):
    old_groups = app.group.get_group_list()
    app.group.create(input_group)
    # Test validation
    assert len(old_groups) + 1 == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups.append(input_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
