"""

THIS PROJECT START AT 19:30 10.10.2022.
I WANT TO SHOW YOU MY SKILLS IN OBJECT-ORIENTED PROGRAMMING
ALSO I WANT TO SHOW MY SKILLS IN PostgreSQL

"""

import tkinter as tk
from tkinter import ttk
# import psycopg2

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DiAPP")
        self.geometry('400x300')
        self.resizable(False, False)
        self['bg'] = 'cyan'
        self.first_window()
        self.quit()

    def cleaning_func(self, objects: tuple, parameter: str) -> None:


        """
                        THIS IS A FUNCTION WHICH WIDGETS IS DESTROYED BY A BUTTON
        """


        for obj in objects:
            obj.destroy()
        if parameter == 'first-to-second':
            self.second_window()
        elif parameter == 'second-to-first':
            self.first_window()




    def first_window(self) -> None:


        """
                        THIS IS THE FIRST WINDOW OF MY APPLICATION
        """


        style = ttk.Style()
        style.configure('A.TButton', font=('calibri', 10, 'bold'), foreground='green')

        self.author_l = tk.Label(self, text = '<-- by iNTENSY -->', bg = 'cyan', font = ('Courier New', 10))
        self.author_l.place(x = 10, y = 10)

        self.game_b = ttk.Button(self, text = 'START THE GAME', style = 'A.TButton', width = 20,
                                 command= lambda : self.cleaning_func(objects = (self.game_b, self.add_b), parameter='first-to-second'))
        self.game_b.place(x = 135, y = 100)

        self.add_b = ttk.Button(self, text = 'ADD WORDS', style = 'A.TButton', width = 20)
        self.add_b.place(x = 135, y = 140)




    def second_window(self) -> None:


        """
                        THIS IS THE SECOND WINDOW OF MY APPLICATION
        """


        self.welcome_l = tk.Label(self, text = 'No one knows what might be on this screen. \nEven a programmer', bg = 'cyan')
        self.welcome_l.pack(expand = True)

        style = ttk.Style()
        style.configure('B.TButton', font = ('Calibry', 10, 'bold', 'underline'), foreground = 'red')
        self.back_b = ttk.Button(self, text = '<- Back', style = 'B.TButton',
                                 command= lambda : self.cleaning_func(objects = (self.welcome_l, self.back_b), parameter='second-to-first'))
        self.back_b.place(x = 200, y = 260)




    def quit(self) -> None:


        """
                        THIS IS A FUNCTION WHICH APPLICATION IS DESTROYED BY A BUTTON
        """


        # Style for Button (QUIT)
        style = ttk.Style()
        style.configure('Q.TButton', font= ('calibri', 10, 'bold', 'underline'), foreground='red')

        self.quit_b = ttk.Button(self, text = 'QUIT', style = 'Q.TButton', command = self.destroy)
        self.quit_b.place(x = 300, y = 260)



if __name__ == "__main__":
    app = App()
    app.mainloop()
