# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_edit_first_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="For modification", header="For modification", footer="For modification"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    input_group = Group(name="Edit name", header="Edit header", footer="Edit footer")
    input_group.id = old_groups[index].id
    app.group.edit_group_by_index(index, input_group)
    # Test validation
    assert len(old_groups) == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups[index] = input_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# Вариант 1: редактирование первой группы через edit_group_by_index с index=0
def test_edit_first_group_name(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="For modification", header="For modification", footer="For modification"))
    old_groups = app.group.get_group_list()
    index = 0
    input_group = Group(name="Modify name")
    input_group.id = old_groups[index].id
    app.group.edit_group_by_index(index, input_group)
    # Test validation
    assert len(old_groups) == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups[index] = input_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# Вариант 2: редактирование первой группы через edit_first_group с index=0
def test_edit_first_group_header(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="For modification", header="For modification", footer="For modification"))
    old_groups = app.group.get_group_list()
    index = 0
    input_group = Group(header="Modify header")
    input_group.id = old_groups[index].id
    app.group.edit_first_group(input_group)
    # Test validation
    assert len(old_groups) == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups[index] = input_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# Вариант 3: редактирование первой группы через edit_first_group без index
def test_edit_first_group_footer(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name="For modification", header="For modification", footer="For modification"))
    old_groups = app.group.get_group_list()
    input_group = Group(footer="Modify footer")
    input_group.id = old_groups[0].id
    app.group.edit_first_group(input_group)
    # Test validation
    assert len(old_groups) == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups[0] = input_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
