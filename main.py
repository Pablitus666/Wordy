import logging
import sys

# Configuración básica inicial para asegurar registro de errores pre-arranque
logging.basicConfig(level=logging.ERROR)

def main():
    """ Punto de entrada principal con refinamiento Élite Final. """

    # 1. Lazy imports para acelerar el tiempo de respuesta inicial
    from tkinterdnd2 import TkinterDnD
    from gui.app_window import WordFormatterApp
    from utils.paths import setup_dpi_awareness
    from config.settings import LOGO_ICO
    from core.logger import setup_logger

    # 2. Inicializar Logs Profesionales
    setup_logger()
    log = logging.getLogger(__name__)
    log.info("Iniciando Wordi - Versión Élite Final")

    # 3. DPI Awareness (Nitidez absoluta)
    setup_dpi_awareness()

    # 4. Inicializar raíz con soporte Drag & Drop
    root = TkinterDnD.Tk()
    root.withdraw()
    root.update_idletasks() # Forzar cálculo de layout para evitar micro-parpadeos

    # 5. Configuración de icono robusta y portátil
    try:
        if LOGO_ICO:
            root.iconbitmap(LOGO_ICO)
    except Exception:
        try:
            # Fallback para otros sistemas o si iconbitmap falla
            import tkinter as tk
            root.iconphoto(True, tk.PhotoImage(file=LOGO_ICO))
        except Exception as e:
            log.warning(f"No se pudo establecer el icono: {e}")

    # 6. Lanzar la aplicación principal
    app = WordFormatterApp(root)

    # 7. Protocolo de cierre limpio
    root.protocol("WM_DELETE_WINDOW", root.quit)

    # 8. Bucle principal
    root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import tkinter as tk
        from tkinter import messagebox
        import os
        
        logging.exception("Error fatal durante el arranque de la aplicación")
        
        # Crear una raíz temporal de emergencia
        error_root = tk.Tk()
        error_root.withdraw()
        
        # Intentar obtener la ruta de logs de forma amigable para el usuario
        log_dir = os.path.expandvars(r"%LOCALAPPDATA%\Wordi\logs")
        if not os.path.exists(log_dir):
            log_dir = "el directorio de instalación"

        messagebox.showerror(
            "Error Crítico - Wordi",
            f"La aplicación no pudo iniciarse debido a un problema técnico:\n\n{str(e)}\n\n"
            f"Por favor, revise los logs en:\n{log_dir}"
        )
        
        # Limpieza explícita
        error_root.destroy()
        sys.exit(1)
