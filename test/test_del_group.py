# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="For delete", header="For delete", footer="For delete"))
    app.group.delete_first_group()
