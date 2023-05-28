import random
from model.contact import Contact


def test_delete_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="contt", middle_name="m_name1"))

    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    old_contacts.remove(contact)
    new_contacts = db.get_contact_list()
    c = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


