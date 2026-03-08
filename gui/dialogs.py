import tkinter as tk
from tkinter import Toplevel
import os
import webbrowser
from config.settings import (
    COLOR_PRIMARY, COLOR_TEXT_PRIMARY, COLOR_GOLD,
    LOGO_ICO, ROBOT_PNG, BOTON_PNG, BOTON1_PNG, FONT_DIALOG
)
from core.i18n import _
from .widgets import create_image_button

def center_window(ventana, ancho=None, alto=None):
    ventana.update_idletasks()
    if ancho is None: ancho = ventana.winfo_reqwidth()
    if alto is None: alto = ventana.winfo_reqheight()
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}')

class AboutDialog(Toplevel):
    """ Clon exacto y profesional (Sin Parpadeo) de MataData con i18n. """
    def __init__(self, parent, image_manager):
        super().__init__(parent)
        self.image_manager = image_manager
        
        # Ocultar inmediatamente para evitar flash visual
        self.withdraw()
        
        self.title(_("title.info"))
        self.geometry("300x181")
        self.config(bg=COLOR_PRIMARY)
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

        try:
            if os.path.exists(LOGO_ICO):
                self.iconbitmap(LOGO_ICO)
        except Exception:
            pass
            
        self._create_widgets()
        center_window(self, 300, 181)
        self.deiconify()

    def _create_widgets(self):
        frame_info = tk.Frame(self, bg=COLOR_PRIMARY)
        frame_info.pack(pady=15, padx=15, fill="both", expand=True)

        frame_info.grid_columnconfigure(0, weight=0)
        frame_info.grid_columnconfigure(1, weight=1)

        # Robot: Imagen original sin efectos
        robot_photo = self.image_manager.load(
            ROBOT_PNG, 
            size=(120, 120), 
            add_shadow_effect=False,
            add_relief_effect=False
        )
        if robot_photo:
            img_label = tk.Label(frame_info, image=robot_photo, bg=COLOR_PRIMARY)
            img_label.image = robot_photo
            img_label.grid(row=0, column=0, padx=(0, 10), rowspan=2, sticky="nsew")

        message = tk.Label(
            frame_info, 
            text=_("info.developed_by"),
            justify="center", 
            bg=COLOR_PRIMARY, 
            fg=COLOR_TEXT_PRIMARY,
            font=("Segoe UI", 11, "bold"),
            wraplength=180
        )
        message.grid(row=0, column=1, sticky="nsew", pady=(5, 10))

        btn_cont = create_image_button(
            frame_info, _("button.close"), self.destroy, self.image_manager, 
            BOTON_PNG, (110, 35)
        )
        btn_cont.grid(row=1, column=1, sticky="n")

def show_custom_message(root, title_key, message_key, image_manager, open_folder=None, **kwargs):
    """ Muestra un mensaje traducido con opción de abrir carpeta. """
    dialog = Toplevel(root)
    dialog.withdraw()
    dialog.title(_(title_key))
    dialog.config(bg=COLOR_PRIMARY)
    dialog.resizable(0, 0)
    dialog.transient(root)
    dialog.grab_set()

    try:
        if os.path.exists(LOGO_ICO):
            dialog.iconbitmap(LOGO_ICO)
    except Exception:
        pass
    
    frame = tk.Frame(dialog, bg=COLOR_PRIMARY)
    frame.pack(pady=20, padx=25, fill="both", expand=True)
    
    label = tk.Label(
        frame, text=_(message_key, **kwargs), bg=COLOR_PRIMARY, fg=COLOR_TEXT_PRIMARY, 
        font=("Segoe UI", 11, "bold"), wraplength=300, justify="center"
    )
    label.pack(expand=True, pady=(0, 20))
    
    btn_frame = tk.Frame(frame, bg=COLOR_PRIMARY)
    btn_frame.pack()

    if open_folder:
        def open_and_close():
            webbrowser.open(os.path.dirname(os.path.abspath(open_folder)))
            dialog.destroy()
        
        # Añadimos espacios antes de "ABRIR" para desplazarlo a la derecha y que no choque con la carpeta
        create_image_button(btn_frame, "   " + _("button.open"), open_and_close, image_manager, BOTON1_PNG, (110, 35)).pack(side="left", padx=5)

    create_image_button(btn_frame, _("button.ok"), dialog.destroy, image_manager, BOTON_PNG, (110, 35)).pack(side="left", padx=5)

    center_window(dialog)
    dialog.deiconify()
