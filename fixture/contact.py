from model.contact import Contact
import re
from selenium.webdriver.support.ui import Select

class ContactHelper:
    def __init__(self, app):
        self.app = app
    def fill_field(self, name_element, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(name_element).click()
            wd.find_element_by_name(name_element).clear()
            wd.find_element_by_name(name_element).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_fields(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def fill_fields(self, contact):
        self.fill_field("firstname", contact.first_name)
        self.fill_field("middlename", contact.middle_name)
        self.fill_field("lastname", contact.last_name)
        self.fill_field("nickname", contact.nickname)
        self.fill_field("title", contact.title)
        self.fill_field("company", contact.company)
        self.fill_field("address", contact.address)
        self.fill_field("home", contact.homephone)
        self.fill_field("mobile", contact.mobilephone)
        self.fill_field("work", contact.workphone)
        self.fill_field("fax", contact.faxphone)
        self.fill_field("email", contact.email)
        self.fill_field("email2", contact.email2)
        self.fill_field("email3", contact.email3)
        self.fill_field("homepage", contact.homepage)
        self.fill_field("address2", contact.secondary_address)
        self.fill_field("phone2", contact.secondaryphone)
        self.fill_field("notes", contact.secondary_notes)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()
        self.contact_cache = None
    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector(f"input[value='{id}'").click()
    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()
        self.contact_cache = None
    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath(f"//tr[@name='entry'][{index+1}]/td[8]/a").click()
        self.fill_fields(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector(f"a[href*='{id}']")[1].click()
        self.fill_fields(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        s = int(wd.find_element_by_xpath("//span[@id='search_count']").text)
        d = 5
        return int(wd.find_element_by_xpath("//span[@id='search_count']").text)


    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                self.contact_cache.append(Contact(first_name=firstname, last_name=lastname, id=id,
                                                  address = address, all_email_from_home_page=all_email,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    #открывает форму редактирования контакта
    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    #открывает страницу детального просмотра информации о контакте
    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_to_edit_by_index(index)
        wd = self.app.wd
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")

        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")

        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        id = wd.find_element_by_name("id").get_attribute("value")
        return Contact(first_name=firstname, last_name=lastname, id = id, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, secondaryphone= secondaryphone,
                       email = email, email2 = email2, email3 = email3, address = address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H:(.*)", text).group(1)
        workphone = re.search("W:(.*)", text).group(1)
        mobilephone = re.search("M:(.*)", text).group(1)
        secondaryphone = re.search("P:(.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("to_group").click()
        dropdown = wd.find_element_by_name("to_group")
        se = Select(dropdown)
        dropdown_item = se.select_by_value(group_id)
        wd.find_element_by_name("add").click()

    def delete_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("group").click()
        dropdown = wd.find_element_by_name("group")
        Select(dropdown).select_by_value(group_id)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()

