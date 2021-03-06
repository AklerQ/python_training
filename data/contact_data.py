from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    symbols = string.digits + ")" + "(" + "-" + " "
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(maxlen):
    symbols = string.ascii_lowercase + string.digits + "_" + "-"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))] + ['@'] + [random.choice(symbols)
                                           for i in range(random.randrange(maxlen))] + ['.', 'ru'])


def random_date(maxlen):
    return str(random.randrange(maxlen))


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", companyname="", address="",
                               homenumber="", worknumber="", email="", email2="",
                               birth_date="//div[@id='content']/form/select[1]//option[1]",
                               birth_month="//div[@id='content']/form/select[2]//option[1]", birth_year="",
                               anniversary_date="//div[@id='content']/form/select[3]//option[1]",
                               anniversary_month="//div[@id='content']/form/select[4]//option[1]", notes="",
                               mobilenumber="", secondarynumber="")] + [
Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string
("lastname", 10), nickname=random_string("nickname", 10), companyname=random_string("companyname", 10), address=
random_string("address", 25), homenumber=random_number(9), mobilenumber=random_number(12), worknumber=random_number(12),
email=random_email(6), email2=random_email(7), email3=random_email(8),
birth_date="//div[@id='content']/form/select[1]//option["+random_date(32)+"]",
birth_month="//div[@id='content']/form/select[2]//option["+random_date(13)+"]", birth_year=random_number(4),
anniversary_date="//div[@id='content']/form/select[3]//option["+random_date(32)+"]", notes=random_string("name", 30),
anniversary_month="//div[@id='content']/form/select[4]//option["+random_date(13)+"]", secondarynumber=random_number(12))
            for i in range(5)]