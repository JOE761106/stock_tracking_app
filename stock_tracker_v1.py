import tkinter as tk
from tkinter import ttk
class Data:
    def __init__(self):
        self.stock_list=['Toyota Motor Corporation' , 'HSBC Holdings' , "Apple Inc."]
  
class Ui:
    def __init__(self , data_source):
        self.data = data_source
        self.window = tk.Tk()
        self.window.geometry('1000x700')
        self.bar = ttk.Progressbar(self.window, length=300 )
        self.bar.place(relx = 0.5 , rely = 0.5 , anchor='center')
        bg_main = "#0f172a"
        self.window.configure(bg=bg_main)
        self.backround_color = "#0f172a"
        self.main_text= "#e2e8f0"
        self.second_color= "#94a3b8"

        self.button_backround = "#3b82f6"
        self.button_text = "#ffffff"

        
        tk.Label(self.window , text="loading current popular stocks..." ,bg =self.backround_color ,fg=self.main_text , font=("Helvetica" , 13  )).place(relx = 0.40, rely =0.45 )
        self.load()
            
        self.window.mainloop()

    def delete(self):
        for widget in self.window.winfo_children():
            widget.destroy()
    def load(self , i=0):
        if i <= 100:
            self.bar['value'] = i
            self.window.after(10, self.load, i + 1)

        
        else:
            self.delete()
            self.welcome()
    def welcome(self):
        tk.Label(self.window , text = 'welcome'  ,fg=self.main_text,bg=self.backround_color ,font=("Space Grotesk" , 20 )).place(relx=0.5 , rely=0)
        tk.Label(self.window , text = "please enjoy the StonkTracker3000ProMax" ,bg=self.backround_color,fg=self.main_text, font = ('Space Grotesk' , 20 , 'bold')).place(relx = 0.25 , rely=0.09)
        self.img = tk.PhotoImage(file='stonks.png')
        self.img = self.img.subsample(2, 2)
        
        label = tk.Label(self.window, image=self.img)
        label.place(relx=0.54 , rely=0.4 , anchor='center')
        
        tk.Button(self.window , text="continue" ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command = lambda:[self.delete() , self.stock_page()]).place(relx=0.45 , rely=0.69)
    def stock_page(self):
        tk.Label(self.window , text = "please select a stock" ,bg=self.backround_color,fg='white', font = ('Space Grotesk' , 20 , 'bold')).place(relx = 0.40, rely=0.01)
        combo = ttk.Combobox(self.window , values=self.data.stock_list)
        combo.grid(relx = 0.45 , rely=0.5)
        








my_data = Data() 


app = Ui(my_data)
 


 
