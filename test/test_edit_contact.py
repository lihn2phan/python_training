from model.contact import Contact


def test_edit_first_group(app):
    contact1 = Contact(first_name="f_name_e",
                       middle_name="m_name_e",
                       last_name="l_name1_e",
                       nickname="nickname1_e",
                       photo_path="C:\\fakepath\\1.jpg",
                       title="title1_e",
                       company="company1_e",
                       address="address1_e",
                       home="home1_e",
                       mobile="mobile1_e",
                       work="work1_e",
                       fax="fax1_e",
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
                       secondary_home="sec_home1_e",
                       secondary_notes="sec_notes1_e")

    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(contact1)
    app.session.logout()