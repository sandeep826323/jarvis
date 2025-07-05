# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Add essential data files
added_data = [
    ('Requirements.txt', '.'),
    ('version.json', '.'),
    ('privacy_config.json', '.'),
    ('client_secrets.json', '.'),
    ('haarcascade_frontalface_default.xml', '.'),
]

a = Analysis(
    ['install_dependencies.py'],
    pathex=[],
    binaries=[],
    datas=added_data,
    hiddenimports=[
        'pywhatkit', 'bs4', 'PIL', 'rich', 'requests', 'keyboard', 
        'pygame', 'PyQt5', 'cv2', 'numpy', 'psutil', 'dotenv'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Jarvis',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
) 