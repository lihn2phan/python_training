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
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_fields(contact)
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        s = int(wd.find_element_by_xpath("//span[@id='search_count']").text)
        d = 5
        return int(wd.find_element_by_xpath("//span[@id='search_count']").text)
