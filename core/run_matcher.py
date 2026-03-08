import logging
import re

class RunMatcher:
    """ 
    Especialista en mapeo y manipulación quirúrgica de Runs en DOCX. 
    Normaliza el texto para asegurar coincidencias con espacios de Word (\xa0).
    """

    def __init__(self, paragraph, pattern):
        self.paragraph = paragraph
        self.pattern = pattern
        self.full_text = ""
        self.run_map = []
        self._build_map()

    def _build_map(self):
        """ Construye el mapa de texto normalizando espacios de Word. """
        self.full_text = ""
        self.run_map = []
        pos = 0
        
        for run in self.paragraph.runs:
            # IMPORTANTE: Reemplazamos \xa0 por espacio normal para que la regex matchee
            # pero mantenemos el objeto run original para aplicar el formato.
            text = run.text if run.text else ""
            normalized_text = text.replace('\xa0', ' ')
            length = len(normalized_text)
            
            if length == 0: continue
            
            self.run_map.append({
                "run": run,
                "start": pos,
                "end": pos + length,
                "original_text": text # Guardamos el original por si acaso
            })
            self.full_text += normalized_text
            pos += length

    def find_and_format(self):
        """ Busca coincidencias sobre el texto normalizado y aplica formato. """
        if not self.full_text:
            return 0
            
        matches = list(self.pattern.finditer(self.full_text))
        if not matches:
            return 0

        replacements = 0
        for match in reversed(matches):
            start, end = match.span()
            self._apply_surgical_format(start, end)
            replacements += 1
            
        return replacements

    def _apply_surgical_format(self, start, end):
        """ Aplica formato dividiendo runs si es necesario. """
        affected_entries = []
        for entry in self.run_map:
            if entry["end"] <= start: continue
            if entry["start"] >= end: break
            affected_entries.append(entry)

        if not affected_entries: return

        # Split al inicio
        first_entry = affected_entries[0]
        if start > first_entry["start"]:
            split_point = start - first_entry["start"]
            new_run = self._split_run(first_entry["run"], split_point)
            first_entry["run"] = new_run
            first_entry["start"] = start

        # Split al final
        last_entry = affected_entries[-1]
        if end < last_entry["end"]:
            split_point = end - last_entry["start"]
            self._split_run(last_entry["run"], split_point)
            last_entry["end"] = end

        # Aplicar Formato
        for entry in affected_entries:
            run = entry["run"]
            run.bold = True
            run.underline = True

    def _split_run(self, run, split_point):
        """ Divide un run preservando el estilo. """
        text = run.text
        left_text = text[:split_point]
        right_text = text[split_point:]
        
        run.text = left_text
        new_run = self.paragraph.add_run(right_text)
        self._copy_run_style(run, new_run)
        
        # Insertar en la posición correcta del XML
        run._r.addnext(new_run._r)
        return new_run

    def _copy_run_style(self, source, target):
        """ Copia propiedades visuales críticas de forma segura. """
        try:
            target.bold = source.bold
            target.italic = source.italic
            target.underline = source.underline
            if source.font.name: target.font.name = source.font.name
            if source.font.size: target.font.size = source.font.size
            if source.font.color and source.font.color.rgb:
                target.font.color.rgb = source.font.color.rgb
            if source.font.highlight_color:
                target.font.highlight_color = source.font.highlight_color
        except Exception:
            # Si falla la copia de un estilo específico (ej. temas de Office), continuamos.
            pass
