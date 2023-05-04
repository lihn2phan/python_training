from model.group import Group

def test_edit_first_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))

    group = Group(name="new_group_name")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

'''

def test_edit_first_group_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(header="new_group_header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_edit_first_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="e_name", header="e_head", footer="e_foot")
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="e_name", header="e_head", footer="e_foot"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
'''