"""

THIS PROJECT START AT 19:30 10.10.2022.
I WANT TO SHOW YOU MY SKILLS IN OBJECT-ORIENTED PROGRAMMING
ALSO I WANT TO SHOW MY SKILLS IN PostgreSQL

"""
import tkinter as tk
from tkinter import ttk
import psycopg2
from random import shuffle

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

        """ THIS IS A FUNCTION WHICH WIDGETS ARE DESTROYED BY A BUTTON """

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
        elif parameter == 'first-to-get':
            self.get_w()

    def add(self) -> None:

        """ THIS IS THE FUNCTION THAT CONNECTED POSTGRESQL WITH THE PROJECT, ALSO GETS THE RUSSIAN AND ENGLISH WORD  """

        try:
            connection = psycopg2.connect(host = 'localhost',
                                          user = 'postgres',
                                          password = '1703',
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

    def get_w(self) -> list:

        """ THIS IS THE FUNCTION THAT CONNECTED POSTGRESQL WITH THE PROJECT, ALSO GIVES OUT RUSSIAN AND ENGLISH WORDS  """

        try:
            connection = psycopg2.connect(host = 'localhost',
                                          user = 'postgres',
                                          password = '1703',
                                          database = 'demo',
                                          port = 5432)
            connection.autocommit = True
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM words""")
                words = cursor.fetchall()
        except Exception as er:
            print(f'PostgreSQL closed connection! Something wrong: {er}')
        finally:
            if connection:
                connection.close()
                print('[INFO] Successfully closed!')
        return words


    def get_message(self):

        """ THIS IS THE FUNCTION BY WHICH THE APPLICATION RECEIVES THE ENGLISH WORD """

        self.ru_word = self.message.get()

        ru_l = tk.Label(self, text='Напишите слово на английском', font=('Courier New', 14, 'bold'), bg='cyan')
        ru_l.place(x=55, y=100)

        self.message2 = tk.StringVar()
        ru_e = ttk.Entry(self, textvariable=self.message2)
        ru_e.place(x=140, y=130)

        next_step_b = ttk.Button(self, text='NEXT STEP', style='A.TButton', width=20,
                                 command=lambda: self.cleaning_func(objects=(next_step_b, ru_l, ru_e), parameter='step1-step2'))
        next_step_b.place(x=127, y=160)


    def get_message2(self):

        """ THIS IS THE FUNCTION BY WHICH THE APPLICATION RECEIVES THE RUSSIAN WORD """

        self.en_word = self.message2.get()
        self.tpl = (self.ru_word, self.en_word)
        temp_lbl = tk.Label(self, text = f'Вы добавили\n{self.ru_word.capitalize()} - {self.en_word.capitalize()}', font=('Courier New', 14, 'bold'), bg = 'cyan')
        temp_lbl.place(x = 140, y = 100)
        next_step_b = ttk.Button(self, text='OK', style='A.TButton', width=20,
                                 command=lambda: self.cleaning_func(objects=(temp_lbl, next_step_b), parameter='step2-postgresql')) # !*
        next_step_b.place(x = 140, y = 150)



    def first_window(self) -> None:

        """ THIS IS THE FIRST WINDOW OF MY APPLICATION """

        author_l = tk.Label(self, text = '<-- by iNTENSY -->', bg = 'cyan', font = ('Courier New', 10))
        author_l.place(x = 10, y = 10)

        game_b = ttk.Button(self, text = 'START THE GAME', style = 'A.TButton', width = 20,
                            command= lambda: self.cleaning_func(objects = (game_b, add_b), parameter='first-to-second'))
        game_b.place(x = 135, y = 100)

        add_b = ttk.Button(self, text = 'ADD WORDS', style = 'A.TButton', width = 20,
                           command= lambda: self.cleaning_func(objects = (game_b, add_b), parameter='first-to-third'))
        add_b.place(x = 135, y = 140)



    def second_window(self) -> None:

        """ THIS IS THE SECOND WINDOW OF MY APPLICATION """

        self.words_game = self.get_w()
        shuffle(self.words_game)

        quest_ru_l = tk.Label(self, text=f'Напишите слово {self.words_game[0][2]}\nна английском', font=('Courier New', 14, 'bold'), bg='cyan')
        quest_ru_l.place(x=90, y=70)
        score = tk.Label(self, bg = 'cyan')
        score.place(x = 10, y = 30)


        self.answer_message = tk.StringVar()
        answer_e = ttk.Entry(self, textvariable=self.answer_message, width=25)
        answer_e.place(x=130, y=130)


        self.i = 1
        self.flag = True
        next_word_b = ttk.Button(self, text='NEXT ->', style='A.TButton', command = lambda: self.check(quest_ru_l, self.i, answer_e, back_b, next_word_b, score))
        next_word_b.place(x=165, y=160)

        back_b = ttk.Button(self, text = '<- Back', style = 'B.TButton',
                            command= lambda: self.cleaning_func(objects = (quest_ru_l, answer_e, back_b, next_word_b, score), parameter='second-to-first'))
        back_b.place(x = 200, y = 260)


    def check(self, quest_ru_l, i, answer_e, back_b, next_word_b, score):

        """ THIS IS A FUNCTION THAT CHECKS A WORD FROM THE USER WITH THE CORRECT ANSWER """

        if self.answer_message.get().capitalize() == self.words_game[self.i-1][1]:
            try:
                quest_ru_l.config(text = f'Новое слово - {self.words_game[i][2]}')
                self.i += 1
                answer_e.delete(0, 'end')
                score.config(text = f'{self.i-1}')
            except IndexError:
                self.cleaning_func(objects = (quest_ru_l, answer_e, back_b, next_word_b, score), parameter='second-to-first')
        else:
            self.cleaning_func(objects=(quest_ru_l, answer_e, back_b, next_word_b, score), parameter='second-to-first')


    def third_window(self):

        """ THIS IS THE SECOND WINDOW OF MY APPLICATION """

        ru_l = tk.Label(self, text = 'Напишите слово на русском', font = ('Courier New', 14, 'bold'), bg = 'cyan')
        ru_l.place(x = 70, y = 100)

        self.message = tk.StringVar()
        ru_e = ttk.Entry(self, textvariable=self.message)
        ru_e.place(x = 140, y = 130)

        next_step_b = ttk.Button(self, text = 'NEXT STEP', style = 'A.TButton', width = 20,
                                 command = lambda: self.cleaning_func(objects = (next_step_b, ru_l, ru_e), parameter = 'third-add'))
        next_step_b.place(x = 127, y = 160)



    def quit(self) -> None:

        """ THIS IS A FUNCTION WHICH APPLICATION IS DESTROYED BY A BUTTON """

        style = ttk.Style()
        style.configure('Q.TButton', font=('Сalibri', 10, 'bold', 'underline'), foreground='red')

        quit_b = ttk.Button(self, text='QUIT', style='Q.TButton', command=self.destroy)
        quit_b.place(x=300, y=260)


if __name__ == "__main__":
    app = App()
    app.mainloop()
