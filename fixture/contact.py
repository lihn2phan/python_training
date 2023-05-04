from model.contact import Contact


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
        self.fill_field("home", contact.home)
        self.fill_field("mobile", contact.mobile)
        self.fill_field("work", contact.work)
        self.fill_field("fax", contact.fax)
        self.fill_field("email", contact.email)
        self.fill_field("email2", contact.email2)
        self.fill_field("email3", contact.email3)
        self.fill_field("homepage", contact.homepage)
        self.fill_field("address2", contact.secondary_address)
        self.fill_field("phone2", contact.secondary_home)
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
            t = len(list(wd.find_elements_by_name("entry")))
            for element in wd.find_elements_by_name("entry"):
                lname = element.find_element_by_xpath("./td[2]").text
                fname = element.find_element_by_xpath("./td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(first_name=fname,last_name=lname, id=id))
        return list(self.contact_cache)
