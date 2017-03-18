# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="Edit name", header="Edit header", footer="Edit footer"))


def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name="Modify name"))


def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header="Modify header"))


def test_edit_first_group_footer(app):
    app.group.edit_first_group(Group(footer="Modify footer"))

