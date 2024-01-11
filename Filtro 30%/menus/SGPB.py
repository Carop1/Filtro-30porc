import menus.gestor_infor as gi
import menus.gestor_peli as gp

def sistemaGPB():
    menu2 = ["1. Administrados de generos","2. Admnistrador de actores", "3. Administrador de formatos" , "4. Gestor de informes", "5. Gestor de peliculas", "6. Salir"]
    etiqueta2 = """
    ++++++++++++++++++++++++++++++++++++++++++++
    + SISTEMA GESTOR DE PELICULAS BLOCKBUSTER  +
    ++++++++++++++++++++++++++++++++++++++++++++
    """
    print(etiqueta2)
    for i in range(len(menu2)):
        print(menu2[i])
    #seleccion = int(input("Ingrese el numero de la opcion que desee: "))
    
        