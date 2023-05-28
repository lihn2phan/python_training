from model.contact import Contact
from random import randrange
import random

def test_edit_some_contact(app, db, check_ui):
    contact1 = Contact(first_name="f_name_e",
                       middle_name="m_name_e",
                       last_name="5555",
                       nickname="nickname1_e",
                       photo_path="C:\\fakepath\\1.jpg",
                       title="title1_e",
                       company="company1_e",
                       address="address1_e",
                       homephone="home1_e",
                       mobilephone="mobile1_e",
                       workphone="work1_e",
                       faxphone="fax1_e",
                       email="emaill1_e", email2="emaill2_e", email3="emaill3_e",
                       homepage="homepage1_e",
                       birthday_day="4",
                       birthday_month="January",
                       birthday_year="2001",
                       anniversary_day="10",
                       anniversary_month="July",
                       anniversary_year="2001",
                       group="group1_e",
                       secondary_address="sec_addr1_e",
                       secondaryphone="sec_home1_e",
                       secondary_notes="sec_notes1_e")

    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="contt", middle_name="m_name1"))

    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)

    contact1.id = contact.id
    app.contact.modify_contact_by_id(contact.id, contact1)
    old_contacts.remove(contact)
    old_contacts.append(contact1)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
