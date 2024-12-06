#импорт
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import Menu
from tkinter import filedialog
import os

#функция кнопки "Посчитать"
def clicked():
    if combo.get()=="*":
        result=int(one_number.get())*int(two_number.get())  
    if combo.get()=="/":
        result=int(one_number.get())/int(two_number.get())
    if combo.get()=="+":
        result=int(one_number.get())+int(two_number.get())
    if combo.get()=="-":
        result=int(one_number.get())-int(two_number.get())
    messagebox.showinfo("Результат",f'Получилось: {result}')
#функция кнопки "Выбрать"
def clicked_choice(): 
    messagebox.showinfo("Выбор",f'Ты выбрал {selected.get()}-й выбор')
#функция кнопуи "Открыть" 
def clicked_file():
    filepath = filedialog.askopenfilename(filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, 'r') as file:
            text = file.read()
            text_area.delete(1.0, END)
            text_area.insert(END, text)  
#создание окна
window=Tk()
window.title("Радиский Давид")
window.geometry('1000x500+200+300')
#создание вкладок
tab_control=ttk.Notebook(window)
tabl1=ttk.Frame(tab_control)
tabl2=ttk.Frame(tab_control)
tabl3=ttk.Frame(tab_control)
#настройка первой вкладки
tab_control.add(tabl1, text="Калькулятор")
one_number=Entry(tabl1) 
one_number.grid(column=0, row=0) 
combo=Combobox(tabl1) 
combo.grid(column=2, row=0)
combo['values']=("*","/","+","-")
two_number=Entry(tabl1)
two_number.grid(column=3, row=0)
btn=Button(tabl1,text="Посчитать",command=clicked)
btn.grid(column=4, row=0)
#настройка второй вкладки
tab_control.add(tabl2, text="Чекбокс")
selected=IntVar()
first_choice=Radiobutton(tabl2,text="Первый", value=1, variable=selected)
first_choice.grid(column=0, row=0)
second_choice=Radiobutton(tabl2,text="Второй", value=2, variable=selected)
second_choice.grid(column=0, row=1)
third_choice=Radiobutton(tabl2,text="Третий", value=3, variable=selected)
third_choice.grid(column=0, row=2)
choice=Button(tabl2, text="Выбрать", command=clicked_choice)
choice.grid(column=2, row=1)
#Настройка третьей вкладки
tab_control.add(tabl3, text="Работа с текстом")
text_area=Text(tabl3)
text_area.pack(expand=True, fill="both")
menu = Menu(window) 
new_item = Menu(menu, tearoff=0)
new_item = Menu(menu)   
new_item.add_command(label='Открыть',command=clicked_file)   
menu.add_cascade(label='Файл', menu=new_item)   
window.config(menu=menu)



tab_control.pack(expand=1, fill='both')
window.mainloop()
    
