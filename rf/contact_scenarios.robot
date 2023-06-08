*** Settings ***
Library  rf.Addressbook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures

*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact   first_name   last_name   address   homephone   mobilephone   workphone   secondaryphone   email   email2  email3
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List    ${old_list}  ${contact}
    Group Lists Should Be Equal  ${new_list}  ${old_list}

Delete contact
    ${old_list}=  Get Not Empty Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List    ${old_list}    ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Edit contact
    ${old_list}=  Get Not Empty Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List    ${old_list}    ${index}
    ${new_contact}=  New Contact   efirst_name   elast_name   eaddress   ehomephone   emobilephone   eworkphone   esecondaryphone   eemail   eemail2  eemail3
    Edit Contact  ${contact}  ${newcontact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Append To List    ${old_list}  ${new_contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}