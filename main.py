import tkinter as tk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_opn_signup = tk.Button(toolbar, text="Sign Up", command=self.open_signup, bd=0, compound=tk.TOP)
        btn_opn_signup.pack(side=tk.LEFT)

        btn_opn_about = tk.Button(toolbar, text="About", command=self.open_about, bd=0, compound=tk.TOP)
        btn_opn_about.pack(side=tk.LEFT)

    def open_signup(self):
        Registration()

    def open_about(self):
        About()


class Registration(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_Registration()

    def init_Registration(self):
        self.title = ("Sign up")
        self.geometry("300x170+400+300")
        self.resizable(False, False)

        self.Reg_label = tk.Label(self,text="Enter your nickname:")
        self.Reg_label.pack()
        self.Reg_nick = tk.Entry(self)
        self.Reg_nick.pack()
        self.Reg_label_pass = tk.Label(self,text="Enter your pasword:")
        self.Reg_label_pass.pack()
        self.Reg_pass = tk.Entry(self,show="*")
        self.Reg_pass.pack()
        self.Reg_label_pass_re = tk.Label(self,text="Enter your password again:")
        self.Reg_label_pass_re.pack()
        self.Reg_pass_re = tk.Entry(self,show="*")
        self.Reg_pass_re.pack()
        self.Reg_btn = tk.Button(self,text="Sign up!")
        self.Reg_btn.place(x=90, y=130)
        self.Cancel_btn=tk.Button(self, text="Cancel")
        self.Cancel_btn.place(x=170, y=130)


        self.grab_set()
        self.focus_set()


class About(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_About()

    def init_About(self):
        self.title = ("About")
        self.geometry("220x80+400+300")
        self.resizable(False, False)


        self.About_label=tk.Label(self,text="Sign in/Sign up program for practice")
        self.About_label.pack()
        self.About_label_2 = tk.Label(self, text="Soroka Dmitriy, 2020")
        self.About_label_2.pack()


        self.grab_set()
        self.focus_set()





if __name__ == "__main__":
    root=tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Sign in")
    root.geometry("350x200+300+200")
    root.resizable(False, False)
    root.mainloop()
