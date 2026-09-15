# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['F:\\jarvis'],
    binaries=[],
    datas=[
        ('Frontend/Graphics/*', 'Frontend/Graphics'),
        ('config/*.py', 'config'),
        ('Backend/Data/*.json', 'Backend/Data'),
        ('Data/speech/*', 'Data/speech')
    ],
    hiddenimports=[
        'numpy',
        'pydantic',
        'sklearn',
        'speech_recognition',
        'pywhatkit'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Jarvis',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='Frontend\\Graphics\\icon.ico'
)