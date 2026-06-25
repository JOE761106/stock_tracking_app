import tkinter as tk
from tkinter import ttk
import requests
class Data:
    def __init__(self):
        self.url = "https://api.coingecko.com/api/v3/simple/price?ids=&vs_currencies=usd&x_cg_demo_api_key="
        
       
    def Fetch_fitgirl_repacks(self):
            self.url = "https://api.coingecko.com/api/v3/simple/price?ids=fitgirl-repacks&vs_currencies=usd&x_cg_demo_api_key=API_KEY"
            
            response = requests.get(self.url)
            self.fitgirl_repacks_coin = response.json()
            print(self.fitgirl_repacks_coin)
    def Fetch_trump(self):
            self.url = "https://api.coingecko.com/api/v3/simple/price?ids=maga&vs_currencies=usd&x_cg_demo_api_key=API_KEY"
            
            response = requests.get(self.url )
            self.trump_coin = response.json()
            print(self.trump_coin)
        
    def Fetch_pepe(self):
            
            self.url = "https://api.coingecko.com/api/v3/simple/price?ids=pepe&vs_currencies=usd&x_cg_demo_api_key=API_KEY"
            response = requests.get(self.url)
            self.pepe_coin = response.json()
            
            print(self.pepe_coin)

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
        
        for F in(Loading_page , Welcome_page , Stock_page , Stock_prices):
                frame = F( container , self )
                self.frames[F] = frame
                frame.place(relwidth=1, relheight=1)

        self.delete(Loading_page)
    def delete(self , page):
        frame = self.frames[page] 
        frame.tkraise()
    #displays label thats says the symbol and back button of the stocks e.g user chose google-->self.symbol=GOOGL
    def Trump_coin_page(self):
         self.data.Fetch_apple()
         self.symbol = 'TRUMP COIN' 
         self.trump_coin_txt=tk.Label(self , text = "SHITCOIN:" +str(self.symbol) ,fg=self.main_text,bg=self.backround_color ,font=("Space Grotesk" , 20 ))
         self.trump_coin_txt.place(relx = 0.5 , rely=0.1)
         
         self.trump_coin_price_txt =tk.Label(self , text = "PRICE:" +str(self.data.stock_data) ,fg='white',bg='black' ,font=("Space Grotesk" , 20 ))
         self.trump_coin_price_txt.place(relx = 0.5 , rely=0.5)
         
         self.trump_coin_refresh_button = tk.Button(self , text="REFRESH" ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command=lambda:[self.data.Fetch_apple() ] )
         self.trump_coin_refresh_button.place(relx=0.45 , rely=0.60)        
         
         self.trump_coin_back_button = tk.Button(self , text="BACK" ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command=lambda:[self.delete(Stock_page) ,  self.Forget_apple()] )
         self.trump_coin_back_button.place(relx=0.45 , rely=0.80)        
         print(self.symbol)
    def Fitgirl_repacks_coin_page(self):
         self.data.Fetch_fitgirl_repacks()
         self.symbol = 'FITGIRL_REPACKS'
         
         self.fitgirl_repacks_coin_txt =tk.Label(self , text = "SHITCOIN:" +str(self.symbol) ,fg=self.main_text,bg=self.backround_color ,font=("Space Grotesk" , 20 ))
         self.fitgirl_repacks_coin_txt.place(relx = 0.5 , rely=0.1)
         
         self.fitgirl_repacks_coin_price =tk.Label(self , text = "PRICE:" +str(self.data.stock_data) ,fg='white',bg='black' ,font=("Space Grotesk" , 20 ))
         self.fitgirl_repacks_coin_price.place(relx = 0.5 , rely=0.5)
         
         self.fitgirl_repacks_refresh_button = tk.Button(self , text="REFRESH" ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command=lambda:[] )
         self.fitgirl_repacks_refresh_button.place(relx=0.45 , rely=0.60)        
         
         self.fitgirl_repacks_back_button = tk.Button(self , text="BACK" ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command=lambda:[self.delete(Stock_page) , self.Forget_google()] )
         self.fitgirl_repacks_back_button.place(relx=0.45 , rely=0.80)
         print(self.symbol)
         
         
         
    def Pepe_coin_page(self):
         self.data.Fetch_pepe()
         self.symbol ="PEPE DA FROG"
         
         self.pepe_coin_txt =tk.Label(self , text = "shitcoin:" +str(self.symbol) ,fg=self.main_text,bg=self.backround_color ,font=("Space Grotesk" , 20 ))
         self.pepe_coin_txt.place(relx = 0.5 , rely=0.1)
         
         self.pepe_coin_price =tk.Label(self , text = "price:" +str(self.data.pepe_coin) ,fg='white',bg='black' ,font=("Space Grotesk" , 20 ))
         self.pepe_coin_price.place(relx = 0.5 , rely=0.5)
         
         self.pepe_coin_refresh_button = tk.Button(self , text="refresh" ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command=lambda:[] )
         self.pepe_coin_refresh_button.place(relx=0.45 , rely=0.60)        
         
         self.pepe_coin_back_button =tk.Button(self , text="back" ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command=lambda:[self.delete(Stock_page) , self.Forget_toyota()] )
         self.pepe_coin_back_button.place(relx=0.45 , rely=0.80)
    #makes it so that the labels and buttons wont last after clicking back on the stock prices screen
    def Forget_pepe_coin(self):
         
         self.pepe_coin_txt.place_forget()     
         
         self.pepe_coin_price.place_forget()
         
         self.pepe_coin_back_button.place_forget()
         
         self.pepe_coin_refresh_button.place_forget()
    
    def Forget_google(self):
         
         self.google_refresh_button.place_forget()
         
         self.google_txt.place_forget()   
         
         self.google_stock_txt.place_forget()
         
         self.google_button.place_forget()
    def Forget_apple(self):
         self.apple_refresh_button.place_forget() 
         
         self.apple_txt.place_forget()     
         
         self.apple_stock_txt.place_forget()
         
         self.apple_button.place_forget()
    ###finishes here
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
            tk.Label(self, text="[image missing]", bg="#0f172a", fg="red").place(relx=0.5 , rely=0.5)
        
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
        
        tk.Button(self , text="TRUMP COIN" ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command=lambda:[self.container.delete(Stock_prices) , self.container.Trump_coin_page()]).place(relx=0.45 , rely=0.60)
        
        tk.Button(self , text='FITGIRL_REPACKS COIN' ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command=lambda:[self.container.delete(Stock_prices) , self.container.Fitgirl_repacks_coin_page()] ).place(relx=0.43 , rely=0.69)
        tk.Button(self , text="PEPE COIN" ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command=lambda:[self.container.delete(Stock_prices) , self.container.Pepe_coin_page() ] ).place(relx=0.45 , rely=0.80)
class Stock_prices(tk.Frame):
     def __init__(self , parent , container):
         super().__init__(parent)
         self.container = container
         self.main_text= "#e2e8f0"
         self.second_color= "#94a3b8"
        
         self.backround_color = "#0f172a"
                 
         self.button_backround = "#3b82f6"
         self.button_text = "#ffffff" 
         
         self.configure(bg=container.backround_color)
        
    

data = Data()
app = Ui(data)
app.mainloop()




