from tkinter import*
import json
import requests
from pprint import pprint
#Функция кнопки "Создать"  
def click():
    username=vvod.get()
    url=f'https://api.github.com/users/{username}'
    user_data=requests.get(url).json()
    info_subject={
        'company': user_data['company'],
        'created_at': user_data['created_at'],
        'email':  user_data['email'],
        'id': user_data['id'],
        'name': user_data['name'],
        'url': user_data['url']
    }
    with open("C:\\Users\\David\\Desktop\\моя работа\\python сдать\\12.json", "w") as file:
        file.write(json.dumps(info_subject, indent = 4))
#создание окна
window=Tk()
window.title("Радинский Давид Антонович")
window.geometry("1000x500")
vvod=Entry(window)
vvod.grid(column=0,row=0)
button=Button(window,text="Создать",command=click)
button.grid(column=1,row=0)
vvod.focus()
window.mainloop()