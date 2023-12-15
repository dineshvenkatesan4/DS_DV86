import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import StringVar , W 
import pandas as pd
import matplotlib.pyplot as plt

window = tk.Tk()
window.title('Combobox')

# Function for selecting Product name
def prdt_name(*args):
    sel = name.get()
    if sel == ListA[0]:
        ListB = ListB1
    elif sel == ListA[1]:
        ListB = ListB2
    elif sel == ListA[2]:
        ListB = ListB3
    p_brand.config(values=ListB)

# Function for selecting Product brand    
def prdt_brand(*args):
    sel = name.get()
    if sel == ListA[0]:
        ListB = ListB1
    elif sel == ListA[1]:
        ListB = ListB2
    elif sel == ListA[2]:
        ListB = ListB3
    p_brand.config(values=ListB)
    
ListA=["mobile","laptop","tv"]
ListB1=["Samsung","Redmi","Iphone"]
ListB2=["HP","Lenovo","Dell"]
ListB3=["Samsung","Sony","LG"]

name = StringVar()
name.set('Select here')
brand = StringVar()
brand.set('Select here')

# Controls in the page
# Labels
title = Label(window,text="Data Scraping and Visualization",font=("Times New Roman",20))
prdt_name_label = Label(window,text="Select Product Name",font=("Times New Roman",15))
prdt_brand_label = Label(window,text="Select Product Brand",font=("Times New Roman",15))

# Comboboxes
p_name = ttk.Combobox(window,textvariable=name,values=ListA, width=15,font=("Times New Roman",15))
p_name.bind("<<ComboboxSelected>>",prdt_name)
p_brand = ttk.Combobox(window,textvariable=brand,values=ListB1, width=15,font=("Times New Roman",15))
p_brand.bind("<<ComboboxSelected>>",prdt_brand)

# Buttons
def mobile():
    if p_name.get() == "mobile":
        if p_brand.get() == "Redmi":
            try:
                data = pd.read_csv(r'H:\DS&DV_PROJECT\data_scraping\exceldata\redmi_data.csv')
                df = pd.DataFrame(data,columns=['Productname','AmazonPrice','FlipkartPrice'])
                print(df)
            except FileNotFoundError:
                print("Error: File not found.")
            except pd.errors.EmptyDataError:
                print("Error: The file is empty.")
            except pd.errors.ParserError as e:
                print(f"Error: There was an issue parsing the file: {e}")
        elif p_brand.get() == "Samsung":
            try:
                data = pd.read_csv(r'H:\DS&DV_PROJECT\data_scraping\exceldata\samsung_data.csv')
                df = pd.DataFrame(data,columns=['Productname','AmazonPrice','FlipkartPrice'])
                print(df)
            except FileNotFoundError:
                print("Error: File not found.")
            except pd.errors.EmptyDataError:
                print("Error: The file is empty.")
            except pd.errors.ParserError as e:
                print(f"Error: There was an issue parsing the file: {e}")
        elif p_brand.get() == "Iphone":
            try:
                data = pd.read_csv(r'H:\DS&DV_PROJECT\data_scraping\exceldata\iphone_data.csv')
                df = pd.DataFrame(data,columns=['Productname','AmazonPrice','FlipkartPrice'])
                print(df)
            except FileNotFoundError:
                print("Error: File not found.")
            except pd.errors.EmptyDataError:
                print("Error: The file is empty.")
            except pd.errors.ParserError as e:
                print(f"Error: There was an issue parsing the file: {e}")
def laptop():
    if p_name.get() == "laptop":
        if p_brand.get() == "Dell":
            try:
                data = pd.read_csv(r'H:\DS&DV_PROJECT\data_scraping\exceldata\dell_data.csv')
                df = pd.DataFrame(data,columns=['Productname','AmazonPrice','FlipkartPrice'])
                print(df)
            except FileNotFoundError:
                print("Error: File not found.")
            except pd.errors.EmptyDataError:
                print("Error: The file is empty.")
            except pd.errors.ParserError as e:
                print(f"Error: There was an issue parsing the file: {e}")
        elif p_brand.get() == "HP":
            try:
                data = pd.read_csv (r'H:\DS&DV_PROJECT\data_scraping\exceldata\hp_data.csv')
                df = pd.DataFrame(data,columns=['Productname','AmazonPrice','FlipkartPrice'])
                print(df)
            except FileNotFoundError:
                print("Error: File not found.")
            except pd.errors.EmptyDataError:
                print("Error: The file is empty.")
            except pd.errors.ParserError as e:
                print(f"Error: There was an issue parsing the file: {e}")
        elif p_brand.get() == "Lenovo":
            try:
                data = pd.read_csv(r'H:\DS&DV_PROJECT\data_scraping\exceldata\lenovo_data.csv')
                df = pd.DataFrame(data,columns=['Productname','AmazonPrice','FlipkartPrice'])
                print(df)
            except FileNotFoundError:
                print("Error: File not found.")
            except pd.errors.EmptyDataError:
                print("Error: The file is empty.")
            except pd.errors.ParserError as e:
                print(f"Error: There was an issue parsing the file: {e}")
        else:
            print("no data")
def tv():
    if p_name.get() == "tv":
        if p_brand.get() == "Sony":
            try:
                data = pd.read_csv(r'H:\DS&DV_PROJECT\data_scraping\exceldata\sonytv_data.csv')
                df = pd.DataFrame(data,columns=['Productname','AmazonPrice','FlipkartPrice'])
                print(df)
            except FileNotFoundError:
                print("Error: File not found.")
            except pd.errors.EmptyDataError:
                print("Error: The file is empty.")
            except pd.errors.ParserError as e:
                print(f"Error: There was an issue parsing the file: {e}")
        elif p_brand.get() == "Samsung":
            try:
                data = pd.read_csv(r'H:\DS&DV_PROJECT\data_scraping\exceldata\samsungtv_data.csv')
                df = pd.DataFrame(data,columns=['Productname','AmazonPrice','FlipkartPrice'])
                print(df)
            except FileNotFoundError:
                print("Error: File not found.")
            except pd.errors.EmptyDataError:
                print("Error: The file is empty.")
            except pd.errors.ParserError as e:
                print(f"Error: There was an issue parsing the file: {e}")
        elif p_brand.get() == "LG":
            try:
                data = pd.read_csv(r'H:\DS&DV_PROJECT\data_scraping\exceldata\lgtv_data.csv')
                df = pd.DataFrame(data,columns=['Productname','AmazonPrice','FlipkartPrice'])
                print(df)
            except FileNotFoundError:
                print("Error: File not found.")
            except pd.errors.EmptyDataError:
                print("Error: The file is empty.")
            except pd.errors.ParserError as e:
                print(f"Error: There was an issue parsing the file: {e}")
        else:
            print("no data")

def data_view():
    if p_name.get() == "mobile":
        mobile()
    elif p_name.get() == "laptop":
        laptop()
    elif p_name.get() == "tv":
        tv()

def chart_view():
    f = ""
    if p_name.get() == "mobile":
        if p_brand.get() == "Redmi":
            f = 'redmi_rating.csv'        
        elif p_brand.get() == "Samsung":
            f = 'samsung_rating.csv'
        elif p_brand.get() == "Iphone":
            f = 'iphone_rating.csv'
    elif p_name.get() == "laptop":
        if p_brand.get() == "Dell":
            f = 'dell_rating.csv'
        elif p_brand.get() == "HP":
            f = 'hp_rating.csv'
        elif p_brand.get() == "Lenovo":
            f = 'lenovo_rating.csv'
    elif p_name.get() == "tv":
        if p_brand.get() == "Sony":
            f = 'sonytv_rating.csv'
        elif p_brand.get() == "Samsung":
            f = 'samsungtv_rating.csv'
        elif p_brand.get() == "LG":
            f = 'lgtv_rating.csv'            
    if f:
        try:
            df = pd.read_csv(f)
            df.set_index('Productname')[['AmazonRating','FlipkartRating']].plot.bar()
            plt.title('DATA VISUALIZATION on Online Product Comparison')
            plt.xlabel('Productname')
            plt.ylabel('Rating')
            plt.show()
        except FileNotFoundError:
            print("Error: File not found.")
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
        except pd.errors.ParserError as e:
            print(f"Error: There was an issue parsing the file: {e}")
view_data = Button(window, command=data_view, text="VIEW DATA", width=12, style="Custom.TButton")
s = ttk.Style()
s.configure("Custom.TButton", padding=(10,5)) 
view_chart = Button(window, command=chart_view, text="VIEW CHART", width=12, style="Custom.TButton")

# Code for grid
title.grid(row=1,column=4, padx=20)
prdt_name_label.grid(row = 5, column=0, sticky = W, pady=80, padx=20)
prdt_brand_label.grid(row =8, column=0, sticky = W, pady=80, padx=20)
p_name.grid(row = 5, column=1, pady=50, padx=20)
p_brand.grid(row=8, column= 1, pady=50, padx=20)
view_data.grid(row = 5, column=5, sticky = W, pady=50, padx=20)
view_chart.grid(row = 8, column=5, sticky = W, pady=50, padx=20)

window.configure(background='skyblue')
window.mainloop()
