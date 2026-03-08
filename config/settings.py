from core.resources import resource_path

# Colores Premium (Estilo MataData/Stegano)
COLOR_PRIMARY = "#023047"
COLOR_ACCENT = "#A1D6E2"
COLOR_TEXT_PRIMARY = "#FFFFFF"
COLOR_TEXT_SECONDARY = "#023047"
COLOR_GOLD = "#FFD700"
COLOR_DROP_BG = "#011E23"
COLOR_DROP_HOVER = "#15262D"

# Tipografías Élite (Sustituyendo Comic Sans por Segoe UI Profesional)
FONT_TITLE = ("Segoe UI", 20, "bold")
FONT_BODY = ("Segoe UI", 12, "bold")
FONT_BUTTON = ("Segoe UI", 11, "bold")
FONT_DIALOG = ("Segoe UI", 11, "bold")

# Identificadores de Assets (Nombres de archivo para ImageManager)
# El ImageManager se encarga de buscar la ruta completa usando core.resources
LOGO_ICO = resource_path(os.path.join("assets", "images", "icon.ico")) if 'os' in locals() else "assets/images/icon.ico"
# Nota: Para el icono de la ventana (root.iconbitmap), necesitamos la ruta física absoluta.
# Para las imágenes de la GUI (PIL), pasamos solo el nombre al ImageManager.

# Nombres de archivos para ImageManager.load()
TITULO_PNG = "titulo.png"
BOTON_PNG = "boton.png"
BOTON1_PNG = "boton1.png"
ROBOT_PNG = "robot.png"

# Re-importar os para la lógica del icono si es necesario
import os
LOGO_ICO = resource_path(os.path.join("assets", "images", "icon.ico"))
