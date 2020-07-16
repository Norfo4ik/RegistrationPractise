import tkinter as tk
from tkinter import messagebox
import hashlib
import os
import pickle
check = {}

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='ghost white', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_opn_signup = tk.Button(toolbar, text="Зарегестрироваться", command=self.open_signup, bg='ghost white', bd=0, compound=tk.TOP)
        btn_opn_signup.pack(side=tk.LEFT)
        btn_opn_about = tk.Button(toolbar, text="О программе", command=self.open_about, bd=0, bg='ghost white', compound=tk.TOP)
        btn_opn_about.pack(side=tk.LEFT)
        Sign_label=tk.Label(text="Введите логин:")
        Sign_label.pack()
        Sign_Entry=tk.Entry()
        Sign_Entry.pack()
        Sign_lable_pas=tk.Label(text="Введите пароль:")
        Sign_lable_pas.pack()
        Sign_Entry_pas=tk.Entry(show="*")
        Sign_Entry_pas.pack()
        Sign_btn=tk.Button(text="Войти", command = lambda: self.signin(Sign_Entry.get(),Sign_Entry_pas.get()))
        Sign_btn.place(x=70, y=120)
        Cancel_btn=tk.Button(text="Выход", command=on_closing)
        Cancel_btn.place(x=130, y=120)

    def open_signup(self):
        Registration()

    def open_about(self):
        About()

    def signin(self, login, passw):
        if check.get(login) is None:
            tk.messagebox.showerror(title="Ошибка", message="Пользователь не найден")
        else:
            salt = check[login]['salt']
            key = check[login]['key']
            entered_key = hashlib.pbkdf2_hmac('sha256', passw.encode('utf-8'), salt, 100000)
            if key == entered_key:
                tk.messagebox.showinfo(title="Успех", message="Вы успешно вошли!")
            else:
                tk.messagebox.showinfo(title="Ошибка", message="Вы ввели неправильный пароль!")


class Registration(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_Registration()
        self.view = app

    def init_Registration(self):
        self.title = ("Регистрация")
        self.geometry("250x190+400+300")
        self.resizable(False, False)

        self.Reg_label = tk.Label(self,text="Введите логин")
        self.Reg_label.pack()
        self.Reg_nick = tk.Entry(self)
        self.Reg_nick.pack()
        self.Reg_label_pass = tk.Label(self,text="Введите пароль:")
        self.Reg_label_pass.pack()
        self.Reg_pass = tk.Entry(self,show="*")
        self.Reg_pass.pack()
        self.Reg_label_pass_re = tk.Label(self,text="Введите пароль снова:")
        self.Reg_label_pass_re.pack()
        self.Reg_pass_re = tk.Entry(self,show="*")
        self.Reg_pass_re.pack()
        Reg_btn = tk.Button(self,text="Зарегестрироваться", command=lambda: self.record_signup(self.Reg_nick.get(),self.Reg_pass.get(), self.Reg_pass_re.get()))
        Reg_btn.pack()
        Cancel_btn=tk.Button(self, text="Отменить", command=self.destroy)
        Cancel_btn.pack()

        self.grab_set()
        self.focus_set()


    def record_signup(self, login, passw, passw_re):
        users = {}
        if  self.Reg_nick.get():
            if self.Reg_pass.get():
                if self.Reg_pass_re.get():
                    if passw != passw_re:
                        tk.messagebox.showerror(title="Ошибка", message="Введннные пароли не совпадают!")
                    else:
                        if check.get(login) is None:
                            tk.messagebox.showinfo(title="Успех", message="Вы успешно зарегестрировались!")
                            salt = os.urandom(32)
                            key = hashlib.pbkdf2_hmac('sha256', passw.encode('utf-8'), salt, 100000)
                            check[login] = {
                                'salt': salt,
                                'key': key
                            }
                            self.Reg_nick.delete(0, tk.END)
                            self.Reg_pass.delete(0, tk.END)
                            self.Reg_pass_re.delete(0, tk.END)
                        else:
                            tk.messagebox.showerror(title="Ошибка", message="Данный логин уже занят другим пользователем!")
                else:
                    tk.messagebox.showerror(title="Ошибка", message="Поле для повторного ввода пароля пустое!")
            else:
                tk.messagebox.showerror(title="Ошибка", message="Поле для ввода пароля пустое!")
        else:
            tk.messagebox.showerror(title="Ошибка", message="Поле для ввода логина пустое!")

class About(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_About()
    def init_About(self):
        self.title = ("О программе")
        self.geometry("220x100+400+300")
        self.resizable(False, False)


        self.About_label=tk.Label(self,text="Программа Входа/Регистрации")
        self.About_label.pack()
        self.About_label_ = tk.Label(self, text="с шифроманием для практики")
        self.About_label_.pack()
        self.About_label_2 = tk.Label(self, text="Дмитрий Сорока, 2020")
        self.About_label_2.pack()
        self.Ok_btn = tk.Button(self, text="OК", command=self.destroy)
        self.Ok_btn.pack()

        self.grab_set()
        self.focus_set()

def on_closing():
    if messagebox.askokcancel("Выход", "Вы действительно хотите выйти?"):
        with open('accounts.txt', 'wb') as out:
            pickle.dump(check, out)
        root.destroy()

if __name__ == "__main__":
    root=tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Вход")
    root.geometry("250x150+300+200")
    root.resizable(False, False)
    if os.path.getsize('accounts.txt') > 0:
        with open ('accounts.txt', 'rb') as inp:
            check = pickle.load(inp)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

