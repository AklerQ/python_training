# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="For modify", birth_date="//div[@id='content']/form/select[1]//option[1]",
                           birth_month="//div[@id='content']/form/select[2]//option[1]",
                           anniversary_date="//div[@id='content']/form/select[3]//option[1]",
                           anniversary_month="//div[@id='content']/form/select[4]//option[1]"))
    old_contacts = app.contact.get_contact_list()
    input_contact = Contact(firstname="Отредактирован", middlename="Отредактирович",
                                         lastname="Отредактированский", nickname="Редактор",
                                         companyname='ОАО "Редакция и Мир"', address="редакторский городок",
                                         homenumber="567-22-04", worknumber="456", email="glavred@mir.ur",
                                         notes="Здесь могла бы быть ваша реклама", email2="",
                                         birth_date="//div[@id='content']/form/select[1]//option[4]",
                                         birth_month="//div[@id='content']/form/select[2]//option[5]", birth_year="",
                                         anniversary_date="//div[@id='content']/form/select[3]//option[6]",
                                         anniversary_month="//div[@id='content']/form/select[4]//option[7]",
                                         mobilenumber="12345678", secondarynumber="(098)76543")
    input_contact.id = old_contacts[0].id
    app.contact.edit_first_contact(input_contact)
    # Test validation
    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = input_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_contact_by_index(app):
    if app.contact.count_contacts() == 0:
        app.contact.create(Contact(firstname="For modify", birth_date="//div[@id='content']/form/select[1]//option[1]",
                           birth_month="//div[@id='content']/form/select[2]//option[1]",
                           anniversary_date="//div[@id='content']/form/select[3]//option[1]",
                           anniversary_month="//div[@id='content']/form/select[4]//option[1]"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
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
    input_contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, input_contact)
    # Test validation
    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = input_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
