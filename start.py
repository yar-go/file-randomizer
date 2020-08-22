from tkinter import *
from tkinter import PhotoImage
from tkinter import scrolledtext
from tkinter import filedialog
import os
from back import get_random_files, copy_and_paste
from tkinter import messagebox as mb

window = Tk()
window.geometry('800x600')
window.title("Рандомайзер файлов")
window.resizable(0, 0)

folder_from_path = ''
folder_to_path = ''



t_folder_from_path = StringVar()
t_folder_to_path = StringVar()
str_type = StringVar()
str_count = StringVar()
str_max = StringVar()
max_count  = StringVar()

def browse_from_fold():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_from_path, t_folder_from_path
    filename = filedialog.askdirectory()
    t_folder_from_path.set(filename)
    folder_from_path = filename
    print(filename)

def browse_to_fold():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_to_path, t_folder_to_path
    filename = filedialog.askdirectory()
    t_folder_to_path.set(filename)
    folder_to_path = filename
    print(filename)

def lets_go():
    if t_folder_from_path.get() == '' or t_folder_to_path.get() == '':
        mb.showerror("Ошибка", 'Не прописаны пути')
        return
    try:
        max = int(max_count.get())
    except:
        mb.showerror("Ошибка", 'Нажмите на кнопку "Обновить окна"')
        return
    if int(max_count.get()) == 0:
        mb.showerror("Ошибка", 'Нет файлов')
        return
    type = str(entry_type.get())
    try:
        count = int(str_count.get())
    except:
        mb.showerror("Ошибка", 'Неправильно указано количество')
        return
    if count == 0:
        mb.showerror("Ошибка", 'Введен 0 файлов')
        return
    folder_from = t_folder_from_path.get() + '/'
    folder_to = t_folder_to_path.get()+ '/'

    if count > max:
        mb.showerror("Ошибка", "Перевышено максимальное число")
        return
    try:
        files_name_done = get_random_files(folder_from, type, count)
        copy_and_paste(folder_from, folder_to, files_name_done)
    except:
        mb.showerror("Ошибка", "Непредвиденная ошибка")
        return
    mb.showinfo("", "Зделано")
    print_to_screens()

def print_to_screens():
    global all_from_f, all_to_f
    path_from = str(folder_from_path)
    path_to = str(folder_to_path)
    try:
        all_from_f = os.listdir(path_from)
        all_to_f = os.listdir(path_to)
    except FileNotFoundError:
        mb.showerror("Ошибка", 'Не удается найти указанный путь')
        return
    all_from_f = list(filter(lambda x: x.endswith(str(entry_type.get())), all_from_f))
    all_to_f = list(filter(lambda x: x.endswith(str(entry_type.get())), all_to_f))
    txt_in.configure(state ='normal')
    txt_out.configure(state ='normal')
    txt_in.delete(1.0, END)
    txt_out.delete(1.0, END)
    txt_in.insert(INSERT, '\n'.join(all_from_f))
    txt_out.insert(INSERT, '\n'.join(all_to_f))
    txt_in.configure(state ='disabled')
    txt_out.configure(state ='disabled')
    max_count.set(len(all_from_f))



path_in = Entry(window, width=45, textvariable=t_folder_from_path)
path_out = Entry(window, width=45, textvariable=t_folder_to_path)

path_in.place(x=28, y=10, height=25)
path_out.place(x=421, y=10, height=25)

btn_in = Button(window, text="Выбор папки", command=browse_from_fold)
btn_out = Button(window, text="Выбор папки", command=browse_to_fold)
btn_in.place(x=298, y=10)
btn_out.place(x=690, y=10)

txt_in = scrolledtext.ScrolledText(window, width=40, height=28)
txt_out = scrolledtext.ScrolledText(window, width=40, height=28)
txt_in.place(x=22, y=60)
txt_out.place(x=448, y=60)

btn_check = Button(window, text="Обновить окна", width=15, height=2, command=print_to_screens)
entry_type = Entry(window, width=15, textvariable=str_type)
entry_count = Entry(window, width=15, textvariable=str_count)
type_label = Label(text="Тип файла:")
count_label = Label(text="Количество:")
max_label = Label(text="MAX:")
max_int_label = Label(textvariable=max_count)
btn_go = Button(window, text="RANDOM IT!", width=15, height=2, command=lets_go)

btn_check.place(x=350, y=523)
entry_type.place(x=110, y=520, height=25)
entry_count.place(x=110, y=540, height=25)
type_label.place(x=35, y=523)
count_label.place(x=35, y=543)
max_label.place(x=35, y =563)
max_int_label.place(x=110, y=563)
btn_go.place(x=660, y=523)

entry_type.insert(0, '.txt')
entry_count.insert(0, '0')
window.mainloop()