import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from funs import DataBase

cardsWindow, fixesWindow = None, None


def create_database():
    status = db.create_database()

    if not status:
        if db.is_damaged:
            messagebox.showinfo("Information", "DB is Damaged. Sorry")
        else:
            messagebox.showinfo("Information", "DB is already created! Opening DB.")
    global cardsWindow, fixesWindow
    if cardsWindow is None and fixesWindow is None:
        cardsWindow = CardsWindow()
        fixesWindow = Fixes()


def delete_database():
    db.delete_database()

    if cardsWindow is not None:
        cardsWindow.destroy()
        fixesWindow.destroy()
    else:
        messagebox.showerror("Error!", "DB is not found!")


class MainWindow(tk.Frame):
    def __init__(self):
        super().__init__(main_window)
        self.create_db = tk.PhotoImage(file="pics/create_db.png")
        self.delete_db = tk.PhotoImage(file="pics/delete_db.png")

        buttons_bar = tk.Frame(bg='#212121', bd=0)
        buttons_bar.pack(side=tk.TOP, fill=tk.X)
        btn_create_db = tk.Button(buttons_bar,
                                  bd=0,
                                  width=120,
                                  height=120,
                                  text='Create/Open DB',
                                  command=create_database,
                                  bg='#212121',
                                  compound=tk.TOP,
                                  image=self.create_db)
        btn_delete_db = tk.Button(buttons_bar,
                                  bd=0,
                                  width=120,
                                  height=120,
                                  text='Delete DB',
                                  command=delete_database,
                                  bg='#212121',
                                  compound=tk.TOP,
                                  image=self.delete_db)
        btn_create_db.pack(side=tk.LEFT)
        btn_delete_db.pack(side=tk.LEFT)


###################################################################


class CardsWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.columns_cards = (
            "id", "name", "rarity", "manacost", "description", "attack", "health")

        self.add_record = tk.PhotoImage(file="pics/add.png")
        self.edit_record = tk.PhotoImage(file="pics/edit.png")
        self.delete_record = tk.PhotoImage(file="pics/delete.png")
        self.find_record = tk.PhotoImage(file="pics/find.png")

        self.cards_list = ttk.Treeview(self, columns=self.columns_cards, height=100, show="headings")
        for heading in self.columns_cards:
            self.cards_list.heading(heading, text=heading.replace("_", " ").title())
            self.cards_list.column(heading, width=50)

        self.cards_list.bind('<Button>', self.handle_click_cards)

        self.title("Cards Info")
        self.geometry("900x350")

        self.init_buttons()
        self.cards_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.show_cards()

    def init_buttons(self):
        accs_buttons_bar = tk.Frame(master=self, bg='#212121', bd=0, )
        accs_buttons_bar.pack(side=tk.TOP, fill=tk.X)

        accs_btn_add_record = tk.Button(accs_buttons_bar,
                                        bd=0,
                                        text='Add',
                                        command=self.add_record_to_DB,
                                        bg='#212121',
                                        compound=tk.TOP,
                                        image=self.add_record)
        accs_btn_edit_record = tk.Button(accs_buttons_bar,
                                         bd=0,
                                         text='Edit',
                                         command=self.edit_record_in_DB,
                                         bg='#212121',
                                         compound=tk.TOP,
                                         image=self.edit_record)
        accs_btn_delete_record = tk.Button(accs_buttons_bar,
                                           bd=0,
                                           text='Delete',
                                           command=self.delete_records_from_db,
                                           bg='#212121',
                                           compound=tk.TOP,
                                           image=self.delete_record)
        accs_btn_find_record = tk.Button(accs_buttons_bar,
                                         bd=0,
                                         text='Find',
                                         command=self.search_file_in_DB,
                                         bg='#212121',
                                         compound=tk.TOP,
                                         image=self.find_record)

        accs_btn_add_record.pack(side=tk.LEFT)
        accs_btn_edit_record.pack(side=tk.LEFT)
        accs_btn_delete_record.pack(side=tk.LEFT)
        accs_btn_find_record.pack(side=tk.LEFT)

    def handle_click_cards(self, fix):
        if self.cards_list.identify_region(fix.x, fix.y) == "separator":
            return "break"

    def show_cards(self):
        db.get_cards()
        [self.cards_list.delete(i) for i in self.cards_list.get_children()]
        for row in db.cursor.fetchall():
            self.cards_list.insert('', "end", values=row)

    def add_record_to_DB(self):
        AddRecord_Cards(window=self)

    def edit_record_in_DB(self):
        if self.cards_list.selection():
            EditRecord_Cards(window=self, selection=self.cards_list.set(self.cards_list.selection()[0]))

    def delete_records_from_db(self):
        if self.cards_list.selection():
            db.delete_card_by_id(self.cards_list.set(self.cards_list.selection()[0])["id"])
            self.show_cards()
        else:
            Delete_Cards(window=self)

    def search_file_in_DB(self):
        SearchRecord_Cards()


class AddRecord_Cards(tk.Toplevel):
    def __init__(self, window):
        super().__init__()
        self.columns_cards = (
            "id", "name", "rarity", "manacost", "description", "attack", "health")

        self.window = window

        self.entry_id = ttk.Entry(self)
        self.entry_name = ttk.Entry(self)
        self.entry_rarity = ttk.Entry(self)
        self.entry_manacost = ttk.Entry(self)
        self.entry_description = ttk.Entry(self)
        self.entry_attack = ttk.Entry(self)
        self.entry_health = ttk.Entry(self)

        self.button_add = ttk.Button(self, text="Add")
        self.button_cancel = ttk.Button(self, text="Close", command=self.destroy)

        self.init_window_entities()

    def init_window_entities(self):
        self.title("Adding card record to DB")
        self.geometry('360x300+400+300')
        self.resizable(False, False)

        label_id = tk.Label(self, text="ID")
        label_id.place(x=10, y=20)
        label_name = tk.Label(self, text="Name")
        label_name.place(x=10, y=50)
        label_rarity = tk.Label(self, text="Rarity")
        label_rarity.place(x=10, y=80)
        label_manacost = tk.Label(self, text="Manacost")
        label_manacost.place(x=10, y=110)
        label_description = tk.Label(self, text="Description")
        label_description.place(x=10, y=140)
        label_attack = tk.Label(self, text="Attack")
        label_attack.place(x=10, y=170)
        label_health = tk.Label(self, text="Health")
        label_health.place(x=10, y=200)

        self.entry_id.place(x=150, y=20)
        self.entry_name.place(x=150, y=50)
        self.entry_rarity.place(x=150, y=80)
        self.entry_manacost.place(x=150, y=110)
        self.entry_description.place(x=150, y=140)
        self.entry_attack.place(x=150, y=170)
        self.entry_health.place(x=150, y=200)

        self.button_add.place(x=65, y=260)
        self.button_add.bind('<Button-1>',
                             lambda fix: self.adding_record([int(self.entry_id.get()),
                                                               self.entry_name.get(),
                                                               int(self.entry_rarity.get()),
                                                               int(self.entry_manacost.get()),
                                                               self.entry_description.get(),
                                                               int(self.entry_attack.get()),
                                                               int(self.entry_health.get())]))

        self.button_cancel.place(x=200, y=260)

    def adding_record(self, fields_list):
        db.add_card(id_=fields_list[0], name=fields_list[1], rarity=fields_list[2],
                    manacost=fields_list[3], description=fields_list[4], attack=fields_list[5],
                    health=fields_list[6])
        self.window.show_cards()
        fixesWindow.show_fixes()
        self.destroy()


class EditRecord_Cards(tk.Toplevel):
    def __init__(self, window, selection):
        super().__init__()
        self.columns_cards = (
            "id", "name", "rarity", "manacost", "description", "attack", "health")
        self.selection = selection
        self.window = window

        self.entry_id = ttk.Entry(self)
        self.entry_name = ttk.Entry(self)
        self.entry_rarity = ttk.Entry(self)
        self.entry_manacost = ttk.Entry(self)
        self.entry_description = ttk.Entry(self)
        self.entry_attack = ttk.Entry(self)
        self.entry_health = ttk.Entry(self)

        self.button_add = ttk.Button(self, text="Edit")
        self.button_cancel = ttk.Button(self, text="Close", command=self.destroy)

        self.init_window_entities()

    def init_window_entities(self):
        self.title("Editing card record to DB")
        self.geometry('360x300+400+300')
        self.resizable(False, False)

        label_id = tk.Label(self, text="ID")
        label_id.place(x=10, y=20)
        label_name = tk.Label(self, text="Name")
        label_name.place(x=10, y=50)
        label_rarity = tk.Label(self, text="Rarity")
        label_rarity.place(x=10, y=80)
        label_manacost = tk.Label(self, text="Manacost")
        label_manacost.place(x=10, y=110)
        label_description = tk.Label(self, text="Description")
        label_description.place(x=10, y=140)
        label_attack = tk.Label(self, text="Attack")
        label_attack.place(x=10, y=170)
        label_health = tk.Label(self, text="Health")
        label_health.place(x=10, y=200)

        self.entry_id.place(x=150, y=20)
        self.entry_name.place(x=150, y=50)
        self.entry_rarity.place(x=150, y=80)
        self.entry_manacost.place(x=150, y=110)
        self.entry_description.place(x=150, y=140)
        self.entry_attack.place(x=150, y=170)
        self.entry_health.place(x=150, y=200)

        self.entry_id.insert(0, self.selection['id'])
        self.entry_name.insert(0, self.selection['name'])
        self.entry_rarity.insert(0, self.selection['rarity'])
        self.entry_manacost.insert(0, self.selection['manacost'])
        self.entry_description.insert(0, self.selection['description'])
        self.entry_attack.insert(0, self.selection['attack'])
        self.entry_health.insert(0, self.selection['health'])

        self.button_add.place(x=65, y=270)
        self.button_add.bind('<Button-1>',
                             lambda fix: self.editing_record([int(self.entry_id.get()),
                                                                self.entry_name.get(),
                                                                int(self.entry_rarity.get()),
                                                                int(self.entry_manacost.get()),
                                                                self.entry_description.get(),
                                                                int(self.entry_attack.get()),
                                                                int(self.entry_health.get())]))
        self.button_cancel.place(x=200, y=270)

    def editing_record(self, fields_list):
        db.edit_card(id_=fields_list[0], name=fields_list[1], rarity=fields_list[2],
                     manacost=fields_list[3], description=fields_list[4], attack=fields_list[5],
                     health=fields_list[6])
        self.window.show_cards()
        fixesWindow.show_fixes()
        self.destroy()


class Delete_Cards(tk.Toplevel):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.resizable(False, False)
        self.title("Deleting")
        self.geometry('360x100+400+300')

        self.button_delete_all = ttk.Button(self, text="Delete all tables", command=self.delete_all)
        self.button_delete_accs = ttk.Button(self, text="Delete this table", command=self.delete_accs)
        self.button_cancel = ttk.Button(self, text="Close", command=self.destroy)

        self.button_delete_all.place(x=10, y=10)
        self.button_delete_accs.place(x=140, y=10)
        self.button_cancel.place(x=270, y=10)

        self.button_search = ttk.Button(self, text="Delete")

        label_name = tk.Label(self, text="Name")
        label_name.place(x=10, y=50)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=80, y=50)

        self.button_search.place(x=280, y=50)
        self.button_search.bind('<Button-1>',
                                lambda fix: self.delete_record(str(self.entry_name.get())))

    def delete_accs(self):
        db.clean_cards()
        self.window.show_cards()

    def delete_all(self):
        db.clean_cards()
        db.clean_health()
        self.window.show_cards()
        fixesWindow.show_fixes()

    def delete_record(self, name):
        db.delete_card_by_name(name)
        self.window.show_cards()


class SearchResults_Cards(tk.Toplevel):
    def __init__(self, name):
        super().__init__()
        self.columns_cards = (
            "id", "name", "rarity", "manacost", "description", "attack", "health")

        self.name = name

        self.resizable(False, False)
        self.cards_list = ttk.Treeview(self, columns=self.columns_cards, height=100, show="headings")
        for heading in self.columns_cards:
            self.cards_list.heading(heading, text=heading.replace("_", " ").title())
            self.cards_list.column(heading, width=50)

        self.cards_list.bind('<Button>', self.handle_click_cards)

        self.title("Cards Info")
        self.geometry("900x350")

        self.cards_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        db.find_card(name=self.name)
        [self.cards_list.delete(i) for i in self.cards_list.get_children()]
        [self.cards_list.insert('', 'end', values=row) for row in db.cursor.fetchall()]

    def handle_click_cards(self, fix):
        if self.cards_list.identify_region(fix.x, fix.y) == "separator":
            return "break"


class SearchRecord_Cards(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.geometry("300x100")
        self.button_search = ttk.Button(self, text="Search")
        self.title("Finding Cards")

        label_name = tk.Label(self, text="Name")
        label_name.place(x=10, y=20)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=90, y=20)

        self.button_search.place(x=110, y=70)
        self.button_search.bind('<Button-1>',
                                lambda fix: self.search_record(self.entry_name.get()))

    def search_record(self, name):
        SearchResults_Cards(name=name)


###################################################################

class Fixes(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.columns_fix = ("id", "description", "card_id", "gold_compensation")
        self.add_record = tk.PhotoImage(file="pics/add.png")
        self.edit_record = tk.PhotoImage(file="pics/edit.png")
        self.delete_record = tk.PhotoImage(file="pics/delete.png")
        self.find_record = tk.PhotoImage(file="pics/find.png")

        self.title("Fixes info")
        self.geometry("600x350")

        self.fix_list = ttk.Treeview(self, columns=self.columns_fix, height=100, show="headings")
        for heading in self.columns_fix:
            self.fix_list.heading(heading, text=heading.replace("_", " ").title())
            self.fix_list.column(heading, width=50)

        self.fix_list.bind('<Button>', self.handle_click_fix)

        self.init_buttons()
        self.fix_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.show_fixes()

    def init_buttons(self):
        buttons_bar = tk.Frame(master=self, bg='#212121', bd=0)
        buttons_bar.pack(side=tk.TOP, fill=tk.X)

        btn_add_record = tk.Button(buttons_bar,
                                   bd=0,
                                   text='Add',
                                   command=self.add_record_to_DB,
                                   bg='#212121',
                                   compound=tk.TOP,
                                   image=self.add_record)
        btn_edit_record = tk.Button(buttons_bar,
                                    bd=0,
                                    text='Edit',
                                    command=self.edit_record_in_DB,
                                    bg='#212121',
                                    compound=tk.TOP,
                                    image=self.edit_record)
        btn_delete_record = tk.Button(buttons_bar,
                                      bd=0,
                                      text='Delete',
                                      command=self.delete_records_from_db,
                                      bg='#212121',
                                      compound=tk.TOP,
                                      image=self.delete_record)
        btn_find_record = tk.Button(buttons_bar,
                                    bd=0,
                                    text='Find',
                                    command=self.search_file_in_DB,
                                    bg='#212121',
                                    compound=tk.TOP,
                                    image=self.find_record)

        btn_add_record.pack(side=tk.LEFT)
        btn_edit_record.pack(side=tk.LEFT)
        btn_delete_record.pack(side=tk.LEFT)
        btn_find_record.pack(side=tk.LEFT)

    def handle_click_fix(self, fix):
        if self.fix_list.identify_region(fix.x, fix.y) == "separator":
            return "break"

    def show_fixes(self):
        db.get_fixes()
        [self.fix_list.delete(i) for i in self.fix_list.get_children()]
        [self.fix_list.insert('', 'end', values=row) for row in db.cursor.fetchall()]

    def add_record_to_DB(self):
        AddRecord_Fixes(window=self)

    def edit_record_in_DB(self):
        if self.fix_list.selection():
            EditRecord_Fixes(window=self, selection=self.fix_list.set(self.fix_list.selection()[0]))

    def delete_records_from_db(self):
        if self.fix_list.selection():
            db.delete_card_by_id(self.fix_list.set(self.fix_list.selection()[0])["id"])
            self.show_fixes()
        else:
            Delete_Fixes(window=self)

    def search_file_in_DB(self):
        SearchRecord_Fixes()


class EditRecord_Fixes(tk.Toplevel):
    def __init__(self, window, selection):
        super().__init__()
        self.columns_fix = ("id", "new_description", "card_id", "gold_compensation")

        self.entry_id = ttk.Entry(self)
        self.entry_fix_name = ttk.Entry(self)
        self.entry_fix_prize = ttk.Entry(self)
        self.entry_card_id = ttk.Entry(self)

        self.button_add = ttk.Button(self, text="Edit")
        self.button_cancel = ttk.Button(self, text="Close", command=self.destroy)

        self.window = window
        self.selection = selection

        self.init_window_entities()

    def init_window_entities(self):
        self.title("Editing fix record to DB")
        self.geometry('360x300+400+300')
        self.resizable(False, False)

        label_id = tk.Label(self, text="ID")
        label_id.place(x=10, y=20)
        label_fix_name = tk.Label(self, text="Description")
        label_fix_name.place(x=10, y=50)
        label_fix_prize = tk.Label(self, text="Card ID")
        label_fix_prize.place(x=10, y=80)
        label_card_id = tk.Label(self, text="Gold Compensation")
        label_card_id.place(x=10, y=110)

        self.entry_id.place(x=150, y=20)
        self.entry_fix_name.place(x=150, y=50)
        self.entry_fix_prize.place(x=150, y=80)
        self.entry_card_id.place(x=150, y=110)

        print(self.selection)

        self.entry_id.insert(0, self.selection['id'])
        self.entry_fix_name.insert(0, self.selection['description'])
        self.entry_fix_prize.insert(0, self.selection['card_id'])
        self.entry_card_id.insert(0, self.selection['gold_compensation'])

        self.button_add.place(x=65, y=270)
        self.button_add.bind('<Button-1>',
                             lambda fix: self.editing_record([int(self.entry_id.get()),
                                                                self.entry_fix_name.get(),
                                                                int(self.entry_fix_prize.get()),
                                                                int(self.entry_card_id.get())]))

        self.button_cancel.place(x=200, y=270)

    def editing_record(self, fields_list):
        db.edit_fix(id_=fields_list[0], fix_name=fields_list[1], fix_prize=fields_list[2],
                      card_id=fields_list[3])
        self.window.show_fixes()
        cardsWindow.show_cards()
        self.destroy()


class Delete_Fixes(tk.Toplevel):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.resizable(False, False)
        self.title("Deleting")
        self.geometry('360x100+400+300')

        self.button_delete_all = ttk.Button(self, text="Delete all tables", command=self.delete_all)
        self.button_delete_fix = ttk.Button(self, text="Delete this table", command=self.delete_accs)
        self.button_cancel = ttk.Button(self, text="Close", command=self.destroy)

        self.button_delete_all.place(x=10, y=10)
        self.button_delete_fix.place(x=140, y=10)
        self.button_cancel.place(x=270, y=10)

        self.button_search = ttk.Button(self, text="Delete")

        label_name = tk.Label(self, text="Fix ID")
        label_name.place(x=10, y=50)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=90, y=50)

        self.button_search.place(x=280, y=50)
        self.button_search.bind('<Button-1>',
                                lambda fix: self.delete_record(str(self.entry_name.get())))

    def delete_accs(self):
        db.clean_fixes()
        self.window.show_fixes()

    def delete_all(self):
        db.clean_cards()
        db.clean_fixes()
        self.window.show_fixes()
        cardsWindow.show_cards()

    def delete_record(self, fix_name):
        db.delete_fix_by_name(fix_name)
        self.window.show_fixes()


class AddRecord_Fixes(tk.Toplevel):
    def __init__(self, window):
        super().__init__()
        self.columns_fix = ("id", "new_description", "card_id", "gold_compensation")

        self.entry_id = ttk.Entry(self)
        self.entry_fix_name = ttk.Entry(self)
        self.entry_fix_prize = ttk.Entry(self)
        self.entry_card_id = ttk.Entry(self)

        self.button_add = ttk.Button(self, text="Add")
        self.button_cancel = ttk.Button(self, text="Close", command=self.destroy)

        self.window = window

        self.init_window_entities()

    def init_window_entities(self):
        self.title("Updating description")
        self.geometry('360x300+400+300')
        self.resizable(False, False)

        label_id = tk.Label(self, text="ID")
        label_id.place(x=10, y=20)
        label_fix_name = tk.Label(self, text="New Description")
        label_fix_name.place(x=10, y=50)
        label_fix_prize = tk.Label(self, text="Card ID")
        label_fix_prize.place(x=10, y=80)
        label_card_id = tk.Label(self, text="Gold Compensation")
        label_card_id.place(x=10, y=110)

        self.entry_id.place(x=150, y=20)
        self.entry_fix_name.place(x=150, y=50)
        self.entry_fix_prize.place(x=150, y=80)
        self.entry_card_id.place(x=150, y=110)

        self.button_add.place(x=65, y=270)
        self.button_add.bind('<Button-1>',
                             lambda fix: self.adding_record([int(self.entry_id.get()),
                                                               self.entry_fix_name.get(),
                                                               int(self.entry_fix_prize.get()),
                                                               int(self.entry_card_id.get())]))

        self.button_cancel.place(x=200, y=270)

    def adding_record(self, fields_list):
        db.add_fix(id_=fields_list[0], fix_name=fields_list[1], fix_prize=fields_list[2],
                     card_id=fields_list[3])
        self.window.show_fixes()
        cardsWindow.show_cards()
        self.destroy()


class SearchRecord_Fixes(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.geometry("300x100")
        self.button_search = ttk.Button(self, text="Search")
        self.title("Finding fixes")

        label_name = tk.Label(self, text="Fix ID")
        label_name.place(x=10, y=20)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=90, y=20)

        self.button_search.place(x=110, y=70)
        self.button_search.bind('<Button-1>',
                                lambda fix: self.search_record(self.entry_name.get()))

    def search_record(self, fix_name):
        SearchResults_Fixes(fix_name=fix_name)


class SearchResults_Fixes(tk.Toplevel):
    def __init__(self, fix_name):
        super().__init__()
        self.columns_fix = ("id", "new_description", "card_id", "gold_compensation")

        self.fix_name = fix_name

        self.resizable(False, False)
        self.fix_list = ttk.Treeview(self, columns=self.columns_fix, height=100, show="headings")
        for heading in self.columns_fix:
            self.fix_list.heading(heading, text=heading.replace("_", " ").title())
            self.fix_list.column(heading, width=50)

        self.fix_list.bind('<Button>', self.handle_click_fix)

        self.title("fixes Info")
        self.geometry("900x350")

        self.fix_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        db.find_fix(fix_name=self.fix_name)
        [self.fix_list.delete(i) for i in self.fix_list.get_children()]
        [self.fix_list.insert('', 'end', values=row) for row in db.cursor.fetchall()]

    def handle_click_fix(self, fix):
        if self.fix_list.identify_region(fix.x, fix.y) == "separator":
            return "break"


if __name__ == "__main__":
    db = DataBase()
    main_window = tk.Tk()
    application = MainWindow()
    application.pack()
    main_window.title("DB")
    main_window.geometry("240x120+300+200")
    main_window.resizable(False, False)
    main_window.mainloop()
