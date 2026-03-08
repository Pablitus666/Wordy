import os
import sys

def get_base_path():
    """ Obtiene la ruta base del proyecto, compatible con PyInstaller y desarrollo. """
    if getattr(sys, 'frozen', False):
        # PyInstaller crea una carpeta temporal y almacena la ruta en _MEIPASS
        return sys._MEIPASS
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def resource_path(relative_path):
    """ Obtiene la ruta absoluta para un recurso. """
    return os.path.join(get_base_path(), relative_path)

def image_path(filename):
    """ Busca una imagen, priorizando la carpeta 'png_master'. """
    # Prioridad 1: assets/images/png_master/
    master_path = resource_path(os.path.join("assets", "images", "png_master", filename))
    if os.path.exists(master_path):
        return master_path
    
    # Prioridad 2: assets/images/
    standard_path = resource_path(os.path.join("assets", "images", filename))
    if os.path.exists(standard_path):
        return standard_path
    
    # Prioridad 3: images/ (retrocompatibilidad)
    legacy_path = resource_path(os.path.join("images", filename))
    if os.path.exists(legacy_path):
        return legacy_path
        
    return standard_path

def master_image_path(filename):
    """ Helper específico para png_master. """
    return resource_path(os.path.join("assets", "images", "png_master", filename))
