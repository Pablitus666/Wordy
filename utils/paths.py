import os
import sys
import ctypes

def get_resource_path(relative_path):
    """ Obtiene la ruta absoluta para recursos, compatible con PyInstaller y desarrollo. """
    try:
        # PyInstaller crea una carpeta temporal y almacena la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def setup_dpi_awareness():
    """ Configura la aplicación para que sea nítida en pantallas de alta resolución (DPI). """
    if sys.platform == "win32":
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            try:
                ctypes.windll.user32.SetProcessDPIAware()
            except Exception:
                pass
