import tkinter as tk
from encrypt import load_key, generate_key, save_key
from interface import create_interface

root = tk.Tk()
root.title("Editor de Texto con Encriptación")

key_filename = "secret.key"
try:
    key = load_key(key_filename)
except FileNotFoundError:
    key = generate_key()
    save_key(key, key_filename)
    tk.messagebox.showinfo("Clave generada", f"Se ha generado y guardado una nueva clave: {key_filename}")

current_file_path = tk.StringVar()

create_interface(key, current_file_path, root)
root.mainloop()