import psycopg2
from sql import sql_functions, sql_admin_functions


class DataBase:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.is_created = False
        self.is_damaged = False

    def connect(self):
        self.connection = psycopg2.connect(database="hearthstone", user="postgres", password="postgres",
                                           host="127.0.0.1", port="5432")
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.cursor.execute(sql_functions)

    def create_database(self):
        try:
            if not self.is_created:
                self.connection = psycopg2.connect(user="postgres", password="postgres",
                                                   host="127.0.0.1", port="5432")
                self.connection.autocommit = True
                self.cursor = self.connection.cursor()
                self.cursor.execute(sql_admin_functions)
                self.cursor.execute(f"""SELECT create_database()""")
                self.connection.close()
                self.connect()
                self.cursor.execute(f"""SELECT create_cards_info()""")
                self.cursor.execute(f"""SELECT create_fixes_info()""")
                self.is_created = True
                return True
        except BaseException as e:
            print(e)
            self.is_damaged = True
            return False
        else:
            return False

    def delete_database(self):
        self.connection = psycopg2.connect(user="postgres", password="postgres",
                                           host="127.0.0.1", port="5432")
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.cursor.execute(sql_functions)
        self.cursor.execute(f"""SELECT delete_database()""")
        self.is_created = False
        if self.is_damaged is True:
            self.is_damaged = False
            self.delete_database()

    ####################################################################################################################

    def get_cards(self):
        self.cursor.execute(f"""SELECT * FROM get_cards()""")

    def clean_cards(self):
        self.cursor.execute(f"""SELECT clear_cards()""")

    def add_card(self, id_=-1, name="", rarity=0, manacost=0, description="", attack=0, health=0):
        self.cursor.execute(
            f"""SELECT add_card({id_}, '{name}', {rarity}, {manacost}, '{description}', {attack}, {health})""")

    def edit_card(self, id_=-1, name="", rarity=0, manacost=0, description="", attack=0, health=0):
        self.cursor.execute(
            f"""SELECT edit_card({id_}, '{name}', {rarity}, {manacost}, '{description}', {attack}, {health})""")

    def delete_card_by_id(self, id_):
        self.cursor.execute(f"""SELECT delete_card_by_id({id_})""")

    def delete_card_by_name(self, name):
        self.cursor.execute(f"""SELECT delete_card_by_name('{name}')""")

    ####################################################################################################################

    def get_fixes(self):
        self.cursor.execute(f"""SELECT * FROM get_fixes()""")

    def find_card(self, name):
        self.cursor.execute(f"""SELECT * FROM find_card('{name}')""")

    def clean_fix(self):
        self.cursor.execute(f"""SELECT clear_fixes()""")

    def add_fix(self, id_=-1, fix_name="", fix_prize=0, card_id=-1):
        self.cursor.execute(f"""SELECT add_fix({id_}, '{fix_name}', {fix_prize}, {card_id})""")

    def edit_fix(self, id_=-1, fix_name="", fix_prize=0, card_id=-1):
        self.cursor.execute(f"""SELECT edit_fix({id_}, '{fix_name}', {fix_prize}, {card_id})""")

    def find_fix(self, fix_name):
        self.cursor.execute(f"""SELECT * FROM find_fix('{fix_name}')""")

    def delete_fix_by_id(self, id_):
        self.cursor.execute(f"""SELECT delete_fix_by_id({id_})""")

    def delete_fix_by_name(self, fix_name):
        self.cursor.execute(f"""SELECT delete_fix_by_name('{fix_name}')""")
