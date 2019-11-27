#updated

from dba import Database, Usuario
import os

usuarioglobal=None
db=Database()
os.system('cls')

def menu_usuario(usuario):
    # print(usuario.get_email())#esto es una prueba para mostrar email
    # os.system('cls')
    # print:("\nMenu:\n")
    
    opcion=input("\nMenu:\n=====\n 1. Ver todos los Post\n 2. Agregar un nuevo Post\n 3. Borrar Post (propio)\n 4. Ver Amigos (actuales)\n 5. Agregar Amigo\n 6. Eliminar Amigo\n 7. Cerrar Sesión\n ")
    os.system('cls')  
    #revisar (abajo está el código original)
    if opcion=="1":
        categorias=db.mostrar_categoria()
        for i in categorias:
            print(f"{i[0]}. {i[1]}")  
        cat=int(input("Indique categoría: "))
        posteos_cat=db.list_posteo_categoria(cat)
        if cat==1 or cat==2 or cat==3 or cat==4 or cat==5:
            print(f"\nEstos son los posts en la categoría {cat}:\n")
            for i in posteos_cat:
                print(i[0])
            input("\nPresione Enter para continuar...")
        else:
            print("\nCategoria incorrecta. Las opciones son entre 1 y 5")
            menu_usuario(usuario)
        menu_usuario(usuario)

    # if opcion=="1":
    #     categorias=db.mostrar_categoria()
    #     for i in categorias:
    #         print(f"{i[0]}. {i[1]}")  
    #     cat=input("Indique categoría: ")
    #     posteos_cat=db.list_posteo_categoria(cat)
    #     print(f"\nEstos son los posts en la categoría {cat}:\n")
    #     for i in posteos_cat:
    #         print(i[0])
    #     input("\nPresione Enter para continuar...")
    #     menu_usuario(usuario)

    elif opcion=="2":
        categorias=db.mostrar_categoria()
        for i in categorias:
            print(f"{i[0]}. {i[1]}")       
        cat=int(input("\nIndique categoría: "))
        if cat>=1 and cat<=5:
            id=db.consultar_id(usuario.get_email())
            post=input("\nIngrese posteo: ")
            db.add_posteo(post, id[0][0], cat)
            print("\nPosteo agregado!")
            input("\nPresione Enter para continuar...")
            menu_usuario(usuario)
        else:
            print("\nCategoria incorrecta. Las opciones son entre 1 y 5")
            menu_usuario(usuario)
        menu_usuario(usuario)

    elif opcion=="3":
        categorias=db.mostrar_categoria()
        for i in categorias:
            print(f"{i[0]}. {i[1]}") 
        cat=input("\nIndique de que categoría:")
        id=db.consultar_id(usuario.get_email())
        posteos=db.list_posteos_propios(cat, id[0][0])
        print(f"\nEstos son ID y tus Posts en la categoría: {cat}")
        for i in posteos:
            print(f"{i[0]}. {i[1]}")
        #hasta acá viene de DBA, trae categoria y idusuario
        borrar_post=input("\nIndique el ID de tu post a borrar: ")
        db.del_posteo(borrar_post, id[0][0])
        print(f"\nPost con ID número {borrar_post} fué eliminado")
        input("\nPresione Enter para continuar...")
        menu_usuario(usuario)

    elif opcion =="4":
        id=db.consultar_id(usuario.get_email())
        amigos=db.ver_amigos(id[0][0])
        if amigos==[]:
            print("No tenes amigos, looser!!")
        else:
            print("Este es el listado de tus amigos:")
        for i in amigos:
            mostrar=(db.mostrar_amigos(i[0]))
            print(mostrar[0][0], mostrar[0][1])
        input("\nPresione Enter para continuar...")
        menu_usuario(usuario)
    
    elif opcion=="5":
        amigo=input("Indica el email de tu amigo: ")
        if db.validar_amigo(amigo) == []:
        	print("Usuario no existe")
        else:
            db.agregar_amigo(usuario, amigo)
            print("Amigo agregado!! :)")
        menu_usuario(usuario)
      
    # elif opcion=="5":
    #     amigo=input("Indica el email de tu amigo: ")
    #     if db.validar_amigo(amigo) == []:
    #     	print("Usuario no existe")
    #     else:
    #         db.agregar_amigo(usuario, amigo)
    #         print("Amigo agregado!! :)")
    #     menu_usuario(usuario)
    
    elif opcion=="6":
        amigo=input("Indica el email de tu amigo: ")
        if db.validar_amigo(amigo) == []:
        	print("Usuario no existe")
        else:
            db.eliminar_amigo(usuario, amigo)
            print("ex-Amigo eliminado!! :(")
        menu_usuario(usuario)
    else:
        menu_login()

def menu_login():
    os.system('cls')
    print("Red Social Punk:")
    print("===============\n")
    print(" 1. Loguearse\n 2. Registrarse\n\n")
    valor=input("Ingrese una opción: ")
    db=Database()
    if valor=="1":
        os.system('cls')
        print("Ud está intentando loguearse, a la red Social Punk!\n")
        # print("Ingrese email con el que se registró:")
        u=input("Ingrese su email: ")
        c=input("Ingrese su Clave: ")
        usuarioglobal=db.login(u, c)
        # os.system('cls')
        if usuarioglobal:
            print(f"\nBienvenido {usuarioglobal[0][1]} {usuarioglobal[0][2]} a la red social Punk!!\n\n----------------------------\nElige una de estas opciones:\n")
            usuario=Usuario(usuarioglobal[0][1], usuarioglobal[0][2], usuarioglobal[0][3], usuarioglobal[0][4], usuarioglobal[0][5], usuarioglobal[0][6], usuarioglobal[0][7], usuarioglobal[0][8])
            # input("Presiona Enter para continuar...")
            menu_usuario(usuario)
        else:
            print("El usuario no existe, ingrese un email y clave válido")
            input("\nPresione Enter para continuar...")
            menu_login()
                        # for i in range(3):
            #     print("no existe, te quedan 2 intentos")
            # menu_login
            #pendiente un contador de máximo 3 intentos
                    
    elif valor=="2":
        print("\nIngrese los siguientes datos:")
        print("============================")
        e=input("E-mail: ")
        if db.validar_email(e) ==[]:
            a=input("Nombre: ")
            b=input("Apellido: ")
            d=input("Clave: ")
            f=input("Ciudad (es un numero): ")
            g=input("Edad: ")
            h=input("Sexo: (M-F) ")
            i=input("Fecha Nacimiento AAAA-MM-DD: ")
            #validar hacindo funcion validar mail y mandamos e
            usuario=Usuario(a,b,d,e,f,g,h,i)
            # if (aca deberiamos hacer la validacion)
            db.crear_usuario(usuario)
            print("Usuario registrado on éxito\ahora vuelve a loguearte por favor\n")
            input("\nPresiona Enter para continuar...")
            #validar si el usuario ya existe (faltante)
            menu_login()
        else:
            print("El usuario ya existe")
            #pendiente un contador de máximo 3 intentos
            input("\nPresione Enter para continuar...")
            menu_login()

    else:
        print("no existe ese valor")
        menu_login()      
   
if __name__ == "__main__":
    menu_login()
