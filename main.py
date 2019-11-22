#updated

from dba import Database, Usuario
import os

usuarioglobal=None
db=Database()
os.system('cls')

def menu_usuario(usuario):
    # print(usuario.get_email())#esto es una prueba para mostrar email
    os.system('cls')
    opcion=input(" 1. Ver Post\n 2. Agregar un nuevo Post\n 3. Borrar Post\n 4. Ver Amigos\n 5. Agregar Amigo\n 6. Eliminar Amigo\n 7. Cerrar Sesión\n ")

    if opcion=="1":
        categorias=db.mostrar_categoria()
        for i in categorias:
            print(i)
        cat=input("Indique categoría: ")
        # id=db.consultar_id(usuario.get_email())
        # print(id[0][0])       #esto me trae el ID del usuario
        posteos_cat=db.list_posteo_categoria(cat)
        for i in posteos_cat:
            print(i[0])
            print()
        # post=input("Ingrese posteo: ")
        # db.add_posteo(post, id[0][0], cat) 
        input("Presione Enter para continuar...")
        menu_usuario(usuario)
    
    elif opcion=="2":
        categorias=db.mostrar_categoria()
        for i in categorias:
            print(i)
        cat=input("Indique categoría: ")
        id=db.consultar_id(usuario.get_email())
        print(id[0][0])
        post=input("Ingrese posteo: ")
        db.add_posteo(post, id[0][0], cat)
        print("Posteo agregado!")
        input("Presione Enter para continuar...")
        # os.system('cls')
        menu_usuario(usuario)

    elif opcion=="3":
        borrar_post=input("ID post a borrar: ")
        # print(ID_POSTEO)
        # db.del_posteo(ID_POSTEO)
        # print(borrar_post)
        db.del_posteo(borrar_post)
        print("Post Eliminado")
        menu_usuario(usuario)

    elif opcion =="4":
        id=db.consultar_id(usuario.get_email())
        amigos=db.ver_amigos(id[0][0])
        print("Tus amigos son:")
        for i in amigos:
            mostrar=(db.mostrar_amigos(i[0]))
            print(mostrar[0][0], mostrar[0][1])
        input("Presione Enter para continuar...")
        menu_usuario(usuario)

        
    elif opcion=="5":
        amigo=input("Indica el email de tu amigo: ")
        if db.validar_amigo(amigo) == []:
        	print("Usuario no existe")
        else:
            db.agregar_amigo(usuario, amigo)
         # falta poner mensaje si existe o no.
            menu_usuario(usuario)
    
    elif opcion==6:
        amigo=input("Indica el email de tu amigo: ")
        if db.validar_amigo(amigo) == []:
        	print("Usuario no existe")
        else:
            db.eliminar_amigo(usuario, amigo)
            menu_usuario(usuario)
    else:
        menu_login()

def menu_login():
    os.system('cls')
    print("Elije Opcion Deseada: ")
    valor=input("1.Loguearse\n2.Registrarse\n")
    db=Database()
    if valor=="1":
        u=input("Usuario: ")
        c=input("Clave: ")
        usuarioglobal=db.login(u, c)
        # os.system('cls')
        if usuarioglobal:
            print(f"Bienvenido {usuarioglobal[0][1]} {usuarioglobal[0][2]}\n\nEsta es la red social Punk!!\nElige una de estas opciones\n")
            usuario=Usuario(usuarioglobal[0][1], usuarioglobal[0][2], usuarioglobal[0][3], usuarioglobal[0][4], usuarioglobal[0][5], usuarioglobal[0][6], usuarioglobal[0][7], usuarioglobal[0][8])
            menu_usuario(usuario)
        else:
            print("El usuario no existe, ingrese un usuario válido")
            #pendiente un contador de máximo 3 intentos
            input("Presione Enter para continuar...")
            menu_login()
                    
    elif valor=="2":
        # ii=input("id: ")
        e=input("eMail: ")
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
            input("Presiona Enter para continuar...")
            #validar si el usuario ya existe (faltante)
            menu_login()
        else:
            print("El usuario ya existe")
            #pendiente un contador de máximo 3 intentos
            input("Presione Enter para continuar...")
            menu_login()

    else:
        print("no existe valor")       
   
if __name__ == "__main__":
    menu_login()
