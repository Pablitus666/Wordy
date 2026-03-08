import tkinter as tk
from config.settings import COLOR_PRIMARY, COLOR_TEXT_PRIMARY, COLOR_GOLD, FONT_BUTTON

def create_image_button(parent, text, command, image_manager, filename, image_size=(150, 45)):
    """
    Crea un botón personalizado siguiendo la técnica exacta de MetaData:
    Solo sombra, sin efecto de relieve (que causa el borde rectangular).
    """
    # Cargar imagen con la técnica de MetaData (Sombra, pero SIN relieve)
    photo = image_manager.load(
        filename, 
        size=image_size, 
        add_shadow_effect=True,
        add_relief_effect=False,  # ELIMINADO: esto causaba el reborde superior izquierdo
        shadow_offset=(3, 3),
        shadow_color=(0, 0, 0, 100),
        blur_radius=3,
        border=5
    )

    # Crear el botón con los parámetros de MetaData
    button = tk.Button(
        parent,
        text=text,
        image=photo,
        compound="center",
        command=command,
        relief="flat",
        bg=COLOR_PRIMARY,
        fg=COLOR_TEXT_PRIMARY,
        activebackground=COLOR_PRIMARY,
        activeforeground=COLOR_TEXT_PRIMARY,
        font=FONT_BUTTON,
        borderwidth=0,
        highlightthickness=0,
        padx=0,
        pady=0,
        takefocus=0,
        cursor="hand2"
    )

    if photo:
        button.photo = photo

    # Hover (estilo MetaData)
    button.bind("<Enter>", lambda e: button.config(fg=COLOR_GOLD))
    button.bind("<Leave>", lambda e: button.config(fg=COLOR_TEXT_PRIMARY))
    
    return button
