import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class Menubar:

    def __init__(self, parent):
        font_specs = ("Helvetica", 9)

        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)

        file = tk.Menu(menubar, font=font_specs, tearoff=0)
        file.add_command(label="New File",
                         accelerator="Ctrl+N",
                         command=parent.new_file)
        file.add_command(label="Open File",
                         accelerator="Ctrl+O",
                         command=parent.open_file)
        file.add_command(label="Save File",
                         accelerator="Ctrl+S",
                         command=parent.save_file)
        file.add_command(label="Save As",
                         accelerator="Ctrl+Shift+S",
                         command=parent.save_as)
        file.add_separator()
        file.add_command(label="Exit",
                         command=parent.master.destroy)

        about = tk.Menu(menubar, font=font_specs, tearoff=0)
        about.add_command(label='Release Notes', command=parent.release_notes)
        about.add_separator()
        about.add_command(label='About', command=parent.about)
        about.add_command(label='Credits', command=parent.credits)

        menubar.add_cascade(label="File", menu=file)
        menubar.add_cascade(label="Help", menu=about)


class Statusbar:

    def __init__(self, parent):
        font_specs = ("Helvetica", 9)

        self.status = tk.StringVar()
        self.status.set("DryUp - 1.0.2 Ruload")

        label = tk.Label(parent.textarea, textvariable=self.status, fg="black", bg="lightgrey", anchor='sw', font=font_specs)
        label.pack(side=tk.BOTTOM, fill=tk.BOTH)


class DryUp:

    def __init__(self, master):
        master.title("Untitled - DryUp")
        master.geometry("1200x700")

        font_specs = ("Helvetica", 18)

        self.master = master
        self.filename = None

        self.textarea = tk.Text(master, font=font_specs)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.menubar = Menubar(self)
        self.statusbar = Statusbar(self)

        self.bind_shortcuts()

    def set_window_title(self, name=None):
        if name:
            self.master.title(name + " - DryUp")
        else:
            self.master.title("Untitled - DryUp") 

    def new_file(self, *args):
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()

    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), 
                       ("Text Files", "*.txt"),
                       ("Python Scripts", "*.py"),
                       ("Markdown Documents", "*.md"),
                       ("JavaScript Files", "*.js"),
                       ("HTML Files", "*.html"),
                       ("CSS Files", "*.css")])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
            self.set_window_title(self.filename)   

    def save_file(self, *args):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
                # self.statusbar.update_status(True)
            except Exception as e:
                messagebox.showerror(e)
        else:
            self.save_as()

    def save_as(self, *args):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"), 
                        ("Text Files", "*.txt"),
                        ("Python Scripts", "*.py"),
                        ("Markdown Documents", "*.md"),
                        ("JavaScript Files", "*.js"),
                        ("HTML Files", "*.html"),
                        ("CSS Files", "*.css")])
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
            # self.statusbar.update_status(True)
        except Exception as e:
            messagebox.showerror('Error!', e)

    def release_notes(self):
        messagebox.showinfo('Release Notes!', 'None Avalible')

    def credits(self):
        messagebox.showinfo('Credits', 'Made and developed by Spiiral-Dev (GitHub)')

    def about(self):
        messagebox.showinfo('About', 'DryUp is a super lightweight and free text editor, with 0 telemetry. Nada, nothing.')

    def bind_shortcuts(self):
        self.textarea.bind('<Control-n>', self.new_file)
        self.textarea.bind('<Control-o>', self.open_file)
        self.textarea.bind('<Control-s>', self.save_file)
        self.textarea.bind('<Control-S>', self.save_as)

if __name__ == "__main__":
    master = tk.Tk()
    du = DryUp(master)
    master.mainloop()