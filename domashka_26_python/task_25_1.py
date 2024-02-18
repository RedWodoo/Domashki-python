from tkinter import *
import os
from tkinter import messagebox
import json
import requests
os.makedirs('saving_folder',exist_ok=True)
get_json = 'https://jsonplaceholder.typicode.com/posts'
window = Tk()
def clicked():
    txt = enter.get()
    new_lbl = Label(window, text="")
    new_lbl.grid(column=0,row=1)
    new_lbl.configure(text=txt)
    get = requests.get(get_json).json()
    to_write = get[int(txt)]
    with open ('saving_folder\info.json','w') as f:
        json.dump(to_write,f)
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW", on_closing)



window.title('id_getter')
window.geometry('800x600')
lbl = Label(window, text='Enter the id of the post you want to get:')
lbl.grid(column=0, row=0)
enter = Entry(window,width=10)
enter.grid(column=1, row=0)
btn = Button(window,text='Enter',command=clicked)
btn.grid(column=2,row=0)


window.mainloop()