class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, photo_path=None,
                 title = None, company = None, address=None, home=None, mobile=None,
                 work=None, fax=None, email=None, email2=None, email3=None, homepage=None,
                 birthday_day=None, birthday_month=None, birthday_year=None,
                 anniversary_day=None, anniversary_month=None, anniversary_year=None, group=None,
                 secondary_address=None, secondary_home=None, secondary_notes=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.photo = photo_path
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.birthday_year = birthday_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.group = group
        self.secondary_address = secondary_address
        self.secondary_home = secondary_home
        self.secondary_notes = secondary_notes