import pymysql.cursors
from model.group import Group
from model.contact import Contact
class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        # при конструировании фикстуры сразу устанавливаем соединение с бд
        self.connection = pymysql.connect\
            (host="127.0.0.1", database="addressbook", user="root", password="", autocommit=True)

    # преобразуем данные из базы в список объектов
    def get_group_list(self):
        cursor = self.connection.cursor()
        groups = []
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                groups.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return groups
    def get_contact_list(self):
        cursor = self.connection.cursor()
        contacts = []
        try:
            cursor.execute("select id, firstname, lastname, home, mobile, work, phone2, email, email2, email3, address from addressbook")
            for row in cursor:
                (id, firstname, lastname, homephone, mobilephone, workphone, secondaryphone, email, email2, email3, address) = row
                contact = Contact(id=str(id), first_name=firstname, last_name=lastname, homephone=homephone,
                        mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone,
                        email=email, email2=email2, email3=email3, address=address)
                contacts.append(contact)
        finally:
            cursor.close()
        return contacts
    def destroy(self):
        # разрываем соединение
        self.connection.close()