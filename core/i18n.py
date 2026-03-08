import json
import locale
import os
import logging
from core.resources import resource_path

# Configuración de Logging para i18n
log = logging.getLogger("WordFormatterPro.i18n")

class Translator:
    """ Motor de internacionalización profesional con soporte para 9 idiomas. """
    
    def __init__(self):
        self.translations = {}
        self.current_lang = "en"
        self._load_translations()

    def _get_system_language(self):
        """ Detecta el idioma del sistema operativo. """
        try:
            lang_code, _ = locale.getdefaultlocale()
            if lang_code:
                return lang_code.split('_')[0].lower()
        except Exception as e:
            log.error(f"Error detectando idioma: {e}")
        return "en"

    def _load_translations(self):
        """ Carga el archivo JSON correspondiente al idioma detectado. """
        self.current_lang = self._get_system_language()
        
        # Lista de idiomas soportados
        supported = ["es", "en", "de", "fr", "it", "ja", "pt", "ru", "zh"]
        if self.current_lang not in supported:
            self.current_lang = "en"

        locale_path = resource_path(os.path.join("assets", "locales", f"{self.current_lang}.json"))
        
        # Fallback a inglés si el archivo no existe
        if not os.path.exists(locale_path):
            log.warning(f"No se encontró el archivo para {self.current_lang}, usando inglés.")
            locale_path = resource_path(os.path.join("assets", "locales", "en.json"))

        try:
            with open(locale_path, 'r', encoding='utf-8') as f:
                self.translations = json.load(f)
            log.info(f"Idioma cargado: {self.current_lang}")
        except Exception as e:
            log.error(f"Error cargando traducciones: {e}")
            self.translations = {}

    def translate(self, key, **kwargs):
        """ Obtiene la traducción para una clave dada. """
        text = self.translations.get(key, key)
        try:
            return text.format(**kwargs)
        except KeyError:
            return text

# Instancia global para uso simplificado
_translator = Translator()

def _(key, **kwargs):
    """ Función alias para traducciones rápidas. """
    return _translator.translate(key, **kwargs)
