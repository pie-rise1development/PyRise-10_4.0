from tkinter import *
from tkinter import messagebox


def click():
    username = username_entry.get()
    password = password_entry.get()

    messagebox.showinfo('Авторизация успешно прошла', f'{username}, {password}')


root = Tk()
root.title('Авторизация')
root.geometry('450x230')
root.resizable(width=False, height=False)
root['bg'] = 'black'

main_label = Label(root, text="Авторизация", font='Arial 15 bold', bg='black', fg='white')
main_label.pack()

username_label = Label(root, text="Имя пользователя", font='Arial 11 bold', bg='black', fg='white', padx=10, pady=8)
username_label.pack()

username_entry = Entry(root, bg='black', fg='lime', font='Arial 12')
username_entry.pack()

password_label = Label(root, text="Пароль", font='Arial 11 bold', bg='black', fg='white', padx=10, pady=8)
password_label.pack()

password_entry = Entry(root, bg='black', fg='lime', font='Arial 12')
password_entry.pack()

send_btn = Button(root, text="Войти", command=click)
send_btn.pack(padx=10, pady=8)

root.mainloop()