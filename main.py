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

    def open_signup(self):
        Registration()


class Registration(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_Registration()

    def init_Registration(self):
        self.title = ('Sign up')
        self.geometry("300x150+400+300")
        self.resizable(False, False)


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
