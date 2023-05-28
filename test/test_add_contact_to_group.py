from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture
def test_add_contact_to_group(app):
    db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    if len(contacts) == 0:
        app.contact.create(Contact(first_name="contt", middle_name="m_name1"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contact = random.choice(contacts)
    group = random.choice(groups)
    app.contact.add_contact_to_group(contact.id, group.id)
    assert contact in db.get_contacts_in_group(group)
