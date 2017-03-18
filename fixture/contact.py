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

    def fill_contact_fields(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.companyname)
        self.change_field_value("address", contact.address)
        # fill communication data
        self.change_field_value("home", contact.homenumber)
        self.change_field_value("work", contact.worknumber)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
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

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.navigation.turn_to_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        # Здесь повторно используется метод TURN вместо RETURN, так как после удаления
        # не доступен переход по ссылке home_page
        self.app.navigation.turn_to_home_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.app.navigation.turn_to_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_fields(contact)
        wd.find_element_by_xpath("//input[@name='update'][@value='Update']").click()
        self.app.navigation.return_to_home_page()

    def count_contacts(self):
        wd = self.app.wd
        self.app.navigation.turn_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))
