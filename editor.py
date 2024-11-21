import tkinter as tk
from tkinter import filedialog, messagebox
from encrypt import encrypt_file, decrypt_file

def open_file(key, text_area, current_file_path):
    file_path = filedialog.askopenfilename(title="Open Encrypted File")
    if not file_path:
        return

    try:
        decrypt_file(file_path, key)

        with open(file_path, 'r') as file:
            content = file.read()
            text_area.delete(1.0, tk.END)  
            text_area.insert(tk.END, content)  

        current_file_path.set(file_path)  
    except Exception as e:
        messagebox.showerror("Error", f"Error al abrir el archivo: {e}")

def save_file(key, text_area, current_file_path):
    file_path = current_file_path.get()
    if not file_path:
        return

    try:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))  

        encrypt_file(file_path, key)

        text_area.delete(1.0, tk.END)

        messagebox.showinfo("Success", "Archivo guardado y encriptado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar el archivo: {e}")

def encrypt_new_file(key):
    file_path = filedialog.askopenfilename(title="Seleccionar archivo para encriptar")
    if not file_path:
        return

    try:
        encrypt_file(file_path, key)
        messagebox.showinfo("Success", "Archivo encriptado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al encriptar el archivo: {e}")

def create_new_file(text_area, current_file_path):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return  

    text_area.delete(1.0, tk.END)
    current_file_path.set(file_path)

    with open(file_path, 'w') as new_file:
        new_file.write("")