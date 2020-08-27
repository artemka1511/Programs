from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd

root = tk.Tk()
root.geometry("600x500")
root.title("Поиск слов в файле by Артём Щербаков")
root['bg'] = '#7dbbf5'
root.resizable(0, 0)
x_mid = root.winfo_width()
y_mid = root.winfo_height()
directory = None


def browsefunc():
    global directory
    directory = fd.askopenfilename()
    path_label.config(text=directory)


def search():
    if directory == None:
        warning_label_1 = Label(root, text='ОШИБКА ! Выберите файл !', width=55, height=5, bg='#7dbbf5', fg='red', font='arial 14')
        warning_label_1.place(x=-40, y=350)
    else:
        file = open(directory, 'r', encoding='utf-8')
        a = reg_var.get()
        if a == 1:
            text_file = file.read().lower()
            word_get = input_word.get().lower()

        else:
            text_file = file.read()
            word_get = input_word.get()
        file.close()
        warning_label_2 = Label(root, text='', width=55, height=5, bg='#7dbbf5', fg='red', font='arial 14')
        warning_label_2.place(x=-40, y=350)
        if word_get == '':
            warning_label_2['text'] = 'ОШИБКА ! Введите слово для поиска !'

        else:
            warning_label_2.destroy()
            count12 = text_file.count(word_get)
            result = Label(root, text='Найдено слов:', width=25, height=5, bg='#7dbbf5', fg='black', font='arial 14')
            result.place(x=-50, y=350)
            count = Label(root, text=count12, width=25, height=5, bg='#7dbbf5', fg='black', font='arial 14')
            count.place(x=170, y=350)


browse_button = Button(root, text="Browse", font='arial 11', command=browsefunc)
browse_button.place(x=350, y=30)

change_file = Label(root, text='Выберите файл:', width=25, height=5, bg='#7dbbf5', fg='black', font='arial 14')
change_file.place(x=-50, y=-10)

path_label = Label(root, bg='#7dbbf5')
path_label.place(x=250, y=60)

input_word = Entry(root, width=30, bd=2, font='arial 14')
input_word.place(x=250, y=145)

word_label = Label(root, text='Введите слово:', width=25, height=5, bg='#7dbbf5', fg='black', font='arial 14')
word_label.place(x=-50, y=100)

search_button = Button(root, text="ИСКАТЬ", font='arial 14', command=search)
search_button.place(x=250, y=295)

reg_var = IntVar()
register = Checkbutton(root, text='Не учитывать регистр', bg='#7dbbf5', font='arial 14', variable=reg_var, onvalue=1, offvalue=0)
register.place(x=20, y=200)

root.mainloop()
