
# Editor de Texto con Encriptación

Simón Botero Villarraga
Pablo Moreno Quintero
Miguel Ángel Martínez García

## Descripción
Este proyecto implementa un editor de texto que permite trabajar con archivos encriptados. Utiliza **cifrado simétrico** mediante la biblioteca `cryptography` (Fernet) y proporciona una interfaz gráfica intuitiva desarrollada con `Tkinter`.

El sistema:
- Genera una clave de encriptación única al primer uso.
- Permite encriptar y desencriptar archivos automáticamente al guardar o abrir.
- Proporciona una experiencia de edición de texto estándar con funciones adicionales de seguridad.

---

## Funcionalidades
1. **Cifrado de Archivos**: Usa una clave secreta simétrica para proteger los datos.
2. **Desencriptado Automático**: Al abrir un archivo encriptado, se descifra automáticamente si la clave es correcta.
3. **Interfaz Gráfica**: Fácil de usar, diseñada con `Tkinter`.

---

## Instalación

### Requisitos
```bash
pip install cryptography
sudo apt-get install python3-tk
```

---

## Uso

### Ejecución
- El proyecto debe ser ejecutado en ambiente Linux.
```bash
python3 main.py
```

### Flujo
1. Si es la primera ejecución, se generará una clave de encriptación (`secret.key`) y se guardará localmente.
2. Al abrir un archivo:
   - Si está encriptado, el sistema lo desencripta automáticamente.
   - Si no, lo carga como texto normal.
3. Al guardar un archivo, el texto se cifra utilizando la clave.

---

## Estructura del Proyecto
- `main.py`: Punto de entrada principal. Configura la interfaz gráfica e inicializa la clave de encriptación.
- `encrypt.py`: Implementa las funciones de generación de clave, cifrado y descifrado de archivos.
- `interface.py`: Maneja los componentes gráficos de la aplicación.
- `secret.key`: Archivo donde se almacena la clave secreta generada (solo se crea si no existe).
- `ej.txt`: Archivo de texto de ejemplo.
- `editor.py`: Gestiona las funcionalidades del editor de texto.
