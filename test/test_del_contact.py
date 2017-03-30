# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_delete_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="Тест_имени", lastname="Тест_фамилии",
                           birth_date="//div[@id='content']/form/select[1]//option[1]",
                           birth_month="//div[@id='content']/form/select[2]//option[1]",
                           anniversary_date="//div[@id='content']/form/select[3]//option[1]",
                           anniversary_month="//div[@id='content']/form/select[4]//option[1]"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    # Test validation
    assert len(old_contacts) - 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
