from data_base.data_base import Con


class Users:
    def __init__(self):
        self.id_user = None
        self.user = None
        self.password = None

    def create_user(self):
        pass

    def delete_user(self):
        pass

    def set_user(self):
        cnx = Con().con()
        with cnx.cursor() as c:
            c.execute(f"SELECT * FROM users WHERE (user = '{self.user}') AND (password = '{self.password}')")
            if c.fetchone():
                return self
            else:
                return self


user_session = Users()