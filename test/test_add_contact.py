# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", last_name="", address="",
                    homephone="", mobilephone="", workphone="",
                    secondaryphone="", email="", email2="", email3="")] \
           + [Contact(first_name=random_string("name", 10), last_name=random_string("name", 10),
                      address=random_string("name", 10), homephone=random_string("name", 11),
                      mobilephone=random_string("name", 11), workphone=random_string("name", 11),
                      secondaryphone=random_string("name", 11), email=random_string("name", 10),
                      email2=random_string("name", 10), email3=random_string("name", 10))
              for i in range(5)
              ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()

    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
