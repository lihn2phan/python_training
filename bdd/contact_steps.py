from pytest_bdd import given, when, then, parsers
from model.contact import Contact
from time import sleep
import random


@given('a contact list', target_fixture="contact_list")
def contact_list(db):
    return db.get_contact_list()
@given('a not empty contact list', target_fixture="not_empty_contact_list")
def not_empty_contact_list(app, db):
    lst = db.get_contact_list()
    if len(lst) == 0:
        app.contact.create(Contact(first_name="first_name", last_name="last_name"))
    return db.get_contact_list()

@given(parsers.parse('a contact with {first_name}, {last_name}, {address}, {homephone}, {mobilephone}, {workphone}, '
                     '{secondaryphone}, {email}, {email2}, {email3}'), target_fixture='new_contact')
def new_contact(first_name, last_name, address, homephone, mobilephone, workphone, secondaryphone, email, email2,
                email3):
    return Contact(first_name=first_name, last_name=last_name, address=address, homephone=homephone,
                   mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone,
                   email=email, email2=email2, email3=email3)


@given('a random contact from contact list', target_fixture="random_contact_from_list")
def random_contact_from_list(not_empty_contact_list):
    return random.choice(not_empty_contact_list)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@when('I delete the contact')
def delete_contact(app, random_contact_from_list):
    app.contact.delete_contact_by_id(random_contact_from_list.id)


@when('I edit the contact')
def delete_contact(app, random_contact_from_list, new_contact):
    app.contact.modify_contact_by_id(random_contact_from_list.id, new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@then('the new contact list is equal to the old list with the removed contact')
def verify_contact_removed(db, not_empty_contact_list, random_contact_from_list):
    old_contacts = not_empty_contact_list
    old_contacts.remove(random_contact_from_list)
    sleep(0.5)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

@then('the new contact list is equal to the old list with the edited contact')
def verify_contact_edited(db, not_empty_contact_list, random_contact_from_list, new_contact):
    old_contacts = not_empty_contact_list
    old_contacts.remove(random_contact_from_list)
    old_contacts.append(new_contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)