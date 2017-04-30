# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_delete_first_contact(app, db, check_ui):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="Тест_имени", lastname="Тест_фамилии",
                           birth_date="//div[@id='content']/form/select[1]//option[1]",
                           birth_month="//div[@id='content']/form/select[2]//option[1]",
                           anniversary_date="//div[@id='content']/form/select[3]//option[1]",
                           anniversary_month="//div[@id='content']/form/select[4]//option[1]"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    # Test validation
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        new_contacts = map(app.contact.clean, db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
