# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_contact_by_index(app, db, check_ui):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="For modify", birth_date="//div[@id='content']/form/select[1]//option[1]",
                           birth_month="//div[@id='content']/form/select[2]//option[1]",
                           anniversary_date="//div[@id='content']/form/select[3]//option[1]",
                           anniversary_month="//div[@id='content']/form/select[4]//option[1]"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    input_contact = Contact(firstname="Отредактирован", middlename="Отредактирович",
                                         lastname="Отредактированский", nickname="Редактор",
                                         companyname='ОАО "Редакция и Мир"', address="редакторский городок",
                                         homenumber="567-22-04", worknumber="45+6", email="glavred@mir.ur",
                                         notes="Здесь могла бы быть ваша реклама", email2="",
                                         birth_date="//div[@id='content']/form/select[1]//option[4]",
                                         birth_month="//div[@id='content']/form/select[2]//option[5]", birth_year="",
                                         anniversary_date="//div[@id='content']/form/select[3]//option[6]",
                                         anniversary_month="//div[@id='content']/form/select[4]//option[7]",
                                         mobilenumber="12345678", secondarynumber="(098)76543")
    input_contact.id = contact.id
    app.contact.edit_contact_by_id(contact.id, input_contact)
    # Test validation
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    idx = int(old_contacts.index(contact))
    old_contacts[idx] = input_contact
    assert old_contacts == new_contacts
    if check_ui:
        new_contacts = map(app.contact.clean, db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
