from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.navigation.turn_to_home_page()
        # create new contact
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_fields(contact)
        # submit created contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.navigation.return_to_home_page()
        self.contact_cache = None

    def fill_contact_fields(self, contact):
        wd = self.app.wd
        # fill personal data
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.companyname)
        self.change_field_value("address", contact.address)
        # fill communication data
        self.change_field_value("home", contact.homenumber)
        self.change_field_value("mobile", contact.mobilenumber)
        self.change_field_value("work", contact.worknumber)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("phone2", contact.secondarynumber)
        # fill dates
        if not wd.find_element_by_xpath(contact.birth_date).is_selected():
            wd.find_element_by_xpath(contact.birth_date).click()
        if not wd.find_element_by_xpath(contact.birth_month).is_selected():
            wd.find_element_by_xpath(contact.birth_month).click()
        self.change_field_value("byear", contact.birth_year)
        if not wd.find_element_by_xpath(contact.anniversary_date).is_selected():
            wd.find_element_by_xpath(contact.anniversary_date).click()
        if not wd.find_element_by_xpath(contact.anniversary_month).is_selected():
            wd.find_element_by_xpath(contact.anniversary_month).click()
        # fill contact commentary
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.turn_to_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        # Здесь повторно используется метод TURN вместо RETURN, так как после удаления
        # не доступен переход по ссылке home_page
        self.app.navigation.turn_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_fields(contact)
        wd.find_element_by_xpath("//input[@name='update'][@value='Update']").click()
        self.app.navigation.return_to_home_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def count_contacts(self):
        wd = self.app.wd
        self.app.navigation.turn_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.navigation.turn_to_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_css_selector('tr[name=entry]'):
                cells = row.find_elements_by_css_selector('td')
                id = cells[0].find_element_by_css_selector('input').get_attribute('value')
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones, all_email_from_home_page=all_email))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.turn_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.turn_to_home_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr["+str(index+2)+"]/td[8]/a/img").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        homenumber = wd.find_element_by_name('home').get_attribute('value')
        mobilenumber = wd.find_element_by_name('mobile').get_attribute('value')
        worknumber = wd.find_element_by_name('work').get_attribute('value')
        secondarynumber = wd.find_element_by_name('phone2').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        return Contact(id=id, firstname=firstname, lastname=lastname, homenumber=homenumber, mobilenumber=mobilenumber,
                       worknumber=worknumber, secondarynumber=secondarynumber, address=address, email=email,
                       email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homenumber = re.search("H: (.*)", text)
        if homenumber is not None:
            homenumber = homenumber.group(1)
        worknumber = re.search("W: (.*)", text)
        if worknumber is not None:
            worknumber = worknumber.group(1)
        mobilenumber = re.search("M: (.*)", text)
        if mobilenumber is not None:
            mobilenumber = mobilenumber.group(1)
        secondarynumber = re.search("P: (.*)", text)
        if secondarynumber is not None:
            secondarynumber = secondarynumber.group(1)
        return Contact(homenumber=homenumber, worknumber=worknumber, mobilenumber=mobilenumber, secondarynumber=secondarynumber)
