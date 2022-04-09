from email import message
from tkinter import *
from tkinter import filedialog, messagebox
import webbrowser

files = []
files_dir = []
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

    def search_lines(self, files_dir):
        if(files_dir[0] == files_dir[1]):
            messagebox.showerror("Error", "You cannot select two of the same files, please press refresh and change them")
            return
        else:
            self.results()

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

    def open_file(self, event, args):
        self.root.update()

        if("None" not in args[0] and event == "initial" or "None" not in args[1] and event == "compare"):
            messagebox.showinfo("Notification", "You may not select another file, please refresh files if you wish to change it")
            return
        elif(event == "compare" and "None" in args[0]):
            messagebox.showerror("Error", "You must select the file to compare to first")
            return
        else:
            pass
        filename = filedialog.askopenfilename()
        if ".py" not in filename and self.extensions == ".py" and filename != "":
            messagebox.showinfo("Error", "As of your settings, you may only use .py files")
        elif filename == "":
            pass
        else:
            self.root.destroy()
            self.__init__()
            if(event == "initial"):
                self.working(evt="{}".format(filename.split("/")[filename.count("/")]), evt2=None)
                files.append(filename.split("/")[filename.count("/")])
                files_dir.append(filename)
            else:
                files.append(filename.split("/")[filename.count("/")])
                files_dir.append(filename)
                self.working(evt=files[0], evt2=files[1])

    def main(self):
        self.manifest()

        start = Button(self.root, text="Start Compairing", command=lambda : self.working(evt=None, evt2=None), bg=self.mainbgbutton, font=("Helvetica", 11, ("bold", "italic")), width=15)
        start.place(x=170, y=150)
      
        settings = Button(self.root, text="Settings", command=lambda : self.settings(), bg=self.mainbgbutton, font=("Helvetica", 11, ("bold", "italic")), width=15)
        settings.place(x=170, y=210)

        credits = Button(self.root, text="Credits", command=lambda : self.credits(), bg=self.mainbgbutton, font=("Helvetica", 11, ("bold", "italic")), width=15)
        credits.place(x=170, y=270)

    def refresh(self):
        files.clear()
        self.working(evt=None, evt2=None)
        files_dir.clear()

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
        self.manifest(title=True)
        Button(self.root, text="Main Page", font=("Helvetica", 10, ("bold", "italic")), bg=self.mainbgbutton, command=lambda : self.main()).place(x=10, y=5)
        Label(self.root, text="Please wait as your results are being generated...", font=("Helvetica", 13, ("bold", "italic")), bg=self.mainbgtext).place(x=100, y=6)
        pass

    def working(self, evt, evt2):
        self.manifest()
        self.back_button.place(x=5, y=5)

        file1 = Label(self.root, text="File Selected: {}".format(evt), font=("Helvetica", 12, ("bold", "italic")), bg=self.mainbgtext)
        file1.place(x=135, y=150)
        file2 = Label(self.root, text="File Selected: {} ".format(evt2), font=("Helvetica", 12, ("bold", "italic")), bg=self.mainbgtext)
        file2.place(x=135, y=280)
        Button(self.root, text="Refresh Files", font=("Helvetica", 10, ("bold", "italic")), bg=self.mainbgbutton, command=lambda : self.refresh()).place(x=400, y=5)
        Label(self.root, text="Select the file you want to compare to", font=("Helvetica", 10, ("bold", "italic")), bg=self.mainbgtext).place(x=130, y=90)
        Button(self.root, text="Select file", font=("helvetica", 10, ("bold", "italic")), bg=self.mainbgbutton, command=lambda : self.open_file("initial", [file1["text"], file2["text"]])).place(x=200, y=120)
        Label(self.root, text="Select file for comparison", font=("Helvetica", 10, ("bold", "italic")), bg=self.mainbgtext).place(x=160, y=220)
        Button(self.root, text="Select file", font=("Helvetica", 10, ("bold", "italic")), bg=self.mainbgbutton, command=lambda : self.open_file("compare", [file1["text"], file2["text"]])).place(x=200, y=250)
        if (evt != None and evt2 != None):
            Button(self.root, text="Start File Comparing", font=("Helvetica", 10, ("bold", "italic")), bg=self.mainbgbutton, command=lambda : self.search_lines(files_dir)).place(x=170, y=340)

    def manifest(self, title=False):
        self.root.update()

        x = self.root.place_slaves()
        for i in x:
            i.place_forget()

        if not title:
            self.title.place(x=110, y=5)
        else:
            pass


    def credits(self):
        self.manifest()
        self.back_button.place(x=5, y=5)
        
        Label(self.root, text="Made by Conner Lovely", font=("Helvetica", 15, ("bold", "italic")), bg=self.mainbgtext).place(x=125, y=80)
        Label(self.root, text="Link to Github", font=("Helvetica", 12, ("bold", "italic")), bg=self.mainbgtext).place(x=190, y=130)
        label = Label(self.root, text="Here", font=("Helvetica", 10, ("bold", "italic", "underline")), bg=self.mainbgtext, fg="blue", cursor="hand2")
        label.place(x=225, y=160)
        label.bind("<Button-1>", lambda e: self.callback("https://github.com/MioDevelops"))
        Label(self.root, text="Link to Replit", font=("Helvetica", 12, ("bold", "italic")), bg=self.mainbgtext).place(x=190, y=190)
        label = Label(self.root, text="Here", font=("Helvetica", 10, ("bold", "italic", "underline")), bg=self.mainbgtext, fg="blue", cursor="hand2")
        label.place(x=225, y=220)
        label.bind("<Button-1>", lambda e: self.callback("https://replit.com/@MioYanaka"))
        Label(self.root, text="Link to Twitter", font=("Helvetica", 12, ("bold", "italic")), bg=self.mainbgtext).place(x=190, y=260)
        label = Label(self.root, text="Here", font=("Helvetica", 10, ("bold", "italic", "underline")), bg=self.mainbgtext, fg="blue", cursor="hand2")
        label.place(x=225, y=290)
        label.bind("<Button-1>", lambda e:self.callback(""))
        Label(self.root, text="Have a question? Email me!", font=("Helvetica", 12, ("bold", "italic")), bg=self.mainbgtext).place(x=135, y=350)
        label = Label(self.root, text="Here", font=("Helvetica", 10, ("bold", "italic", "underline")), bg=self.mainbgtext, fg="blue", cursor="hand2")
        label.place(x=225, y=380)
        label.bind("<Button-1>", lambda e: self.callback("mailto:MioDevelops@gmail.com"))

screen = Screen()

screen.main()

screen.root.mainloop()