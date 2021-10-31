

import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime

def get_html_data(url):
    data = requests.get(url)
    return data


def get_covid_detail_bd():
    url = "https://worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_detail = ""

    for i in range(3):
        text = info_div[i].find("h1", class_=None).get_text()

        count = info_div[i].find("span", class_=None).get_text()

        all_detail = all_detail + text + " " + count + "\n"

    return all_detail

def get_country_data():
    name= textfield.get()
    url="https://worldometers.info/coronavirus/country/"+name
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_detail = ""

    for i in range(3):
        text = info_div[i].find("h1", class_=None).get_text()

        count = info_div[i].find("span", class_=None).get_text()

        all_detail = all_detail + text + " " + count + "\n"

    mainlabel['text']=all_detail

def reload():
    new_data = get_covid_detail_bd()
    mainlabel['text']=new_data





root = tk.Tk()
root.geometry("900x700")
root.title("Covid19 update ")
f = ("poppins", 25, "bold")
banner = tk.PhotoImage(file="covid.png")
bannerlabel = tk.Label(root, image=banner)
bannerlabel.pack()

textfield=tk.Entry(root, width= 50)
textfield.pack()

mainlabel = tk.Label(root, text = get_covid_detail_bd(), font=f)
mainlabel.pack()

gbtn = tk.Button(root, text="Get data", font=f, relief='solid', command=get_country_data)
gbtn.pack()

rbtn = tk.Button(root, text="Reload", font=f, relief='solid', command=reload)
rbtn.pack()

root.mainloop()