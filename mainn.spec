# -*- mode: python -*-

block_cipher = None

excludesPassedToAnalysis = []



excludeEncodings = []

a = Analysis(['main.py'],
             pathex=['C:\\PROGRAMAS PYTHON\\SANEPY\\Projetos\SANEPY'],
             binaries=[],
             datas=[('DLLs/glut.h', '.'),('DLLs/glut32.def', '.'),
                    ('DLLs/glut32.def', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=excludesPassedToAnalysis+excludeEncodings,
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)


for d in a.datas:
    if "pyconfig" in d[0]:
        a.datas.remove(d)
        break

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)


a.datas += []

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,        
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=True)
