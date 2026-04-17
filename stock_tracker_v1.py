import tkinter as tk
from tkinter import ttk
class Data:
    def __init__(self):
        self.stock_list=['Toyota Motor Corporation' , 'HSBC Holdings' , "Apple Inc."]
  
class Ui (tk.Tk):
    def __init__(self , data_source):
        super().__init__()
        self.data = data_source
    
        
        self.geometry('1000x700')
        self.resizable(False, False)
        
    
        bg_main = "#0f172a"
        self.configure(bg=bg_main)
            
        self.backround_color = "#0f172a"
        self.main_text= "#e2e8f0"
        self.second_color= "#94a3b8"
        
        self.button_backround = "#3b82f6"
        self.button_text = "#ffffff"

        
        self.frames = {}
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        
        for F in(Loading_page , Welcome_page , Stock_page):
                frame = F( container , self )
                self.frames[F] = frame
                frame.place(relwidth=1, relheight=1)

        self.delete(Loading_page)
    def delete(self , page):
        frame = self.frames[page] 
        frame.tkraise()

class Loading_page(tk.Frame):
    def __init__(self , parent , container):
         super().__init__(parent)
         self.bar = ttk.Progressbar(self, length=300 )
         self.bar.place(relx = 0.5 , rely = 0.5 , anchor='center')
        
         self.container = container

         self.configure(bg=container.backround_color)
         self.load()
    def load(self , i=0):
            tk.Label(self , text="loading current popular stocks..." ,bg =self.container.backround_color ,fg=self.container.main_text , font=("Helvetica" , 13  )).place(relx = 0.40, rely =0.45 )
            if i <= 100:
                self.bar['value'] = i
                self.after(10, self.load, i + 1)

        
            else:
                
                self.container.delete(Welcome_page)
class Welcome_page(tk.Frame):
    def __init__(self , parent , container):
         super().__init__(parent)
         self.container = container
         
         self.main_text= "#e2e8f0"
         self.second_color= "#94a3b8"
        
         self.backround_color = "#0f172a"
                 
         self.button_backround = "#3b82f6"
         self.button_text = "#ffffff" 
         
         self.configure(bg=container.backround_color)
         self.welcome()
    def welcome(self):
        tk.Label(self , text = 'welcome'  ,fg=self.main_text,bg=self.backround_color ,font=("Space Grotesk" , 20 )).place(relx=0.5 , rely=0)
        tk.Label(self , text = "please enjoy the StonkTracker3000ProMax" ,bg=self.backround_color,fg=self.main_text, font = ('Space Grotesk' , 20 , 'bold')).place(relx = 0.25 , rely=0.09)
        self.img = tk.PhotoImage(file='stonks.png')
        try:
            self.img = self.img.subsample(2, 2)
            label = tk.Label(self, image=self.img).place(relx=0.54 , rely=0.4 , anchor='center')
        except:
            tk.Label(self, text="[image missing]", bg="#0f172a", fg="red").pack(pady=20)
        
        tk.Button(self , text="continue" ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command=lambda:[self.container.delete(Stock_page)] ).place(relx=0.45 , rely=0.69)
class Stock_page(tk.Frame):
     def __init__(self , parent , container):
         super().__init__(parent)
         self.container = container
         self.main_text= "#e2e8f0"
         self.second_color= "#94a3b8"
        
         self.backround_color = "#0f172a"
                 
         self.button_backround = "#3b82f6"
         self.button_text = "#ffffff" 
         
         self.configure(bg=container.backround_color)
         self.stock_page()
     def stock_page(self):
        tk.Label(self , text = "please select a stock" ,bg=self.backround_color,fg='white', font = ('Space Grotesk' , 20 , 'bold')).place(relx = 0.40, rely=0.01)
        combo = ttk.Combobox(self , values=self.container.data.stock_list)
        combo.place(relx = 0.45 , rely=0.5)
        

data = Data()
app = Ui(data)
app.mainloop()


