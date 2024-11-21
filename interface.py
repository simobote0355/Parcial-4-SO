import tkinter as tk
from tkinter import messagebox
from editor import open_file, save_file, encrypt_new_file, create_new_file

def create_interface(key, current_file_path, root):
    text_area = tk.Text(root, wrap=tk.WORD, width=60, height=20)
    text_area.pack(pady=20)

    open_button = tk.Button(root, text="Abrir Archivo Encriptado", command=lambda: open_file(key, text_area, current_file_path))
    open_button.pack(side=tk.LEFT, padx=10)

    save_button = tk.Button(root, text="Guardar Archivo Encriptado", command=lambda: save_file(key, text_area, current_file_path))
    save_button.pack(side=tk.LEFT, padx=10)

    encrypt_button = tk.Button(root, text="Encriptar Nuevo Archivo", command=lambda: encrypt_new_file(key))
    encrypt_button.pack(side=tk.LEFT, padx=10)

    create_button = tk.Button(root, text="Crear Nuevo Archivo", command=lambda: create_new_file(text_area, current_file_path))
    create_button.pack(side=tk.LEFT, padx=10)