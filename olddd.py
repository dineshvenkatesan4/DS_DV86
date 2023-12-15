import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import StringVar, W 
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
title = Label(window,text="Data Scraping with DataVisualization",font=("Times New Roman",20),)
prdt_name_label = Label(window,text="Select ProductName",font=("Times New Roman",15))
prdt_brand_label = Label(window,text="Select ProductBrand",font=("Times New Roman",15))

# Comboboxes
p_name = ttk.Combobox(window,textvariable=name,values=ListA, width=15,font=("Times New Roman",12))
p_name.bind("<<ComboboxSelected>>",prdt_name)
p_brand = ttk.Combobox(window,textvariable=brand,values=ListB1, width=15,font=("Times New Roman",12))
p_brand.bind("<<ComboboxSelected>>",prdt_brand)

# Buttons
def mobile():
    if p_name.get() == "mobile":
        if p_brand.get() == "Redmi":
           data = pd.read_csv(r'H:\DS&DV_PROJECT\data_scraping\exceldata\redmi_data.csv')
           df = pd.DataFrame(data,columns=['Productname',' Amazon Price','Flipkart Price'])
           print(df)
        elif p_brand.get() == "Samsung":
           data = pd.read_csv(r'H:\DS&DV_PROJECT\data_scraping\exceldata\samsung_data.csv')
           df = pd.DataFrame(data,columns=['Product name','AmazonPrice','Flipkart Price'])
           print(df)
        elif p_brand.get() == "Iphone":
           data = pd.read_csv(r'H:\DS&DV_PROJECT\data_scraping\exceldata\iphone_data.csv')
           df = pd.DataFrame(data,columns=['Product name', 'AmazonPrice','Flipkart Price'])
           print(df)
def laptop():
    if p_name.get() == "laptop":
        if p_brand.get() == "Dell":
           data = pd.read_csv(r'H:\DS&DV_PROJECT\data_scraping\exceldata\dell_data.csv')
           df = pd.DataFrame(data,columns=['Product name','Amazon Price','Flipkart Price'])
           print(df)
        elif p_brand.get() == "HP":
           data = pd.read_csv (r'H:\DS&DV_PROJECT\data_scraping\exceldata\hp_data.csv')
           df = pd.DataFrame(data,columns=['Product name","Amazon Price','Flipkart Price'])
           print(df)
        elif p_brand.get() == "Lenovo":
           data = pd.read_csv(r'H:\DS&DV_PROJECT\data_scraping\exceldata\lenovo_data.csv')
           df = pd.DataFrame(data,columns=['Product name','AmazonPrice','Flipkart Price'])
           print(df)
        else:
           print("no data")
def tv():
    if p_name.get() == "tv":
        if p_brand.get() == "Sony":
           data = pd.read_csv(r'H:\DS&DV_PROJECT\data_scraping\exceldata\sonytv_data.csv')
           df = pd.DataFrame(data,columns=['Product name','AmazonPrice','Flipkart Price'])
           print(df)
        elif p_brand.get() == "Samsung":
           data = pd.read_esv(r'H:\DS&DV_PROJECT\data_scraping\exceldata\samsungtv_data.csv')
           df = pd.DataFrame(data,columns=['Product name','Amazon Price','Flipkart Price'])
           print(df)
        elif p_brand.get() == "LG":
           data = pd.read_esv(r'H:\DS&DV_PROJECT\data_scraping\exceldata\lgtv_data.csv')
           df = pd.DataFrame(data,columns=['Product name","Amazon Price','Flipkart Price'])
           print(df)
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
        elif p_brand.get() == "Apple":
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
        df = pd.read_csv(f)
        df.set_index('Product name')[['Amazon Rating','Flipkart Rating']].plot.bar()
        plt.title('DATA VISUALIZATION on Online Product Comparison')
        plt.xlabel('PRODUCT NAME')
        plt.ylabel('RATING')
        plt.show()
        
view_data = Button(window, command=data_view, text="VIEW DATA", width=12, style="Custom.TButton")
s = ttk.Style()
s.configure("Custom.TButton", padding=(10, 5)) 
view_chart = Button(window, command=chart_view, text="VIEW CHART", width=12, style="Custom.TButton")

# Code for grid
title.grid(row=1,column=4,padx=20)
prdt_name_label.grid(row = 5, column=0, sticky = W, pady = 200,padx=20)
prdt_brand_label.grid(row =8, column=0, sticky = W,pady=2,padx=20)
p_name.grid(row = 5, column=1, pady=100,padx=20)
p_brand.grid(row=8, column= 1, pady=2,padx=20)
view_data.grid(row = 5, column=5, sticky = W,pady=100, padx=20)
view_chart.grid(row = 8, column=5, sticky=W,pady=2,padx=20)

window.configure(background='skyblue')
window.mainloop()
