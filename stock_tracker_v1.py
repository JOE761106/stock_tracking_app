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
            self.fitgirl_repacks_coin_remove_dict = response.json()

            self.fitgirl_repacks_coin = self.fitgirl_repacks_coin_remove_dict['fitgirl-repacks']['usd']
            self.fitgirl_repacks_coin = f"${self.fitgirl_repacks_coin:.8f}"
            print(self.fitgirl_repacks_coin)
            self.fitgirl_repacks_prices_history =[]
            self.fitgirl_repacks_prices_history.append(self.fitgirl_repacks_coin)
            print(self.fitgirl_repacks_prices_history)
    def Fetch_trump(self):
            self.url = "https://api.coingecko.com/api/v3/simple/price?ids=maga&vs_currencies=usd&x_cg_demo_api_key=API_KEY"
            
            response = requests.get(self.url )
            self.trump_coin = response.json()
            self.trump_coin_remove_dict = response.json()

            self.trump_coin = self.trump_coin_remove_dict['maga']['usd']
            self.trump_coin = f"${self.trump_coin:.8f}"
            print(self.trump_coin)  


            self.trump_coin_prices_history =[]
            self.trump_coin_prices_history.append(self.trump_coin)
            print(self.trump_coin_prices_history)

    def Fetch_pepe(self):
            
            
            self.url = "https://api.coingecko.com/api/v3/simple/price?ids=pepe&vs_currencies=usd&x_cg_demo_api_key=API_KEY"
            response = requests.get(self.url)
            self.pepe_coin = response.json()
            self.pepe_coin_remove_dict = response.json()

            self.pepe_coin = self.pepe_coin_remove_dict['pepe']['usd']
            self.pepe_coin = f"${self.pepe_coin:.8f}"
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
    #displays: label thats says the symbol back button of the stocks page ,refresh button and price of the coin
    def Trump_coin_page(self):
         self.data.Fetch_trump()
         self.symbol = 'TRUMP COIN' 
         self.trump_coin_txt=tk.Label(self , text = "MEME COIN:" +str(self.symbol) ,fg=self.main_text,bg=self.backround_color ,font=("Space Grotesk" , 20 ))
         self.trump_coin_txt.place(relx = 0.37 , rely=0.1)
         
         self.trump_coin_price_txt =tk.Label(self , text = "PRICE:" +str(self.data.trump_coin) ,fg='white',bg='black' ,font=("Space Grotesk" , 20 ))
         self.trump_coin_price_txt.place(relx = 0.4 , rely=0.5)
         
         self.trump_coin_refresh_button = tk.Button(self , text="REFRESH" ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command=lambda:[self.data.Fetch_trump() ] )
         self.trump_coin_refresh_button.place(relx=0.43 , rely=0.72)        
             
         self.trump_coin_back_button = tk.Button(self , text="BACK" ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command=lambda:[self.delete(Stock_page) ,  self.Forget_trump_coin()] )
         self.trump_coin_back_button.place(relx=0.45 , rely=0.80)        
         print(self.symbol)
    def Fitgirl_repacks_coin_page(self):
         self.data.Fetch_fitgirl_repacks()
         self.symbol = 'FITGIRL_REPACKS'
         
         self.fitgirl_repacks_coin_txt =tk.Label(self , text = "MEME COIN:" +str(self.symbol) ,fg=self.main_text,bg=self.backround_color ,font=("Space Grotesk" , 20 ))
         self.fitgirl_repacks_coin_txt.place(relx = 0.37 , rely=0.1)
         
         self.fitgirl_repacks_coin_price =tk.Label(self , text = "PRICE:" +str(self.data.fitgirl_repacks_coin) ,fg='white',bg='black' ,font=("Space Grotesk" , 20 ))
         self.fitgirl_repacks_coin_price.place(relx = 0.4 , rely=0.5)
         
         self.fitgirl_repacks_refresh_button = tk.Button(self , text="REFRESH" ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command=lambda:[] )
         self.fitgirl_repacks_refresh_button.place(relx=0.43 , rely=0.72)        
         
         self.fitgirl_repacks_back_button = tk.Button(self , text="BACK" ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command=lambda:[self.delete(Stock_page) , self.Forget_fitgirl_repacks()] )
         self.fitgirl_repacks_back_button.place(relx=0.45 , rely=0.80)
         print(self.symbol)
         
         
         
    def Pepe_coin_page(self):
         self.data.Fetch_pepe()
         self.symbol ="PEPE THE FROG"
         
         self.pepe_coin_txt =tk.Label(self , text = "MEME COIN: " +str(self.symbol) ,fg=self.main_text,bg=self.backround_color ,font=("Space Grotesk" , 20 ))
         self.pepe_coin_txt.place(relx = 0.37 , rely=0.1)
         
         self.pepe_coin_price =tk.Label(self , text = "PRICE:" +str(self.data.pepe_coin) ,fg='white',bg='black' ,font=("Space Grotesk" , 20 ))
         self.pepe_coin_price.place(relx = 0.4 , rely=0.5)
         
         self.pepe_coin_refresh_button = tk.Button(self , text="REFRESH" ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command=lambda:[] )
         self.pepe_coin_refresh_button.place(relx=0.43 , rely=0.72)        
         
         self.pepe_coin_back_button =tk.Button(self , text="back" ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command=lambda:[self.delete(Stock_page) , self.Forget_pepe_coin()] )
         self.pepe_coin_back_button.place(relx=0.45 , rely=0.80)
    #makes it so that the labels and buttons wont last after clicking back on the stock prices screen
    def Forget_pepe_coin(self):
         
         self.pepe_coin_txt.place_forget()     
         
         self.pepe_coin_price.place_forget()
         
         self.pepe_coin_back_button.place_forget()
         
         self.pepe_coin_refresh_button.place_forget()
    
    def Forget_fitgirl_repacks(self):
         
         self.fitgirl_repacks_back_button.place_forget()
         
         self.fitgirl_repacks_coin_price.place_forget()   
         
         self.fitgirl_repacks_refresh_button.place_forget()
         
         self.fitgirl_repacks_coin_txt.place_forget()
    def Forget_trump_coin(self):
         self.trump_coin_back_button.place_forget() 
         
         self.trump_coin_txt.place_forget()     
         
         self.trump_coin_price_txt.place_forget()
         
         self.trump_coin_refresh_button.place_forget()
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
         self.button_backround = "#3b82f6"
         self.button_text = "#ffffff" 
         
         self.configure(bg=container.backround_color)
        
         self.backround_color = "#0f172a"
         self.display_images()
     def display_images(self):
            
            self.fitgirl_img = tk.PhotoImage(file='fitgirl.png')
            try:
                self.fitgirl_img = self.fitgirl_img.subsample(7, 7)
                self.label = tk.Label(self, image=self.fitgirl_img).place(relx=0.84 , rely=0.73 , anchor='center')
            except:
                tk.Label(self, text="[image missing]", bg="#0f172a", fg="red").place(relx=0.5 , rely=0.5)
            
            self.pepe_img = tk.PhotoImage(file='pepe.png')
            try:
                self.pepe_img = self.pepe_img.subsample(8, 8)
                self.label = tk.Label(self, image=self.pepe_img).place(relx=0.67 , rely=0.83 , anchor='center')
            except:
                tk.Label(self, text="[image missing]", bg="#0f172a", fg="red").place(relx=0.5 , rely=0.5)
            
            self.trump_img = tk.PhotoImage(file='trump.png')
            try:
                self.trump_img = self.trump_img.subsample(9, 9)
                self.label = tk.Label(self, image=self.trump_img).place(relx=0.7 , rely=0.62 , anchor='center')
            except:
                tk.Label(self, text="[image missing]", bg="#0f172a", fg="red").place(relx=0.5 , rely=0.5)
                     
            self.stock_page()
                        # 1. Create the outer "Border" frame (this sets the highlight color)
           
           
     def stock_page(self):
        tk.Label(self , text = "please select a stock" ,bg=self.backround_color,fg='white', font = ('Space Grotesk' , 20 , 'bold')).place(relx = 0.40, rely=0.01)
        
        tk.Button(self , text="TRUMP COIN" ,bg=self.button_backround ,fg=self.button_text , font = ( 'Space Grotesk', 20 , 'bold') , command=lambda:[self.container.delete(Stock_prices) , self.container.Trump_coin_page()]).place(relx=0.42 , rely=0.60)
        
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






