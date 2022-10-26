# commande à taper en ligne de commande après la sauvegarde de ce fichier:
# python setup.py build

from cx_Freeze import setup, Executable
  
executables = [
        Executable(script = "main.py",icon = "logo.ico", base = "Win32GUI" )
]
  
buildOptions = dict( 
        includes = ["pygame","random"],
        include_files = ["bg.png", "logo.ico", "logo.png","trebuc.ttf"]
)
  
setup(
    name = "Morpion",
    version = "1",
    description = "Morpion pygame",
    author = "@444chak",
    options = dict(build_exe = buildOptions),
    executables = executables
)