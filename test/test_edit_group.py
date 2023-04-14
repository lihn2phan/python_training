from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="e_name", header="e_head", footer="e_foot"))
    app.session.logout()