# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from contact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()

    def test_add_contact(self):
        self.login()
        contact1 = Contact(first_name="f_name1",
                           middle_name="m_name1",
                           last_name="l_name1",
                           nickname="nickname1",
                           photo_path="C:\\fakepath\\1.jpg",
                           title="title1",
                           company="company1",
                           address="address1",
                           home="home1",
                           mobile="mobile1",
                           work="work1",
                           fax="fax1",
                           email="emaill1", email2="emaill2", email3="emaill3",
                           homepage="homepage1",
                           birthday_day="1",
                           birthday_month="January",
                           birthday_year="2000",
                           anniversary_day="5",
                           anniversary_month="July",
                           anniversary_year="2000",
                           group="group1",
                           secondary_address="sec_addr1",
                           secondary_home="sec_home1",
                           secondary_notes="sec_notes1")
        self.create_user(contact1)
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def fill_field(self, name_element, text):
        wd = self.wd
        wd.find_element_by_name(name_element).click()
        wd.find_element_by_name(name_element).clear()
        wd.find_element_by_name(name_element).send_keys(text)

    def create_user(self, contact):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_field("firstname", contact.first_name)
        self.fill_field("middlename", contact.middle_name)
        self.fill_field("lastname", contact.last_name)
        self.fill_field("nickname", contact.nickname)
        self.fill_field("title", contact.title)
        self.fill_field("company", contact.company)
        self.fill_field("address", contact.address)
        self.fill_field("home", contact.home)
        self.fill_field("mobile", contact.mobile)
        self.fill_field("work", contact.work)
        self.fill_field("fax", contact.fax)
        self.fill_field("email", contact.email)
        self.fill_field("email2", contact.email2)
        self.fill_field("email3", contact.email3)
        self.fill_field("homepage", contact.homepage)

        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birthday_day)
        wd.find_element_by_xpath(f"//option[@value='{contact.birthday_day}']").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birthday_month)
        self.fill_field("byear", contact.birthday_year)

        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        self.fill_field("ayear", contact.anniversary_year)

        self.fill_field("address2", contact.secondary_address)
        self.fill_field("phone2", contact.secondary_home)
        self.fill_field("notes", contact.secondary_notes)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.open_home_page()

    def login(self):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()