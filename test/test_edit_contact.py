# -*- coding: utf-8 -*-
from model.contact import Contact


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
                                         homenumber="567-22-04", worknumber="456", email1="glavred@mir.ur",
                                         notes="Здесь могла бы быть ваша реклама", email2="",
                                         birth_date="//div[@id='content']/form/select[1]//option[4]",
                                         birth_month="//div[@id='content']/form/select[2]//option[5]", birth_year="",
                                         anniversary_date="//div[@id='content']/form/select[3]//option[6]",
                                         anniversary_month="//div[@id='content']/form/select[4]//option[7]")
    app.contact.edit_first_contact(input_contact)
    # Test validation
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = input_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


