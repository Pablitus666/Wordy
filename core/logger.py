import os
import sys
import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    """ 
    Configura un Logger profesional con rotación y rutas inteligentes.
    Redirige a %LOCALAPPDATA% si la aplicación está congelada (PyInstaller).
    """
    app_name = "Wordi"
    
    # Determinar ruta de logs
    if getattr(sys, 'frozen', False):
        # Entorno de Producción (Ejecutable)
        base_dir = os.path.join(os.environ.get('LOCALAPPDATA', os.path.expanduser('~')), app_name)
    else:
        # Entorno de Desarrollo
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    log_dir = os.path.join(base_dir, "logs")
    
    try:
        os.makedirs(log_dir, exist_ok=True)
    except Exception:
        # Fallback a carpeta temporal si no hay permisos
        log_dir = os.path.join(os.environ.get('TEMP', '.'), app_name, "logs")
        os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "app.log")

    # Configuración de Formato y Rotación (5MB por archivo, máximo 3 archivos)
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    handler = RotatingFileHandler(
        log_file, maxBytes=5*1024*1024, backupCount=3, encoding='utf-8'
    )
    handler.setFormatter(formatter)

    # Logger Raíz
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    # También log a consola en desarrollo
    if not getattr(sys, 'frozen', False):
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    logging.getLogger("Wordi.Logger").info(f"Sistema de Logs iniciado en: {log_file}")
    return logger
