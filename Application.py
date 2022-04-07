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

    def callback(self, url):
        answer = messagebox.askyesno("Redirect", "This link will open a new browser window, do you wish to continue?")
        if answer:
            webbrowser.open_new(url)
        else:
            answer.conjugate()

    def open_file(self):
        pass

    def main(self):
        title = Label(self.root, text="Python File Comparer", font=("Helvetica", 20), bg=self.mainbgtext)
        title.place(x=110, y=10)

        credits = Label(self.root, text="Created by: Conner Lovely", font=("Helvetica", 10, "bold"), cursor="hand2", bg=self.mainbgtext)
        credits.place(x=325, y=475)
        credits.bind("<Button-1>", lambda e: self.callback("https://github.com/MioDevelops"))

        start = Button(self.root, text="Start Compairing", command=self.working(), bg=self.mainbgbutton, font=("Helvetica", 11, ("bold", "italic")))
        start.place(x=170, y=150)

        print(start.winfo_width())
        settings = Button(self.root, text="Settings", command=self.settings(), bg=self.mainbgbutton, font=("Helvetica", 11, ("bold", "italic")), width=int(start.winfo_width()/9.5))
        settings.place(x=170, y=210)

        credits = Button(self.root, text="Credits", command=self.results(), bg=self.mainbgbutton, font=("Helvetica", 11, ("bold", "italic")), width=int(start.winfo_width()/9.5))
        credits.place(x=170, y=270)

    def settings(self):
        pass

    def results(self):
        pass

    def working(self):
        pass

screen = Screen()

screen.main()

screen.root.mainloop()