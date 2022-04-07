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
        self.title_place = (110, 10)
        self.title.place(x=110, y=10)

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
        self.root.update()

        start = Button(self.root, text="Start Compairing", command=lambda : self.working(), bg=self.mainbgbutton, font=("Helvetica", 11, ("bold", "italic")), width=15)
        start.place(x=170, y=150)
      
        settings = Button(self.root, text="Settings", command=lambda : self.settings(), bg=self.mainbgbutton, font=("Helvetica", 11, ("bold", "italic")), width=15)
        settings.place(x=170, y=210)

        credits = Button(self.root, text="Credits", command=lambda : self.credits(), bg=self.mainbgbutton, font=("Helvetica", 11, ("bold", "italic")), width=15)
        credits.place(x=170, y=270)

        credits = Label(self.root, text="Created by: Conner Lovely", font=("Helvetica", 10, "bold"), cursor="hand2", bg=self.mainbgtext)
        credits.place(x=325, y=475)
        credits.bind("<Button-1>", lambda e: self.callback("https://github.com/MioDevelops"))

    def settings(self):
        self.minifest()
        pass

    def results(self):
        self.minifest()
        pass

    def working(self):
        self.minifest()
        pass

    def minifest(self):
        self.root.update()

        x = self.root.place_slaves()
        for i in x:
            i.place_forget()

        self.title.place(x=self.title_place[0], y=self.title_place[1])

    def credits(self):
        self.minifest()
        
        lable = Label(self.root, text="Made by Conner Lovely", font=("Helvetica", 15, ("bold", "italic")), bg=self.mainbgtext)
        lable.place(x=125, y=80)

screen = Screen()

screen.main()

screen.root.mainloop()