from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, companyname=None, address=None,
                 homenumber=None, mobilenumber=None, worknumber=None, faxnumber=None, email1=None, email2=None,
                 birth_date=None, birth_month=None, birth_year=None, anniversary_date=None, anniversary_month=None,
                 secondarynumber=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.companyname = companyname
        self.address = address
        self.homenumber = homenumber
        self.mobilenumber = mobilenumber
        self.worknumber = worknumber
        self.faxnumber = faxnumber
        self.email1 = email1
        self.email2 = email2
        self.birth_date = birth_date
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.anniversary_date = anniversary_date
        self.anniversary_month = anniversary_month
        self.secondarynumber = secondarynumber
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None) and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
