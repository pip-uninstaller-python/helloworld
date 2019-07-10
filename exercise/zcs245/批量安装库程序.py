import os
libs ={"matplotlib","pillow","sklearn","requests","beautifulsoup4","wheel","networkx","sympy","pyinstaller","django","flask","werobot","PyQt5","pandas","pyopengl","pypdf2","docopt","pygame"}
try:
    for lib in libs:
        os.system("pip install "+lib)
    print("Succeesful")
except:
    print("Falied Somehow")