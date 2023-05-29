from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture
def test_del_contact_from_group(app):
    db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")
    groups = db.get_group_list()
    contacts = db.get_contact_list()

    if len(contacts) == 0:
        app.contact.create(Contact(first_name="contt", middle_name="m_name1"))
        contacts = db.get_contact_list()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
        groups = db.get_group_list()

    group = random.choice(groups)
    contact = random.choice(contacts)

    if len(db.get_contacts_in_group(group)) == 0:
        app.contact.add_contact_to_group(contact.id, group.id)
    else:
        contact = random.choice(db.get_contacts_in_group(group))

    app.contact.delete_contact_from_group(contact.id, group.id)
    assert contact in db.get_contacts_not_in_group(group)
