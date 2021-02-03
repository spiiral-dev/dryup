import tkinter as tk


class Menubar:

    def __init__(self, parent):
        font_specs = ("ubuntu", 12)

        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown.add_command(label="New File")
        file_dropdown.add_command(label="Open File")
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Save File")
        file_dropdown.add_command(label="Save As")
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit")

        menubar.add_cascade(label="File", menu=file_dropdown)


class DryUp:

    def __init__(self, master):
        master.title("Untitled - DryUp")
        master.geometry("1200x700")

        font_specs = ("ubuntu", 18)

        self.master = master

        self.textarea = tk.Text(master, font=font_specs)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.menubar = Menubar(self)



if __name__ == "__main__":
    master = tk.Tk()
    du = DryUp(master)
    master.mainloop()