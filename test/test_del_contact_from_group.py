# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact
from fixture.orm import ORMfixture
import random

db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_contact_from_group(app):
    # Проверка на наличие групп
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="For adds contact", header="For adds contact", footer="For adds contact"))
    group_list = db.get_group_list()
    group = random.choice(group_list)
    # Проверка на наличие контактов в группе
    if len(db.get_contacts_in_group(group)) == 0:
        app.contact.create(Contact(firstname="Тест_добавления", lastname="Тест_для_добавления",
                           birth_date="//div[@id='content']/form/select[1]//option[1]",
                           birth_month="//div[@id='content']/form/select[2]//option[1]",
                           anniversary_date="//div[@id='content']/form/select[3]//option[1]",
                           anniversary_month="//div[@id='content']/form/select[4]//option[1]",
                           new_group="//select[@name='new_group']/option[@value='%s']" % group.id))
    app.navigation.open_group_page_by_id(group.id)
    contacts_list = db.get_contacts_in_group(group)
    contact = random.choice(contacts_list)
    app.contact.select_contact_by_id(contact.id)
    app.contact.delete_contact_from_group()
    app.navigation.open_group_page_by_id(group.id)
    # test validation
    assert contact in list(db.get_contacts_not_in_group(group))
    assert contact not in list(db.get_contacts_in_group(group))
