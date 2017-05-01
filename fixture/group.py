# -*- coding: utf-8 -*-
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_fields(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.app.navigation.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.app.navigation.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def edit_group_by_index(self, index, input_group):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_group_by_index(index)
        # init group edition
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_fields(input_group)
        # submit group edition
        wd.find_element_by_name("update").click()
        self.app.navigation.return_to_groups_page()
        self.group_cache = None

    def edit_first_group(self, input_group):
        self.edit_group_by_index(0, input_group)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def fill_group_fields(self, input_group):
        self.change_field_value("group_name", input_group.name)
        self.change_field_value("group_header", input_group.header)
        self.change_field_value("group_footer", input_group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count_groups(self):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.app.navigation.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.app.navigation.return_to_groups_page()
        self.group_cache = None

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_group_by_id_for_add_to(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath('//select[@name="to_group"]/option[@value="%s"]' % id).click()

    def clean(self, group):
        return Group(id=group.id, name=group.name.strip())

    def edit_group_by_id(self, id, input_group):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_group_by_id(id)
        # init group edition
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_fields(input_group)
        # submit group edition
        wd.find_element_by_name("update").click()
        self.app.navigation.return_to_groups_page()
        self.group_cache = None
