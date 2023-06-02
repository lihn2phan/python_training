import re
from model.contact import Contact
def test_all_contact_fields(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_from_home_page) == len(contacts_from_db)
    count = len(contacts_from_home_page)
    for i in range(count):
        contact_from_home_page = contacts_from_home_page[i]
        contact_from_db = contacts_from_db[i]
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_db)
        assert clear_repeat_spaces(contact_from_home_page.address) == clear_repeat_spaces(contact_from_db.address)
        assert contact_from_home_page.first_name == clear_repeat_spaces(contact_from_db.first_name)
        assert contact_from_home_page.last_name == clear_repeat_spaces(contact_from_db.last_name)


def clear(s):
    return re.sub("[() -]", "", s)
def clear_repeat_spaces(s):
    return " ".join(s.split())

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear_repeat_spaces(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x:clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))
