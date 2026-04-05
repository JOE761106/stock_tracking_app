import tkinter as tk
from tkinter import ttk

class ui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('1000x700')
        self.bar = ttk.Progressbar(self.window, length=300 )
        tk.Label(self.window , text="loading current popular stocks..." , font=("Helvetica" , 13 , "bold" )).place(relx = 0.36 , rely =0.45 )
        self.bar.place(relx = 0.5 , rely = 0.5 , anchor='center')
        
        
        self.load()
            
        self.window.mainloop()

    def load(self , i=0):
        if i <= 100:
            self.bar['value'] = i
            self.window.after(10, self.load, i + 1)

        else:
            for widget in self.window.winfo_children():
                widget.destroy()
            self.welcome()
    def welcome(self):
        tk.Label(self.window , text = 'welcome' , font=("Helvetica" , 13 , "bold" , )).place(relx=0.5 , rely=0)
        tk.Label(self.window , text = "please enjoy the StonkTracker3000ProMax" , font = ('Helvetica' , 20 , 'bold')).place(relx = 0.25 , rely=0.09)
        self.img = tk.PhotoImage(file='stonks.png')
        self.img = self.img.subsample(2, 2)
        
        label = tk.Label(self.window, image=self.img)
        label.place(relx=0.54 , rely=0.4 , anchor='center')
        tk.Button(self.window , text="continue" , font = ('Helivetica' , 13 , 'bold') ).place(relx=0.5 , rely=0.69)









app = ui()

 
