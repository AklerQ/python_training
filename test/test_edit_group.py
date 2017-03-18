# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="For modification", header="For modification", footer="For modification"))
    app.group.edit_first_group(Group(name="Edit name", header="Edit header", footer="Edit footer"))


def test_edit_first_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="For modification", header="For modification", footer="For modification"))
    app.group.edit_first_group(Group(name="Modify name"))


def test_edit_first_group_header(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="For modification", header="For modification", footer="For modification"))
    app.group.edit_first_group(Group(header="Modify header"))


def test_edit_first_group_footer(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="For modification", header="For modification", footer="For modification"))
    app.group.edit_first_group(Group(footer="Modify footer"))
