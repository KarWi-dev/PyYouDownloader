from tkinter import Tk, Label, Button, Entry
from pytube import YouTube

class Root(Tk):
    def __init__(self):
        super().__init__()

        self.title_label = Label(self, text="\n\nA simple Youtube Downloader\n")
        self.title_label.pack()

        self.link_label = Label(self, text="\nLink:")
        self.link_label.pack()

        self.entry = Entry(self)
        self.entry.pack()

        self.button = Button(self, text="Download!", command=self.onclick)
        self.button.pack()

        self.labelHidden = Label(self, text="\n\n\n")
        self.labelHidden.pack()

        self.labelHidden2 = Label(self, text="")
        self.labelHidden2.pack()



    def onclick(self):
        link = self.entry.get()
        yt = YouTube(link).streams.get_by_itag(251)
        yt.download()
        self.labelHidden['text'] = "\n\nfertig"
        print("done")

root = Root()
root.mainloop()



