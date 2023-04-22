from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="contt", middle_name="m_name1"))
    app.contact.delete_first_contact()
