# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    contact = Contact(first_name="Ivan",
                       middle_name="m_name1",
                       last_name="Petrov",
                       nickname="nickname1",
                       photo_path="C:\\fakepath\\1.jpg",
                       title="title1",
                       company="company1",
                       address="address1",
                       homephone="home1",
                       mobilephone="mobile1",
                       workphone="work1",
                       faxphone="fax1",
                       email="emaill1", email2="emaill2", email3="emaill3",
                       homepage="homepage1",
                       birthday_day="1",
                       birthday_month="January",
                       birthday_year="2000",
                       anniversary_day="5",
                       anniversary_month="July",
                       anniversary_year="2000",
                       group="group1",
                       secondary_address="sec_addr1",
                       secondaryphone="sec_home1",
                       secondary_notes="sec_notes1")


    old_contacts = app.contact.get_contact_list()

    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)






