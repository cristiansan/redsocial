from dba import Database, Usuario


if __name__ == "__main__":
    print("Elije Opcion Deseada: ")
    valor=input("1.Loguearse 2.Registrarse 3.Borrar: ")
    db=Database()
    if valor=="1":
        u=input("Usuario: ")
        c=input("Clave: ")
        db.login(u, c)
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
        # email=Email(e)   
        db.del_usuario(e)

    else:
        print("no existe valor")
    # db.list_posteo_usuario(1)
    # db.list_posteos()
    
    # db.mod_posteo_usuario("nuevo posteo", 2)
    
    # print(usuario.get_nombre())
    # a1=Usuario("01", "jorge", "caseros", "4321", "jocaseros@gmail.com","3", "44","M","1980-09-09")
    # usuario.crear_usuario()
