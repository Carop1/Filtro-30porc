import menus.menu_principal as mp
import menus.SGPB as sp
import menus.gestor_peli as gp
import menus.gestor_actores as ga
import menus.gestor_form as gf
import menus.gestor_infor as gi
import menus.gestor_genero as gg
#import modulos.pelicula2 as pl2
Active = True
import os
if __name__ == '__main__':
    while(Active == True):
        mp.menuPrincipal()
        try:
            opcion = int(input("ingrese la opcion que desea escoger: "))
        except ValueError:
            print("Ingreso informacion incorrecta")
            
        if opcion == 1:
            sp.sistemaGPB()
            try:
                op1 = int(input("Ingrese la opcion que desea escoger: "))
            except ValueError:
                print("Ingreso informacion incorrecta")
            
        elif opcion == 2:
            gg.gestorGenero()
            
            try:
                op2 = int(input("ingrese la opcion que desea escoger: "))
            except ValueError:
                print("Ingreso informacion incorrecta")
        elif opcion == 3:
            ga.gestorActores()
            
            try:
                op3 = int(input("ingrese la opcion que desea escoger: "))
            except ValueError:
                print("Ingreso informacion incorrecta")
        elif opcion == 4:
            gf.gestorFormatos()
            
            try:
                op4 = int(input("ingrese la opcion que desea escoger: "))
            except ValueError:
                print("Ingreso informacion incorrecta")
        elif opcion == 5:
            gp.gestorPeliculas()
            try:
                op5 = int(input("ingrese la opcion que desea escoger: "))
            except ValueError:
                print("Ingreso informacion incorrecta") 
                
                if op5 == 1:
                      pass
                
        elif opcion == 6:
            gi.gestorInformes()
            try:
                op6 = int(input("ingrese la opcion que desea escoger: "))
            except ValueError:
                print("Ingreso informacion incorrecta")
        elif opcion == 7:
            Active = False

            