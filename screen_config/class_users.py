from data_base.data_base import con
from screen_config.cf_first_config import FirstConfig


class Users:
    def __init__(self):
        self.id_user = None
        self.user = None
        self.password = None
        self.email = None

    def create_user(self):
        pass

    def delete_user(self):
        pass

    def set_user(self):
        try:
            cnx = con()
            with cnx.cursor() as c:
                c.execute(f"SELECT * FROM users WHERE (user = '{self.user}') AND (password = '{self.password}')")
                if c.fetchone():
                    return self
                else:
                    return False
        except Exception as e:
            print(e)
            FirstConfig()
