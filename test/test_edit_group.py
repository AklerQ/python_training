# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="For modification", header="For modification", footer="For modification"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="Edit name", header="Edit header", footer="Edit footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="For modification", header="For modification", footer="For modification"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="Modify name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_header(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="For modification", header="For modification", footer="For modification"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="Modify header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_footer(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="For modification", header="For modification", footer="For modification"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(footer="Modify footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
