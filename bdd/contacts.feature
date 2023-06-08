# Given - предусловие, то что должно быть написано перед началом сценария
# When - действие, которое нужно выполнить
# Then - результат, то что должно получиться после выполнения действия

Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <first_name>, <last_name>, <address>, <homephone>, <mobilephone>, <workphone>, <secondaryphone>, <email>, <email2>, <email3>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | first_name   | last_name  | address  | homephone  | mobilephone  | workphone  | secondaryphone  | email  | email2  | email3  |
  | first_name44 | last_name1 | address1 | homephone1 | mobilephone1 | workphone1 | secondaryphone1 | email1 | email21 | email31 |
  | first_name55 | last_name2 | address2 | homephone2 | mobilephone2 | workphone2 | secondaryphone2 | email2 | email22 | email32 |



Scenario Outline: Delete contact
  Given a not empty contact list
  Given a random contact from contact list
  When I delete the contact
  Then the new contact list is equal to the old list with the removed contact


Scenario Outline: Edit contact
  Given a not empty contact list
  Given a random contact from contact list
  Given a contact with <first_name>, <last_name>, <address>, <homephone>, <mobilephone>, <workphone>, <secondaryphone>, <email>, <email2>, <email3>
  When I edit the contact
  Then the new contact list is equal to the old list with the edited contact
  Examples:
    | first_name   | last_name  | address  | homephone  | mobilephone  | workphone  | secondaryphone  | email  | email2  | email3  |
    | first_name_e | last_name_e | address_e | homephone_e | mobilephone_e | workphone_e | secondaryphone_e | email_e | email2_e | email3_e |
