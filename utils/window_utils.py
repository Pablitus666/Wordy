import tkinter as tk

def center_window(window, width, height):
    """ Centra una ventana en la pantalla. """
    window.update_idletasks()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def set_modern_theme(widget, bg, fg):
    """ Aplica colores base a un widget. """
    widget.config(bg=bg, fg=fg)
