# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from data.contact_data import testdata


@pytest.mark.parametrize("input_contact", testdata, ids=[repr(i) for i in testdata])
def test_add_contact(app, input_contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(input_contact)
    # Test validation
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(input_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
