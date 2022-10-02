# commande à taper en ligne de commande après la sauvegarde de ce fichier:
# python setup.py build
from cx_Freeze import setup, Executable
  
executables = [
        Executable(script = "main.py",icon = "logo.ico", base = "Win32GUI" )
]
# ne pas mettre "base = ..." si le programme n'est pas en mode graphique, comme c'est le cas pour chiffrement.py.
  
buildOptions = dict( 
        includes = ["pygame","random"],
        include_files = ["bg.png", "logo.ico", "logo.png","trebuc.ttf"]
)
  
setup(
    name = "Morpion",
    version = "1",
    description = "Morpion pygame",
    author = "@chvkib.mp3",
    options = dict(build_exe = buildOptions),
    executables = executables
)