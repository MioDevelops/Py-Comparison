from tkinter import *
from tkinter import filedialog, messagebox
import webbrowser

class Screen():
    def __init__(self):
        self.root = Tk()
        self.root.title("Python File Comparer")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(background="#1ecbe1")
        self.mainbgtext = "#1ecbe1"
        self.mainbgbutton = "#1695a5"
        self.title = Label(self.root, text="Python File Comparer", font=("Helvetica", 20), bg=self.mainbgtext)
        self.title.place(x=110, y=5)
        self.back_button = Button(self.root, text="Back", font=("Helvetica", 10, ("bold", "italic")), bg=self.mainbgbutton, command=lambda : self.main())
        self.back_button.place(x=5,y=5)
        self.extensions=".py"
        self.root.update()

    def change_extension(self, ext):
        self.extensions = ext
        messagebox.showinfo("Notification", 'You have successfully changed the file extensions to "{}", you may now close this window'.format(ext))

    def callback(self, url):
        answer = messagebox.askyesno("Redirect", "This link will open a new browser window, do you wish to continue?")
        if answer:
            webbrowser.open_new(url)
        else:
            answer.conjugate()

    def open_file(self):
        self.root.update()
        pass

    def main(self):
        self.manifest()

        start = Button(self.root, text="Start Compairing", command=lambda : self.working(), bg=self.mainbgbutton, font=("Helvetica", 11, ("bold", "italic")), width=15)
        start.place(x=170, y=150)
      
        settings = Button(self.root, text="Settings", command=lambda : self.settings(), bg=self.mainbgbutton, font=("Helvetica", 11, ("bold", "italic")), width=15)
        settings.place(x=170, y=210)

        credits = Button(self.root, text="Credits", command=lambda : self.credits(), bg=self.mainbgbutton, font=("Helvetica", 11, ("bold", "italic")), width=15)
        credits.place(x=170, y=270)

        credits = Label(self.root, text="Created by: Conner Lovely", font=("Helvetica", 10, "bold"), cursor="hand2", bg=self.mainbgtext)
        credits.place(x=325, y=475)

    def settings(self):
        self.manifest()
        self.back_button.place(x=self.back_button.winfo_rootx() - 1, y=self.back_button.winfo_rooty() - 25)

        label = Label(self.root, text="Settings", font=("Helvetica", 20, "bold"), bg=self.mainbgtext)
        label.place(x=185, y=80)

        #still need to figure out how to open and run a different file
        button = Button(self.root, text="Change language to spanish/cambiar el idioma a español", font=("Helvetica", 9, ("bold", "italic")), bg=self.mainbgbutton, command=None)
        button.place(x=30, y=140)
        
        if(self.extensions == ".py"):
            button = Button(self.root, text="Use all file extensions", font=("Helvetica", 10, ("bold", "italic")), bg=self.mainbgbutton, command= lambda : self.change_extension("All"))
            button.place(x=150, y=200)
        else:
            button = Button(self.root, text="Use only .py file extensions", font=("Helvetica", 10, ("bold", "italic")), bg=self.mainbgbutton, command= lambda : self.change_extension(".py"))
            button.place(x=135, y=200)

    def results(self):
        self.manifest()
        self.back_button.place(x=self.back_button.winfo_rootx() - 1, y=self.back_button.winfo_rooty() - 25)
        pass

    def working(self):
        self.manifest()
        self.back_button.place(x=self.back_button.winfo_rootx() - 1, y=self.back_button.winfo_rooty() - 25)
        pass

    def manifest(self):
        self.root.update()

        x = self.root.place_slaves()
        for i in x:
            i.place_forget()

        self.title.place(x=self.title.winfo_rootx() - 1, y=self.title.winfo_rooty() - 25)

    def credits(self):
        self.manifest()
        self.back_button.place(x=self.back_button.winfo_rootx() - 1, y=self.back_button.winfo_rooty() - 25)
        
        lable = Label(self.root, text="Made by Conner Lovely", font=("Helvetica", 15, ("bold", "italic")), bg=self.mainbgtext)
        lable.place(x=125, y=80)

        label = Label(self.root, text="Link to Github", font=("Helvetica", 12, ("bold", "italic")), bg=self.mainbgtext)
        label.place(x=190, y=130)

        label = Label(self.root, text="Here", font=("Helvetica", 10, ("bold", "italic", "underline")), bg=self.mainbgtext, fg="blue")
        label.place(x=235, y=160)
        label.bind("<Button-1>", lambda e: self.callback("https://github.com/MioDevelops"))

        label = Label(self.root, text="Link to Replit", font=("Helvetica", 12, ("bold", "italic")), bg=self.mainbgtext)
        label.place(x=190, y=190)

        label = Label(self.root, text="Here", font=("Helvetica", 10, ("bold", "italic", "underline")), bg=self.mainbgtext, fg="blue")
        label.place(x=235, y=220)
        label.bind("<Button-1>", lambda e: self.callback("https://replit.com/@MioYanaka"))

        label = Label(self.root, text="Link to Twitter", font=("Helvetica", 12, ("bold", "italic")), bg=self.mainbgtext)
        label.place(x=190, y=260)

        label = Label(self.root, text="Here", font=("Helvetica", 10, ("bold", "italic", "underline")), bg=self.mainbgtext, fg="blue")
        label.place(x=235, y=290)
        label.bind("<Button-1>", lambda e:self.callback(""))

        label = Label(self.root, text="Have a question? Email me!", font=("Helvetica", 12, ("bold", "italic")), bg=self.mainbgtext)
        label.place(x=135, y=350)

        label = Label(self.root, text="Here", font=("Helvetica", 10, ("bold", "italic", "underline")), bg=self.mainbgtext, fg="blue")
        label.place(x=235, y=380)
        label.bind("<Button-1>", lambda e: self.callback("https://mail.google.com/mail/?view=cm&fs=1%to=MioDevelops@gmail.com"))

screen = Screen()

screen.main()

screen.root.mainloop()