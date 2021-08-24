import tkinter as tk
from tkinter import *
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox as mb
from main import export_ebook_wordlist
default_path = os.path.expanduser('~/Desktop')
import_valid_types = [("import ebook file","*.epub")]
export_valid_types = [("export word list ","*.xlsx")]

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyWordList")
        self.label_text = "please select your epub book"
        self.label = tk.Label(self, text=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=20)
        self.import_path_text = tk.StringVar()
        self.export_path_text = tk.StringVar()

        self.select_import_button = tk.Button(self,text="import book",
                                   command=self.select_import_path)
        self.select_import_button.pack(side=tk.TOP,  anchor=S, expand=YES)
        self.selected_import_path_label = tk.Label(self, text="~/", bg="blue", fg="white",textvariable=self.import_path_text)
        self.selected_import_path_label.pack(fill=X,padx=50)



        self.select_export_button = tk.Button(self, text="export path",
                                       command=self.select_export_path)
        self.select_export_button.pack(side=tk.TOP,  anchor=S, expand=YES,pady=(20,0))
        self.selected_export_path_label = tk.Label(self, text="~/Desktop/wordlist.xlsx", bg="blue", fg="white",textvariable=self.export_path_text)
        self.selected_export_path_label.pack(fill=X, padx=50)

        self.label_text2 = "set your vocabulary level/count (eg:3000)"
        self.label2 = tk.Label(self, text=self.label_text2)
        self.label2.pack(fill=tk.BOTH, expand=1, padx=100, pady=20)

        self.level_input = tk.Entry(self)
        self.level_input.pack(side=tk.TOP,  anchor=S, expand=YES,pady=(0,0))

        export_button = tk.Button(self, text="export",
                                     command=self.export)
        export_button.pack(side=tk.TOP,  anchor=S, expand=YES,pady=(20,20))


    def select_import_path(self):
        filename = askopenfilename(initialdir=default_path,
                                   message="Choose one or more files",
                                   multiple=True,
                                   title="File Selector",
                                   filetypes=import_valid_types)
        filename = list(filename)[0]
        print("import filename:{}".format(filename))
        self.import_path_text.set(filename)

    def select_export_path(self):
        filename = asksaveasfilename(initialdir=default_path,
                                     title="Select Filename to save",
                                     filetypes=export_valid_types)

        print("exprot filename:{}".format(filename))
        self.export_path_text.set(filename)

    def export(self):
        export_path = self.export_path_text.get()
        import_path = self.import_path_text.get()
        number = self.level_input.get()

        print("export_path_text:{}".format(export_path))
        print("import_path_text:{}".format(import_path))
        print("number = {}".format(number))

        if not import_path:
            mb.showwarning('OK', 'please select a import file')
            return
        if not export_path:
            mb.showwarning('OK', 'please select a export path')
            return
        if not number:
            mb.showwarning('OK', 'please input your vocabulary level/count')
            return 

        export_ebook_wordlist(book_path=import_path,export_path=export_path,my_word_count=int(number))

if __name__ == "__main__":
    window = Window()
    window.mainloop()