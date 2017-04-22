# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts):
    input_contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(input_contact)
    # Test validation
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(input_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
