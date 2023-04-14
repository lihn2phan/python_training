from model.group import Group


def test_edit_first_group(app):
    app.group.modify_first_group(Group(name="e_name", header="e_head", footer="e_foot"))

def test_edit_first_group_name(app):
    app.group.modify_first_group(Group(name="new_group_name"))

def test_edit_first_group_header(app):
    app.group.modify_first_group(Group(header="new_group_header"))