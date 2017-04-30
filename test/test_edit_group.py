# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_edit_first_group_footer(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="For modification", header="For modification", footer="For modification"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    input_group = Group(name="Modify name", header="Modify header", footer="Modify footer")
    app.group.edit_group_by_id(group.id, input_group)
    # Test validation
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    idx = int(old_groups.index(group))
    old_groups[idx] = input_group
    assert old_groups == new_groups
    if check_ui:
        new_groups = map(app.group.clean, db.get_group_list())
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
