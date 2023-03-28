import random
import string
import webbrowser
from tkinter import *

import pyperclip
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

class Password:
    def __init__(self):
        self.count_symbols = random.randint(9, 13)
        self.line = ""

    def generate_password(self):
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for i in range(self.count_symbols))
        return password

    def parsing(self):
        self.line = self.generate_password()
        url = r'https://www.passwordmonster.com/'
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)
        browser.get(url)
        input_tab = browser.find_element(By.XPATH, r'//*[@id="lgd_out_pg_pass"]')
        input_tab.send_keys(self.line)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        st = soup.find(id='first_estimate').text.strip()
        browser.close()
        self.st = st
        return st

    def window(self):
        root = Tk()
        root.configure(bg='#F5F5DC')
        root.geometry('380x200+200+200')
        root.title("Генератор паролей")
        root.resizable(False, False)

        def show():
            but_parol.config(text=self.line)

        def again():
            but_parol.config(text=f'{len(self.line) * "*"}', command=copy)
            self.st = self.parsing()
            lab_info.config(text=f'Этот пароль можно будет взломать через {self.st}*')

        def copy():
            pyperclip.copy(self.line)

        def callback(event):
            webbrowser.open_new(r"https://www.passwordmonster.com/")

        label_hello = Label(text='Генератор паролей', height=1, background='#DAA520')
        label_hello.pack()
        but_parol = Button(text=f'{len(self.line) * "*"}', command=copy)
        but_parol.pack()
        but_copy = Button(text='Показать пароль', command=show)
        but_copy.pack()
        but_again = Button(text='Переделать пароль', command=again)
        but_again.pack()
        lab_info = Label(text=f'Этот пароль можно будет взломать через {self.st}*')
        lab_info.pack()
        lab_lc = Label(text='*На основании веб-сервиса')
        lab_lb = Label(text='passwordmonster.com', fg="blue", cursor="hand2")
        lab_lc.pack()
        lab_lb.pack()
        lab_lb.bind("<Button-1>", callback)

        root.mainloop()


par = Password()
par.window()
