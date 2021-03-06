# -*- coding: utf-8 -*-
class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not ((len(wd.find_elements_by_link_text("Create account")) > 0)
                and (len(wd.find_elements_by_link_text("Forgot password")) > 0)):
            wd.get(self.app.base_url)

    def turn_to_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("add")) > 0
                and wd.find_element_by_xpath("//*[contains(text(), 'Number of results')]")):
            wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("add")) > 0
                and wd.find_element_by_xpath("//*[contains(text(), 'Number of results')]")):
            wd.find_element_by_link_text("home page").click()

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("group page").click()

    def open_contact_edit_page_by_id(self, id):
        wd = self.app.wd
        if not wd.current_url.endswith("/edit.php?id=%s" % id):
            wd.get(self.app.base_url+"/edit.php?id=%s" % id)

    def open_group_page_by_id(self, id):
        wd = self.app.wd
        if not wd.current_url.endswith("/?group=%s" % id):
            wd.get(self.app.base_url+"?group=%s" % id)

