"""

THIS PROJECT START AT 19:30 10.10.2022.
I WANT TO SHOW YOU MY SKILLS IN OBJECT-ORIENTED PROGRAMMING
ALSO I WANT TO SHOW MY SKILLS IN PostgreSQL

"""
import tkinter as tk
from tkinter import ttk
import psycopg2

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DiAPP")
        self.geometry('400x300')
        self.resizable(False, False)
        self['bg'] = 'cyan'
        self.style = ttk.Style()
        self.style.configure('A.TButton', font=('calibri', 10, 'bold'), foreground='green')
        self.style.configure('B.TButton', font=('Calibry', 10, 'bold', 'underline'), foreground='red')
        self.first_window()
        self.quit()

    def cleaning_func(self, objects: tuple, parameter: str) -> None:


        """ THIS IS A FUNCTION WHICH WIDGETS IS DESTROYED BY A BUTTON """

        for obj in objects:
            obj.destroy()

        if parameter == 'first-to-second':
            self.second_window()
        elif parameter == 'second-to-first':
            self.first_window()
        elif parameter == 'first-to-third':
            self.third_window()
        elif parameter == 'third-add':
            self.get_message()
        elif parameter == 'step1-step2':
            self.get_message2()
        elif parameter == 'step2-postgresql':
            self.add()
    def add(self) -> None:
        try:
            connection = psycopg2.connect(host = 'localhost',
                                          user = 'postgres',
                                          password = '****',
                                          database = 'demo',
                                          port = 5432)
            connection.autocommit = True
            with connection.cursor() as cursor:
                cursor.execute(f"""INSERT INTO words(en_word, ru_word) VALUES ('{self.tpl[1].capitalize()}', '{self.tpl[0].capitalize()}')""")
                print('[INFO] Successfully added!')
        except Exception as er:
            print(f'PostgreSQL closed connection! Something wrong: {er}')
        finally:
            if connection:
                connection.close()
                print('[INFO] Successfully closed!')
                self.first_window()

    def get_message(self):

        self.ru_word = self.message.get()

        self.ru_l = tk.Label(self, text='Напишите слово на английском', font=('Courier New', 14, 'bold'), bg='cyan')
        self.ru_l.place(x=55, y=100)

        self.message2 = tk.StringVar()
        self.ru_e = ttk.Entry(self, textvariable=self.message2)
        self.ru_e.place(x=140, y=130)

        self.next_step_b = ttk.Button(self, text='NEXT STEP', style='A.TButton', width=20,
                                      command=lambda: self.cleaning_func(objects=(self.next_step_b, self.ru_l, self.ru_e), parameter='step1-step2'))
        self.next_step_b.place(x=127, y=160)


    def get_message2(self):
        self.en_word = self.message2.get()
        self.tpl = (self.ru_word, self.en_word)
        self.temp_lbl = tk.Label(self, text = f'Вы добавили\n{self.ru_word.capitalize()} - {self.en_word.capitalize()}', font=('Courier New', 14, 'bold'), bg = 'cyan')
        self.temp_lbl.place(x = 140, y = 100)
        self.next_step_b = ttk.Button(self, text='OK', style='A.TButton', width=20,
                                      command=lambda: self.cleaning_func(objects=(self.temp_lbl, self.next_step_b), parameter='step2-postgresql')) # !*
        self.next_step_b.place(x = 140, y = 150)



    def first_window(self) -> None:


        """ THIS IS THE FIRST WINDOW OF MY APPLICATION """


        self.author_l = tk.Label(self, text = '<-- by iNTENSY -->', bg = 'cyan', font = ('Courier New', 10))
        self.author_l.place(x = 10, y = 10)

        self.game_b = ttk.Button(self, text = 'START THE GAME', style = 'A.TButton', width = 20,
                                 command= lambda : self.cleaning_func(objects = (self.game_b, self.add_b), parameter='first-to-second'))
        self.game_b.place(x = 135, y = 100)

        self.add_b = ttk.Button(self, text = 'ADD WORDS', style = 'A.TButton', width = 20,
                                command= lambda : self.cleaning_func(objects = (self.game_b, self.add_b), parameter='first-to-third'))
        self.add_b.place(x = 135, y = 140)




    def second_window(self) -> None:


        """ THIS IS THE SECOND WINDOW OF MY APPLICATION """


        self.welcome_l = tk.Label(self, text = 'No one knows what might be on this screen. \nEven a programmer', bg = 'cyan')
        self.welcome_l.pack(expand = True)

        self.back_b = ttk.Button(self, text = '<- Back', style = 'B.TButton',
                                 command= lambda : self.cleaning_func(objects = (self.welcome_l, self.back_b), parameter='second-to-first'))
        self.back_b.place(x = 200, y = 260)


    def third_window(self):


        """ THIS IS THE SECOND WINDOW OF MY APPLICATION """


        #
        self.ru_l = tk.Label(self, text = 'Напишите слово на русском', font = ('Courier New', 14, 'bold'), bg = 'cyan')
        self.ru_l.place(x = 70, y = 100)

        self.message = tk.StringVar()
        self.ru_e = ttk.Entry(self, textvariable=self.message)
        self.ru_e.place(x = 140, y = 130)

        self.next_step_b = ttk.Button(self, text = 'NEXT STEP', style = 'A.TButton', width = 20,
                                      command = lambda: self.cleaning_func(objects = (self.next_step_b, self.ru_l, self.ru_e), parameter = 'third-add'))
        self.next_step_b.place(x = 127, y = 160)

    def quit(self) -> None:


        """ THIS IS A FUNCTION WHICH APPLICATION IS DESTROYED BY A BUTTON """


        # Style for Button (QUIT)
        style = ttk.Style()
        style.configure('Q.TButton', font= ('calibri', 10, 'bold', 'underline'), foreground='red')

        self.quit_b = ttk.Button(self, text = 'QUIT', style = 'Q.TButton', command = self.destroy)
        self.quit_b.place(x = 300, y = 260)



if __name__ == "__main__":
    app = App()
    app.mainloop()
