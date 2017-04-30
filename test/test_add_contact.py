# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts, db, check_ui):
    input_contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(input_contact)
    # Test validation
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(input_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = map(app.contact.clean, db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
