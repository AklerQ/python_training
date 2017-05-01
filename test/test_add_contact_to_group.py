# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact
from fixture.orm import ORMfixture
import random

orm = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    # Проверка на наличие групп
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="For adds contact", header="For adds contact", footer="For adds contact"))
    # Проверка на наличие свободных контактов
    if len(db.get_contacts_out_groups()) == 0:
        app.contact.create(Contact(firstname="Тест_добавления", lastname="Тест_для_добавления",
                           birth_date="//div[@id='content']/form/select[1]//option[1]",
                           birth_month="//div[@id='content']/form/select[2]//option[1]",
                           anniversary_date="//div[@id='content']/form/select[3]//option[1]",
                           anniversary_month="//div[@id='content']/form/select[4]//option[1]",
                           new_group="//select[@name='new_group']/option[@value='[none]']"))
    contact_list = db.get_contacts_out_groups()
    contact = random.choice(contact_list)
    group_list = db.get_group_list()
    group = random.choice(group_list)
    app.navigation.turn_to_home_page()
    app.contact.select_contact_by_id(contact.id)
    app.group.select_group_by_id_for_add_to(group.id)
    app.contact.add_contact_to_group()
    app.navigation.open_group_page_by_id(group.id)
    # test validation
    assert contact in list(orm.get_contacts_in_group(group))
    assert contact not in list(db.get_contacts_out_groups())


