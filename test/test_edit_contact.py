# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="Отредактирован", middlename="Отредактирович",
                                         lastname="Отредактированский", nickname="Редактор",
                                         companyname='ОАО "Редакция и Мир"', address="редакторский городок",
                                         homenumber="567-22-04", worknumber="456", email1="glavred@mir.ur",
                                         notes="Здесь могла бы быть ваша реклама", email2="",
                                         birth_date="//div[@id='content']/form/select[1]//option[2]",
                                         birth_month="//div[@id='content']/form/select[2]//option[2]", birth_year="",
                                         anniversary_date="//div[@id='content']/form/select[3]//option[2]",
                                         anniversary_month="//div[@id='content']/form/select[4]//option[2]"))
    app.session.logout()
