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
        self.files = []
        self.root.update()

    def change_extension(self, ext):
        self.extensions = ext
        messagebox.showinfo("Notification", 'You have successfully changed the file extensions to "{}", you may now close this window'.format(ext))

    def change_language(self):
        ans = messagebox.askyesno("Notification", "Changing language to spanish, are you sure? cambiando idioma a español, estas seguro?")
        if(ans):
            pass
            #do the thing of changing languages
        pass

    def callback(self, url):
        answer = messagebox.askyesno("Redirect", "This link will open a new browser window, do you wish to continue?")
        if answer:
            webbrowser.open_new(url)
        else:
            answer.conjugate()

    def open_file(self, evt):
        self.root.update()

        filename = filedialog.askopenfilename()
        print(filename)
        if ".py" not in filename and self.extensions == ".py" and filename != "":
            messagebox.showinfo("Error", "As of your settings, you may only use .py files")
        elif filename == "":
            pass
        else:
            self.root.destroy()
            self.__init__()
            file = [filename, filename.split("/")[filename.count("/")]]
            self.files.append(file)
            if(evt == "initial"):
                self.working(evt="{}".format(filename.split("/")[filename.count("/")]), evt2=None)
            else:
                self.working(evt=self.files[0][0], evt2=filename.split("/")[filename.count("/")])

    def main(self):
        self.manifest()

        start = Button(self.root, text="Start Compairing", command=lambda : self.working(evt=None, evt2=None), bg=self.mainbgbutton, font=("Helvetica", 11, ("bold", "italic")), width=15)
        start.place(x=170, y=150)
      
        settings = Button(self.root, text="Settings", command=lambda : self.settings(), bg=self.mainbgbutton, font=("Helvetica", 11, ("bold", "italic")), width=15)
        settings.place(x=170, y=210)

        credits = Button(self.root, text="Credits", command=lambda : self.credits(), bg=self.mainbgbutton, font=("Helvetica", 11, ("bold", "italic")), width=15)
        credits.place(x=170, y=270)

        credits = Label(self.root, text="Created by: Conner Lovely", font=("Helvetica", 10, "bold"), cursor="hand2", bg=self.mainbgtext)
        credits.place(x=325, y=475)

    def settings(self):
        self.manifest()
        self.back_button.place(x=5, y=5)

        label = Label(self.root, text="Settings", font=("Helvetica", 20, "bold"), bg=self.mainbgtext)
        label.place(x=185, y=80)

        #still need to figure out how to open and run a different file
        Button(self.root, text="Change language to spanish/cambiar el idioma a español", font=("Helvetica", 9, ("bold", "italic")), bg=self.mainbgbutton, command=lambda : self.change_language()).place(x=70, y=140)
        
        if(self.extensions == ".py"):
            Button(self.root, text="Use all file extensions", font=("Helvetica", 10, ("bold", "italic")), bg=self.mainbgbutton, command= lambda : self.change_extension("All")).place(x=170, y=200)
        else:
            Button(self.root, text="Use only .py file extensions", font=("Helvetica", 10, ("bold", "italic")), bg=self.mainbgbutton, command= lambda : self.change_extension(".py")).place(x=155, y=200)

    def results(self):
        self.manifest()
        self.back_button.place(x=5, y=5)
        pass

    def working(self, evt, evt2):
        evt = None
        evt2 = None
        self.manifest()
        self.back_button.place(x=5, y=5)

        Label(self.root, text="Select the file you want to compare to", font=("Helvetica", 10, ("bold", "italic")), bg=self.mainbgtext).place(x=130, y=90)
        Button(self.root, text="Select file", font=("helvetica", 10, ("bold", "italic")), bg=self.mainbgbutton, command=lambda : self.open_file("initial")).place(x=200, y=120)
        Label(self.root, text="File Selected: {}".format(evt), font=("Helvetica", 12, ("bold", "italic")), bg=self.mainbgtext).place(x=135, y=150)
        Label(self.root, text="Select file for comparison", font=("Helvetica", 10, ("bold", "italic")), bg=self.mainbgtext).place(x=160, y=220)
        Button(self.root, text="Select file", font=("Helvetica", 10, ("bold", "italic")), bg=self.mainbgbutton, command=lambda : self.open_file("compare")).place(x=200, y=250)
        Label(self.root, text="File Selected: {}".format(evt2), font=("Helvetica", 12, ("bold", "italic")), bg=self.mainbgtext).place(x=135, y=280)
        if evt != None and evt2 != None:
            Button(self.root, text="Start File Comparing", font=("Helvetica", 10, ("bold", "italic")), bg=self.mainbgbutton, command=lambda : self.results()).place(x=200, y=300)

    def manifest(self):
        self.root.update()

        x = self.root.place_slaves()
        for i in x:
            i.place_forget()

        self.title.place(x=110, y=5)

    def credits(self):
        self.manifest()
        self.back_button.place(x=5, y=5)
        
        Label(self.root, text="Made by Conner Lovely", font=("Helvetica", 15, ("bold", "italic")), bg=self.mainbgtext).place(x=125, y=80)
        Label(self.root, text="Link to Github", font=("Helvetica", 12, ("bold", "italic")), bg=self.mainbgtext).place(x=190, y=130)
        label = Label(self.root, text="Here", font=("Helvetica", 10, ("bold", "italic", "underline")), bg=self.mainbgtext, fg="blue")
        label.place(x=225, y=160)
        label.bind("<Button-1>", lambda e: self.callback("https://github.com/MioDevelops"))
        Label(self.root, text="Link to Replit", font=("Helvetica", 12, ("bold", "italic")), bg=self.mainbgtext).place(x=190, y=190)
        label = Label(self.root, text="Here", font=("Helvetica", 10, ("bold", "italic", "underline")), bg=self.mainbgtext, fg="blue")
        label.place(x=225, y=220)
        label.bind("<Button-1>", lambda e: self.callback("https://replit.com/@MioYanaka"))
        Label(self.root, text="Link to Twitter", font=("Helvetica", 12, ("bold", "italic")), bg=self.mainbgtext).place(x=190, y=260)
        label = Label(self.root, text="Here", font=("Helvetica", 10, ("bold", "italic", "underline")), bg=self.mainbgtext, fg="blue")
        label.place(x=225, y=290)
        label.bind("<Button-1>", lambda e:self.callback(""))
        Label(self.root, text="Have a question? Email me!", font=("Helvetica", 12, ("bold", "italic")), bg=self.mainbgtext).place(x=135, y=350)
        label = Label(self.root, text="Here", font=("Helvetica", 10, ("bold", "italic", "underline")), bg=self.mainbgtext, fg="blue")
        label.place(x=225, y=380)
        label.bind("<Button-1>", lambda e: self.callback("mailto:MioDevelops@gmail.com"))

screen = Screen()

screen.main()

screen.root.mainloop()