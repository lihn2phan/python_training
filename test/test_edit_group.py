from model.group import Group
from random import randrange
def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="new_group_name55")

    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)

    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    new_groups = app.group.get_group_list()
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