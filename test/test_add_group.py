# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, data_group_data):
    input_group = data_group_data
    old_groups = app.group.get_group_list()
    app.group.create(input_group)
    # Test validation
    assert len(old_groups) + 1 == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups.append(input_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
