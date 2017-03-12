# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Иван", middlename="Иванович", lastname="Иванов", nickname="Ваня",
                        companyname="Иван и Ко", address="посёлок Иваново", homenumber="543-66-12", worknumber=
                        "+7(456)1-14-15", email1="mail@ivan.io", email2="ivanov@ivan.io",
                        birth_date="//div[@id='content']/form/select[1]//option[16]",
                        birth_month="//div[@id='content']/form/select[2]//option[8]", birth_year="1987",
                        anniversary_date="//div[@id='content']/form/select[3]//option[20]",
                        anniversary_month="//div[@id='content']/form/select[4]//option[12]", notes="Текст заметки"))
    app.session.logout()
