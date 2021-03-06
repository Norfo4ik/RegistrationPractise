import tkinter as tk  # Подключаем нужные бибилотеки: tkinter для отрисовки интерфейсов
from tkinter import messagebox  # hashlib для шифрования паролей
import hashlib  # os для генерации соли и проверки файла с паролями на пустоту
import os  # pickle для загрузки и выгрузки из файла
import pickle

check = {}  # Наш словарь с данными о пользователях


class Main(tk.Frame):  # Класс оновного окна
    def __init__(self, root):  # Конструктор
        super().__init__(root)
        self.init_main()  # Вызываем функцию инициализации

    def init_main(self):  # Ф-ия инициализации
        toolbar = tk.Frame(bg='ghost white', bd=2)  # Создаем объект тулбар
        toolbar.pack(side=tk.TOP, fill=tk.X)  # Пакуем(размещаем на окне)

        btn_opn_signup = tk.Button(toolbar, text="Sign Up", command=self.open_signup, bg='ghost white', bd=0,
                                   compound=tk.TOP)  # Создаем кнопку "Зарегестрироваться"
        btn_opn_signup.pack(side=tk.LEFT)  # Размещаем на тулбаре
        btn_opn_about = tk.Button(toolbar, text="About", command=self.open_about, bd=0, bg='ghost white',
                                  compound=tk.TOP)  # Создаем кнопку "О программе"
        btn_opn_about.pack(side=tk.LEFT)  # Размещаем на тулбаре
        Sign_label = tk.Label(text="Enter your nickname:")  # Надпись - приглашение ввода логина
        Sign_label.pack()  # Размещаем ее
        Sign_Entry = tk.Entry()  # Поле для ввода логина
        Sign_Entry.pack()  # Размещаем его
        Sign_lable_pas = tk.Label(text="Enter your pasword:")  # Надпись - приглашение для ввода пароля
        Sign_lable_pas.pack()  # Размещаем ее
        Sign_Entry_pas = tk.Entry(show="*")  # Поле для ввода пароля, вводимые символы заменяем на звездочку
        Sign_Entry_pas.pack()  # Размещаем его
        # Кнопка входа, вызываем ф-цию входа, передаем данные из полей:
        Sign_btn = tk.Button(text="Sign in!", command=lambda: self.signin(Sign_Entry.get(), Sign_Entry_pas.get()))  #
        Sign_btn.place(x=70, y=120)  # Размещаем ее
        Cancel_btn = tk.Button(text="Exit", command=on_closing)  # Кнопка закрытия окна(выход)
        Cancel_btn.place(x=130, y=120)  # Размещаем ее

    def open_signup(self):  # Ф-ция вызова окна класса регистрации
        Registration()

    def open_about(self):  # Ф-ция вызова окна класса о программе
        About()

    def signin(self, login, passw):  # Ф-ция проверки коррекности данных для входа и входа
        if check.get(login) is None:  # Если словарь по данному ключу возвращает пустое значение
            tk.messagebox.showerror(title="Error", message="User didn't find")  # Выводим, что пользователь под таким
            # логином не найден
        else:  # Иначе
            salt = check[login]['salt']  # Получаем "соль"
            key = check[login]['key']  # Получаем хеш
            entered_key = hashlib.pbkdf2_hmac('sha256', passw.encode('utf-8'), salt, 100000)  # Получаем хеш
            # введенного ключа с оспользованием соли, полученной по ключу
            if key == entered_key:  # Если хеши равны
                tk.messagebox.showinfo(title="Success", message="You successfully signin")  # Выводим сообщение об
                # успешном входе
            else:  # Иначе
                tk.messagebox.showinfo(title="Error", message="You didn't signup")  # Введен неверный пароль


class Registration(tk.Toplevel):  # Класс окна регистрации (Наследуемся от главного окна)
    def __init__(self):  # Конструктор
        super().__init__(root)
        self.init_Registration()  # Иницилизируем элементы

    def init_Registration(self):  # Ф-ция инициализации
        self.title = "Sign up"  # Заголовок
        self.geometry("250x160+400+300")  # Размеры и положение
        self.resizable(False, False)  # Задаем параметры, чтобы нельзя было изменять окно

        self.Reg_label = tk.Label(self, text="Enter your nickname:")  # Надпись - приглашение ввести логин
        self.Reg_label.pack()  # Размещаем надпись
        self.Reg_nick = tk.Entry(self)  # Поле для ввода лонина
        self.Reg_nick.pack()  # Размещаем поле
        self.Reg_label_pass = tk.Label(self, text="Enter your pasword:")  # Надпись - приглашение для ввода пароля
        self.Reg_label_pass.pack()  # Размещаем надпись
        self.Reg_pass = tk.Entry(self, show="*")  # Поле для ввода пароля, вводимые символы - скрываем
        self.Reg_pass.pack()  # Размещаем поле
        self.Reg_label_pass_re = tk.Label(self, text="Enter your password again:")  # Надпись приглашение для
        # повторного ввода пароля
        self.Reg_label_pass_re.pack()  # Размещаем надпись
        self.Reg_pass_re = tk.Entry(self, show="*")  # Поле для повторного ввода пароля
        self.Reg_pass_re.pack()  # Размещаем поле
        Reg_btn = tk.Button(self, text="Sign up!",
                            command=lambda: self.record_signup(self.Reg_nick.get(), self.Reg_pass.get(),
                                                               self.Reg_pass_re.get()))  # Кнопка регистрации,
        # вызываем ф-цию регистрации, передаем введеные в поля значения
        Reg_btn.place(x=60, y=130)  # Размещаем кнопку
        Cancel_btn = tk.Button(self, text="Cancel", command=self.destroy)  # Кнопка отмены
        Cancel_btn.place(x=130, y=130)  # Размещаем кнопку

        self.grab_set()  # Устанавливаем фокус на это окно, другие окна не доступны
        self.focus_set()

    def record_signup(self, login, passw, passw_re):  # Ф-ция для записи данных о регистрации
        if self.Reg_nick.get():  # Если поле для ввода логина не пустое
            if self.Reg_pass.get():  # Если поле для ввода пароля не пустое
                if self.Reg_pass_re.get():  # Если поле для повторного ввода пароля не пустое
                    if passw != passw_re:  # Если пароли не совпадают
                        # Выводим сообщение о том, что пароли не совпадают :
                        tk.messagebox.showerror(title="Pass error", message="Entered passwords don`t much!")
                    else: # Иначе
                        if check.get(login) is None:  # Если такого логина в словаре нет
                            tk.messagebox.showinfo(title="Success", message="You successfully signup") # Выводим
                            # сообщение об успешной регистрации
                            salt = os.urandom(32)  # Генерируем соль
                            key = hashlib.pbkdf2_hmac('sha256', passw.encode('utf-8'), salt, 100000)  # Содаем хеш
                            # пароля
                            check[login] = {  # Добавляем наши данные в словарь
                                'salt': salt,
                                'key': key
                            }
                            self.Reg_nick.delete(0, tk.END)  # Очищаем поля для ввода
                            self.Reg_pass.delete(0, tk.END)
                            self.Reg_pass_re.delete(0, tk.END)
                        else:  # Иначе
                            # Выводим сообщение о том, что данный ник используется:
                            tk.messagebox.showerror(title="Nick error!", message="Entered nick is already in use!")
                else:  # Иначе
                    # Выводим сообщение, что поле для повторного ввода пароля пустое:
                    tk.messagebox.showerror(title="Pass error", message="Password re-entry is empty!")
            else:  # Иначе
                # Выводим сообщение, что поле для ввода пароля пустое:
                tk.messagebox.showerror(title="Pass error", message="Password entry is empty!")
        else:  # Иначе
            # Выводим сообщение, что поле для ввода логина пустое:
            tk.messagebox.showerror(title="Nickname error", message="Nickname entry is empty!")


class About(tk.Toplevel):  # Класс окна о программе, наследуемся от главного окна
    def __init__(self):  # Конструктор
        super().__init__(root)
        self.init_About()  # Ф-ция инициализации окна (вызов)

    def init_About(self): # Ф-ция инициализации окна
        self.title = "About"  # Заголовок окна
        self.geometry("220x80+400+300")  # Размеры и положение окна
        self.resizable(False, False)  # Задаем параметры окна, чтоб нельзя было изменить размер
        # Надписи информация о программе
        self.About_label = tk.Label(self, text="Sign in/Sign up program for practice")
        self.About_label.pack()
        self.About_label_2 = tk.Label(self, text="Soroka Dmitriy, 2020")
        self.About_label_2.pack()  # Размещаем надписи
        self.Ok_btn = tk.Button(self, text="Ok", command=self.destroy)  # Кнопка ОК для ознакомления и выхода
        self.Ok_btn.pack()  # Размещаем кнопку

        self.grab_set()  # Устанавливаем фокус на окне
        self.focus_set()


def on_closing():  # Функция выгрузки данных в файл при закрытии главного окна
    if messagebox.askokcancel("Quit", "Do you want to quit?"):  # Выводим окно подтверждения выхода
        with open('accounts.txt', 'wb') as out:  # Если подтвердили, то открываем файл на запись и выводим наш
            # словарь в файл
            pickle.dump(check, out)
        root.destroy()  # Уничтожаем окно


if __name__ == "__main__":  # Основная функция, если имя файла маин, создаем экземпляр нашего окна, задаем параметры
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Sign in")
    root.geometry("250x150+300+200")
    root.resizable(False, False)
    if os.path.getsize('accounts.txt') > 0: # Загружаем данные из файла для работы программы
        with open('accounts.txt', 'rb') as inp:
            check = pickle.load(inp)

    root.protocol("WM_DELETE_WINDOW", on_closing)  # Если окно уничтожается, запускаем функцию закрытия
    root.mainloop()  # Основной цикл
