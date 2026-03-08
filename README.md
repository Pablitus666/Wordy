# 📝 Wordy (Windows) — Advanced Word Formatting & Surgical Search Tool

Herramienta Profesional de **Búsqueda Quirúrgica y Formateo Inteligente en Documentos Word**

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows)
![Architecture](https://img.shields.io/badge/Architecture-MVC-informational)
![Format](https://img.shields.io/badge/Format-DOCX-blue?logo=microsoftword)
![Engine](https://img.shields.io/badge/Engine-RunMatcher%20XML-red)
![Build](https://img.shields.io/badge/Build-PyInstaller-orange)
![Code Signing](https://img.shields.io/badge/Code%20Signing-Digitally%20Signed-blue)
![Security](https://img.shields.io/badge/Security-Digitally%20Signed-blue)

---

**Wordy** es una aplicación de escritorio desarrollada en **Python 3.11+** diseñada para automatizar el formateo de palabras clave dentro de documentos **Word (.docx)**.

A diferencia de la búsqueda tradicional de Word, **Wordy analiza directamente la estructura XML interna del documento**, permitiendo detectar palabras incluso cuando están **fragmentadas por el formato interno (runs)**.

Esto permite aplicar cambios de formato **sin romper estilos, tablas, imágenes o estructura del documento**.


La aplicación está orientada a:

* Redactores y editores de contenido
* Profesionales jurídicos y administrativos
* Estudiantes y académicos
* Usuarios que buscan consistencia visual en documentos extensos

---
## ⚡ Resumen Rápido

| Característica | Descripción |
|-------|-------------|
| Procesamiento DOCX | Edición segura sin alterar la estructura del documento. |
| Motor RunMatcher | Detecta palabras fragmentadas entre elementos `<w:r>`. |
| Inteligencia Lingüística | Búsqueda tolerante a mayúsculas, acentos y plurales. |
| Multilingüe | Soporte para 9 idiomas con detección automática. |
| Drag & Drop | Carga de documentos instantánea al arrastrar. |
| Interfaz High-DPI | UI optimizada para monitores 4K y escalado dinámico. |
| Firma Digital | Ejecutables firmados por Walter Pablo Téllez Ayala. |

--- 

## ✨ Características Destacadas

*   🔍 **Motor RunMatcher:** Detecta palabras incluso cuando están **divididas por el formato interno de Word** (negritas parciales, cambios de fuente o espacios internos). Wordy las identifica correctamente sin romper la integridad del documento.
*   🧠 **Inteligencia Lingüística:** Búsqueda insensible a mayúsculas, acentos, género, plurales y caracteres especiales como espacios de no ruptura (`\xa0`).
*   🌍 **Soporte Multilingüe (9 Idiomas):** ES, EN, FR, DE, IT, PT, RU, JA, ZH con detección automática del sistema.
*   🖱️ **Drag & Drop Nativo:** Sistema intuitivo de arrastrar y soltar archivos para carga instantánea.
*   🖥️ **Soporte High-DPI (4K Ready):** Interfaz nítida con iconos multi-resolución (16px a 256px) y escalado dinámico para pantallas modernas.  
*   🛡️ **Firma Digital Verificada:** Todo el software está firmado digitalmente (SHA256) por **Walter Pablo Téllez Ayala**. Esto garantiza:
    *   **Integridad:** Garantía de que el software no ha sido alterado.
    *   **Autenticidad:** Identidad del desarrollador verificada.
    *   **Seguridad:** Protección total contra modificaciones malintencionadas.

---

![Wordy Preview](https://raw.githubusercontent.com/Pablitus666/Wordy/main/images2/Preview.png)

---

## 🏗️ Ingeniería y Arquitectura

Wordy sigue un patrón estructurado **MVC (Modelo-Vista-Controlador)** que garantiza estabilidad y un rendimiento óptimo.

🔹 **Capa de Negocio (Core)**
    * **RunMatcher:** Cirugía XML para detectar palabras fragmentadas entre elementos `<w:r>`.
    * **DocxFormatter:** Orquestador de cambios que preserva estilos, imágenes y tablas.
    * **i18n Engine:** Gestión dinámica de traducciones en tiempo de ejecución.

🔹 **Capa de Interfaz (UI)**
    * Interfaz nativa optimizada para Windows.
    * Bloqueo lógico de UI durante procesos con cursor de espera interactivo.
    * Sistema de notificaciones personalizadas con soporte para abrir carpetas de salida.

🔹 **Gestión de Recursos**
    * **ImageManager:** Caché de imágenes con escalado dinámico para evitar pixelado.
    * **Fonts Engine:** Carga profesional de tipografías mediante la API de Windows.

---

## 📂 Estructura del Proyecto

```text
Wordy/
├── assets/             # Recursos estáticos
│   ├── images/         # Imágenes UI (PNG/ICO)
│   └── locales/        # Archivos de traducción (JSON)
├── config/             # Configuración global
├── core/               # Motor lógico (XML/DOCX)
├── gui/                # Componentes de la interfaz
├── logs/               # Registro de eventos
├── tkinterdnd2/        # Soporte Drag & Drop
├── utils/              # Utilidades de sistema
├── main.py             # Punto de entrada
└── requirements.txt    # Dependencias
```
---

## 📷 Capturas de Pantalla

<p align="center">
  <img src="images2/screenshot.png" alt="Wordy Interface" width="600"/>
</p>

---

## 🧰 Tecnologías Utilizadas

- Python 3.11+
- python-docx
- Tkinter
- TkinterDnD
- PyInstaller
- ImageMagick (pipeline de iconos)

---

## 📋 Requisitos

- Windows 10 / 11
- Documentos `.docx`
- 4 GB RAM recomendados

---

## 🚀 Guía de Instalación y Uso

Wordy se distribuye en formatos profesionales diseñados para máxima comodidad:

### 1. Versión Portable (Sin Instalación) 🏃
Ideal para uso rápido desde cualquier carpeta o unidad USB.
1.  Ve a la sección [**Releases**](https://github.com/Pablitus666/Wordy/releases).
2.  Descarga el archivo `Wordy_Portable_Final.exe`.
3.  **Ejecución:** Haz doble clic. Al ser un ejecutable único, cargará los recursos necesarios en memoria de forma segura.

### 2. Versión en Carpeta (Arranque Instantáneo) 🖥️
Recomendada para uso frecuente en estaciones de trabajo.
1.  Descarga el paquete `Wordy_Final_Folder.zip` desde [**Releases**](https://github.com/Pablitus666/Wordy/releases).
2.  Extrae el contenido y ejecuta `Wordy_Final.exe`.
3.  **Ventaja:** Mayor velocidad de carga al no requerir descompresión temporal.

### 3. Compilar a ejecutable (Windows)
```bash
# Wordy puede compilarse a un .exe usando PyInstaller.
pip install pyinstaller

Compilar:
pyinstaller --noconfirm --onefile --windowed --icon=assets/icon.ico main.py

El ejecutable aparecerá en:
dist/Wordy.exe
```
### 4. Instalación para desarrollo
```bash
# Clonar el repositorio
git clone https://github.com/Pablitus666/Wordy.git
cd Wordy

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python main.py
```

---

## 🧭 Evolución: Versión Legacy

Wordy representa la evolución profesional de un script experimental previo. La versión Legacy permanece disponible con fines educativos.
👉 [**Wordi — Legacy Edition**](https://github.com/Pablitus666/Wordi---Legacy.git)

--- 

## 👨‍💻 Autor

**Walter Pablo Téllez Ayala**  
Software Developer  
📍 Bolivia 🇧🇴 <img src="https://flagcdn.com/w20/bo.png" width="20"/> <br>
📧 [pharmakoz@gmail.com](mailto:pharmakoz@gmail.com) 

© 2026 — Wordy Professional Tool

---

⭐ Si este proyecto te es útil, considera dejar una estrella en el repositorio oficial: [**Wordy Repo**](https://github.com/Pablitus666/Wordy.git)
