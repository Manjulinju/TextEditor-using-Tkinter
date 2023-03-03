from tkinter import *
from tkinter import Text
from tkinter import filedialog
# create main window
window = Tk()
window.title("Text Editor")

# create a text widget
text_widget = Text(window)
text_widget.pack()

# create menu bar
menu_bar = Menu(window)

def new_file():
    text_widget.delete("1.0", END)
    filepath = None
    window.title("Text Editor")

def open_file():
    filepath = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "r") as f:
        text_widget.delete(1.0, END)
        text_widget.insert('1.0', f.read())
        window.title(f"Text Editor App - {filepath}")

def save_file():
    filepath = filedialog.asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text File", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as f:
        text = text_widget.get(1.0, END)
        f.write(text)
    window.title(f"{filepath}")

# create file menu

file_menu = Menu(menu_bar)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Quit", command=window.quit)
#   add file to menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

window.config(menu=menu_bar)
window.mainloop()
