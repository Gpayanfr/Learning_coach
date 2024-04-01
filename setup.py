from cx_Freeze import setup, Executable
import sys

base = "Win32GUI" if sys.platform == "win32" else None

executables = [Executable("Graphic_LC.py", base=base)]
fichiers = ['Images','Plans_de_travail','Banque_exercices']
packages = ["idna", "docx", "os", "csv", "tkinter", "Fonctions.Learning_coach"]

options = {
    'build_exe': {    
        'packages':packages,
        'include_files':fichiers,
    },
}
##Adaptez les valeurs des variables "name", "version", "description" à votre programme.
setup(
    name = "Learning_coach",
    options = options,
    version = "1.0",
    description = 'Voici mon programme',
    executables = executables
)