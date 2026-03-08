import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES
import os

from config.settings import (
    COLOR_PRIMARY, COLOR_TEXT_PRIMARY, COLOR_ACCENT,
    COLOR_DROP_BG, COLOR_DROP_HOVER, FONT_BODY,
    TITULO_PNG, BOTON_PNG
)
from core.image_manager import ImageManager
from core.docx_formatter import DocxFormatter
from core.i18n import _
import threading
from .widgets import create_image_button
from .dialogs import AboutDialog, show_custom_message, center_window

class WordFormatterApp:
    """ Interfaz de Usuario de Nivel Élite para Word Formatter Pro con i18n. """

    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        
        self.root.title(_("app.title"))
        self.root.geometry("550x500")
        self.root.resizable(False, False)
        self.root.config(bg=COLOR_PRIMARY)
        
        # Inicializar gestores
        self.image_manager = ImageManager(root)
        self.formatter = DocxFormatter()
        
        # Variables y Estado
        self.file_path_var = tk.StringVar()
        self.words_var = tk.StringVar()
        self._is_processing = False
        
        # Lista de widgets que deben bloquearse durante el proceso
        self._action_widgets = []
        
        self._setup_ui()
        
        # Vincular teclas de acceso rápido
        self.root.bind("<Delete>", self._on_delete_pressed)
        self.root.bind("<Return>", self._on_enter_pressed)
        
        center_window(self.root, 550, 500)
        self.root.deiconify()

    def _on_enter_pressed(self, event):
        """ Dispara el proceso al pulsar Enter. """
        if not self._is_processing:
            self._start_process()

    def _on_delete_pressed(self, event):
        if self._is_processing: return
        self.file_entry.config(state="normal")
        self.file_path_var.set("")
        self.file_entry.config(state="readonly")
        self.words_var.set("")

    def _set_ui_state(self, locked=True):
        """ Bloquea o desbloquea la interfaz de forma lógica sin alterar la estética de los botones. """
        self._is_processing = locked
        cursor = "wait" if locked else ""
        
        # Cambiar cursor de la ventana y de todos los widgets interactivos
        self.root.config(cursor=cursor)
        for widget in self._action_widgets:
            widget.config(cursor="wait" if locked else "hand2")
            
        # El entry de palabras se bloquea visualmente porque es texto, pero los botones no
        self.word_entry.config(state="disabled" if locked else "normal")

    def _setup_ui(self):
        """ Construcción de la UI internacionalizada con registro de widgets de acción. """
        
        # 1. Título
        titulo_photo = self.image_manager.load(
            TITULO_PNG, 
            size=(380, 92), 
            add_shadow_effect=True,
            add_relief_effect=True,
            relief_intensity=2,
            shadow_offset=(4, 4),
            shadow_color=(0, 0, 0, 150)
        )
        if titulo_photo:
            self.title_label = tk.Label(
                self.root, image=titulo_photo, bg=COLOR_PRIMARY, cursor="hand2"
            )
            self.title_label.image = titulo_photo
            self.title_label.pack(pady=(25, 10))
            self.title_label.bind("<Button-1>", self._show_about)

        # 2. Área de Entrada
        main_frame = tk.Frame(self.root, bg=COLOR_PRIMARY)
        main_frame.pack(fill="both", expand=True, padx=40)

        BG_ENTRY = "#EAF6F8"
        FG_ENTRY = "#023047"

        # Documento Word
        tk.Label(main_frame, text=_("label.document"), bg=COLOR_PRIMARY, fg=COLOR_TEXT_PRIMARY, font=FONT_BODY).pack(anchor="w")
        
        self.drop_frame = tk.Frame(main_frame, bg=BG_ENTRY, height=45, bd=1, relief="flat")
        self.drop_frame.pack(fill="x", pady=(5, 10))
        self.drop_frame.pack_propagate(False)

        self.file_entry = tk.Entry(
            self.drop_frame, textvariable=self.file_path_var,
            font=("Segoe UI", 11, "bold"), bg=BG_ENTRY, fg=FG_ENTRY,
            insertbackground=FG_ENTRY, borderwidth=0, highlightthickness=0,
            state="readonly"
        )
        self.file_entry.pack(fill="both", expand=True, padx=10)
        
        self.file_entry.drop_target_register(DND_FILES)
        self.file_entry.dnd_bind('<<Drop>>', self._handle_drop)

        # Botón Examinar
        self.btn_browse = create_image_button(
            main_frame, _("button.browse"), self._browse_file, self.image_manager, 
            BOTON_PNG, (130, 35)
        )
        self.btn_browse.pack(pady=(0, 15))
        self._action_widgets.append(self.btn_browse)

        # Palabras
        tk.Label(main_frame, text=_("label.words"), bg=COLOR_PRIMARY, fg=COLOR_TEXT_PRIMARY, font=FONT_BODY).pack(anchor="w")
        
        word_entry_frame = tk.Frame(main_frame, bg=BG_ENTRY, height=45)
        word_entry_frame.pack(fill="x", pady=(5, 20))
        word_entry_frame.pack_propagate(False)

        self.word_entry = tk.Entry(
            word_entry_frame, textvariable=self.words_var,
            font=("Segoe UI", 11, "bold"), bg=BG_ENTRY, fg=FG_ENTRY,
            insertbackground=FG_ENTRY, borderwidth=0, highlightthickness=0
        )
        self.word_entry.pack(fill="both", expand=True, padx=10)

        # 3. Botones Finales
        actions_frame = tk.Frame(self.root, bg=COLOR_PRIMARY)
        actions_frame.pack(pady=(0, 25))

        self.btn_process = create_image_button(
            actions_frame, _("button.process"), self._start_process, self.image_manager, 
            BOTON_PNG, (150, 45)
        )
        self.btn_process.pack(side="left", padx=10)
        self._action_widgets.append(self.btn_process)

        self.btn_exit = create_image_button(
            actions_frame, _("button.exit"), self.root.quit, self.image_manager, 
            BOTON_PNG, (150, 45)
        )
        self.btn_exit.pack(side="left", padx=10)
        self._action_widgets.append(self.btn_exit)

    def _show_about(self, event=None):
        if self._is_processing: return
        AboutDialog(self.root, self.image_manager)

    def _handle_drop(self, event):
        if self._is_processing: return
        # Robustez para rutas con espacios y múltiples archivos (tomamos el primero)
        files = self.root.tk.splitlist(event.data)
        if not files: return
        
        data = files[0]
        if data.lower().endswith('.docx'):
            self.file_entry.config(state="normal")
            self.file_path_var.set(data)
            self.file_entry.config(state="readonly")
            # Efecto visual: pequeño destello de éxito en el frame
            self._flash_success()
        else:
            show_custom_message(self.root, "title.error", "error.docx_only", self.image_manager)

    def _flash_success(self):
        """ Efecto visual de 'archivo aceptado'. """
        original_bg = self.drop_frame.cget("bg")
        self.drop_frame.config(bg=COLOR_ACCENT)
        self.root.after(150, lambda: self.drop_frame.config(bg=original_bg))

    def _browse_file(self):
        if self._is_processing: return
        path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
        if path:
            self.file_entry.config(state="normal")
            self.file_path_var.set(path)
            self.file_entry.config(state="readonly")

    def _start_process(self):
        """ Inicia el procesamiento con validaciones robustas de nivel profesional. """
        if self._is_processing: return
        
        path = self.file_path_var.get()
        words = self.words_var.get()
        
        # 1. Validación de campos vacíos
        if not path or not words:
            show_custom_message(self.root, "title.warning", "error.path_words", self.image_manager)
            return
            
        # 2. Validación de existencia física (por si se movió/borró el archivo)
        if not os.path.exists(path):
            show_custom_message(self.root, "title.error", "error.file_not_found", self.image_manager)
            return

        # Bloquear UI de forma centralizada
        self._set_ui_state(locked=True)

        threading.Thread(target=self._run_async_process, args=(path, words), daemon=True).start()

    def _run_async_process(self, path, words):
        """ Lógica de procesamiento en segundo plano con captura de errores de nivel forense. """
        try:
            output = self.formatter.process(path, words)
            # Volver al hilo principal para éxito
            self.root.after(0, lambda: self._on_process_complete(output))
        except PermissionError:
            self.root.after(0, lambda: self._on_process_error("error.word_open"))
        except FileNotFoundError:
            self.root.after(0, lambda: self._on_process_error("error.file_not_found"))
        except Exception as e:
            import logging
            logging.error(f"Error en el procesamiento: {e}", exc_info=True)
            self.root.after(0, lambda: self._on_process_error("error.unexpected", error=str(e)))

    def _on_process_complete(self, output_path):
        """ Desbloqueo y notificación de éxito. """
        self._set_ui_state(locked=False)
        show_custom_message(
            self.root, "title.success", "success.processed", 
            self.image_manager, open_folder=output_path, filename=os.path.basename(output_path)
        )

    def _on_process_error(self, key, **kwargs):
        """ Desbloqueo y notificación de error. """
        self._set_ui_state(locked=False)
        show_custom_message(self.root, "title.error", key, self.image_manager, **kwargs)

