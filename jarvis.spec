# -*- mode: python ; coding: utf-8 -*-
import sys
from os.path import join

block_cipher = None

# Add data files that need to be included
added_data = [
    ('Requirements.txt', '.'),
    ('version.json', '.'),
    ('privacy_config.json', '.'),
    ('client_secrets.json', '.'),
    ('haarcascade_frontalface_default.xml', '.'),
    ('nlu_training_data.json', '.'),
    ('gesture_config.json', '.'),
    ('Backend', 'Backend'),
    ('Frontend', 'Frontend'),
    ('Data', 'Data'),
    ('secure_keys', 'secure_keys'),
    ('cleanup_scripts', 'cleanup_scripts'),
]

# Add any special handling for data files here
# Example: ('path/to/local/file', 'relative/path/in/dist')

a = Analysis(
    ['install_dependencies.py'],
    pathex=[],
    binaries=[],
    datas=added_data,
    hiddenimports=[
        'pywhatkit', 'bs4', 'PIL', 'rich', 'requests', 'keyboard', 
        'cohere', 'selenium', 'mtranslate', 'pygame', 'PyQt5',
        'instagrapi', 'pyttsx3', 'cv2', 'face_recognition', 'numpy', 
        'yfinance', 'SpeechRecognition', 'pyaudio', 'twilio', 'pytube',
        'tensorflow', 'pandas', 'scikit-learn', 'tensorflow_hub',
        'tensorflow_text', 'matplotlib', 'scipy', 'h5py', 'psutil',
        'dotenv'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
    optimize=0,
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
    icon='Frontend/icon.ico' if 'Frontend/icon.ico' in [f[0] for f in a.datas] else None,
) 