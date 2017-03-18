# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Edit name", header="Edit header", footer="Edit footer"))
    app.session.logout()


def test_edit_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Modify name"))
    app.session.logout()


def test_edit_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="Modify header"))
    app.session.logout()


def test_edit_first_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(footer="Modify footer"))
    app.session.logout()

