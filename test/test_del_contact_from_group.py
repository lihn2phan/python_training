import random
from fixture.orm import ORMFixture
def test_del_contact_from_group(app):
    db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    if contact in db.get_contacts_not_in_group(group):
        app.contact.add_contact_to_group(contact.id, group.id)

    app.contact.delete_contact_from_group(contact.id, group.id)
    assert contact in db.get_contacts_not_in_group(group)
