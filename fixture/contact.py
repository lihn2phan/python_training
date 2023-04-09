class ContactHelper:
    def __init__(self, app):
        self.app = app
    def fill_field(self, name_element, text):
        wd = self.app.wd
        wd.find_element_by_name(name_element).click()
        wd.find_element_by_name(name_element).clear()
        wd.find_element_by_name(name_element).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
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
        self.fill_field("address2", contact.secondary_address)
        self.fill_field("phone2", contact.secondary_home)
        self.fill_field("notes", contact.secondary_notes)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.open_home_page()