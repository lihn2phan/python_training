import pymysql.cursors
from model.group import Group
class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        # при конструировании фикстуры сразу устанавливаем соединение с бд
        self.connection = pymysql.connect\
            (host="127.0.0.1", database="addressbook", user="root", password="", autocommit=True)

    # преобразуем данные из базы в список объектов
    def get_group_list(self):
        cursor = self.connection.cursor()
        groups = []
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                groups.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return groups
    def destroy(self):
        # разрываем соединение
        self.connection.close()