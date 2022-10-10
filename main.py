import tkinter as tk
import psycopg2


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DiAPP")
        self.geometry('400x300')
        self.resizable(False, False)

    """ 

    THIS PROJECT START AT 19:30 10.10.2022. 
    I WANT TO SHOW YOU MY SKILLS IN OBJECT-ORIENTED PROGRAMMING
    ALSO I WANT TO SHOW MY SKILLS IN PostgreSQL

    """


if __name__ == "__main__":
    app = App()
    app.mainloop()
