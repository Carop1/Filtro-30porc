
def menuPrincipal():
    menu = ["1. Sistema de gestor de peliculas Blockbuster","2. Gestor de generos", "3. Gestor de actores" , "4. Gestor de formatos", "5. Gestor de peliculas", "6. Gestor de informes"]
    etiqueta = """
    ++++++++++++++++++++++++++++++++++++
    +         MENU PRINCIPAL           +
    ++++++++++++++++++++++++++++++++++++
    """
    print(etiqueta)
    for i in range(len(menu)):
        print(menu[i])
    
