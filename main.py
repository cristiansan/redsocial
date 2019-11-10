from dba import Database, Usuario
usuarioglobal=None
db=Database()

def menu_usuario(usuario):
    print(usuario.get_email())#esto es una prueba para mostrar email
    opcion=input("1.Agregar amigo 2.Postear 3.Borrar post")
    if opcion=="1":
        amigo=input("Indica el email de tu amigo: ")
        db.agregar_amigo(usuario, amigo)
    # elif opcion=="2":
    #     postear=input("Post: ")
    #     db.add_posteo(MENSAJE)
    # else opcion=="3":
    #     borrar_post=input("ID post a borrar: ")
    #     db.borrar_post(ID_POSTEO)

if __name__ == "__main__":
    print("Elije Opcion Deseada: ")
    valor=input("1.Loguearse 2.Registrarse 3.Borrar Usuario: ")
    db=Database()
    if valor=="1":
        u=input("Usuario: ")
        c=input("Clave: ")
        usuarioglobal=db.login(u, c)
        if usuarioglobal:
               print(f"Bienvenido {usuarioglobal[0][1]} {usuarioglobal[0][2]}, a la red social Punk!")
               usuario=Usuario(usuarioglobal[0][1], usuarioglobal[0][2], usuarioglobal[0][3], usuarioglobal[0][4], usuarioglobal[0][5], usuarioglobal[0][6], usuarioglobal[0][7], usuarioglobal[0][8])
               menu_usuario(usuario)
        #falta traer todos los datos del usuario
    
    elif valor=="2":
        # ii=input("id: ")
        a=input("Nombre: ")
        b=input("Apellido: ")
        d=input("Clave: ")
        e=input("eMail: ")
        f=input("Ciudad (es un numero): ")
        g=input("Edad: ")
        h=input("Sexo: (M-F) ")
        i=input("Fecha Nacimiento AAAA-MM-DD: ")
        usuario=Usuario(a,b,d,e,f,g,h,i)
        db.crear_usuario(usuario)
        
    
    elif valor=="3":
        e=input("Email a eliminar: ")
        db.del_usuario(e)

    else:
        print("no existe valor")
# pos=('hola')
# data=Database()
# data.add_posteo(pos)

