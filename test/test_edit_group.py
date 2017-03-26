# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="For modification", header="For modification", footer="For modification"))
    old_groups = app.group.get_group_list()
    input_group = Group(name="Edit name", header="Edit header", footer="Edit footer")
    input_group.id = old_groups[0].id
    app.group.edit_first_group(input_group)
    # Test validation
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = input_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_first_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="For modification", header="For modification", footer="For modification"))
    old_groups = app.group.get_group_list()
    input_group = Group(name="Modify name")
    input_group.id = old_groups[0].id
    app.group.edit_first_group(input_group)
    # Test validation
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = input_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_first_group_header(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="For modification", header="For modification", footer="For modification"))
    old_groups = app.group.get_group_list()
    input_group = Group(header="Modify header")
    input_group.id = old_groups[0].id
    app.group.edit_first_group(input_group)
    # Test validation
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = input_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_first_group_footer(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="For modification", header="For modification", footer="For modification"))
    old_groups = app.group.get_group_list()
    input_group = Group(footer="Modify footer")
    input_group.id = old_groups[0].id
    app.group.edit_first_group(input_group)
    # Test validation
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = input_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
