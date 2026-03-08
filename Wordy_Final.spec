# -*- mode: python ; coding: utf-8 -*-
import sys
import os

# --- CONFIGURACIÓN DE RUTAS ---
BLOCK_CIPHER = None
PROJECT_DIR = os.path.abspath(os.getcwd())
ASSETS_DIR = os.path.join(PROJECT_DIR, 'assets')
ICON_PATH = os.path.join(ASSETS_DIR, 'images', 'icon.ico')

# --- ANÁLISIS DE DEPENDENCIAS ---
a = Analysis(
    ['main.py'],
    pathex=[PROJECT_DIR],
    binaries=[],
    datas=[
        ('assets', 'assets'),
        ('tkinterdnd2', 'tkinterdnd2'),
        ('config', 'config'),
        ('core', 'core'),
        ('gui', 'gui'),
        ('utils', 'utils'),
    ],
    hiddenimports=[
        'tkinterdnd2',
        'PIL.Image',
        'PIL.ImageTk',
        'docx',
        'lxml',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib', 'numpy', 'pandas', 'scipy', 'PyQt5', 'PySide2'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=BLOCK_CIPHER,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=BLOCK_CIPHER)

# --- EJECUTABLE PORTABLE (ONEFILE) ---
exe_portable = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Wordy_Portable_Final',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=ICON_PATH,
)

# --- EJECUTABLE CON CARPETA (ONEDIR) ---
exe_folder = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Wordy_Final',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=ICON_PATH,
)

coll = COLLECT(
    exe_folder,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='Wordy_Final_Folder',
)
