#updated

dbconf = {
    'host':'localhost',
    'database':'red_social',
    'user':'root',
    'password':''
}

queries = {
    
    'list_table':'SELECT * FROM %s',#trae odos los campos de la tabla seleccionada
    'validar_email':'SELECT * FROM USUARIO WHERE EMAIL = %s',#valida usuario en base al email
    'add_usuario':'INSERT INTO usuario ( NOMBRE, APELLIDO, CLAVE, EMAIL, Ciudad, edad, sexo, fecha_nac) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',#agrega datos del usuario
    'del_usuario':'DELETE FROM usuario WHERE EMAIL = %s', #borra usuario en base al email que ingresemos
    'add_posteo':'INSERT INTO posteo ( MENSAJE, ID_USUARIO, ID_CATEGORIA) VALUES (%s, %s, %s)',#inserta posteo, le pasamos: el mensaje en si, nuestro id_usuario y la categoría
    'del_posteo':'DELETE FROM posteo WHERE ID_POSTEO = %s and ID_USUARIO = %s',#borra de tabla Posteo, le pasamos id_posteo y id_usuario
    'mostrar_categoria':'SELECT * FROM categoria',#muestra todo de categoría
    'consultar_id':'select ID FROM USUARIO WHERE EMAIL = %s',#trae ID de USUARIO, le pasamos email
    'add_amigo':'INSERT INTO amistad (ID_USUARIO1, ID_USUARIO2) VALUES (%s, %s)',#agrega en tabla Amistad nuestro id más el de nuestro amigo
    'ver_amigos':'SELECT ID_USUARIO2 FROM AMISTAD WHERE ID_USUARIO1 = %s',#ID de amigos
    'mostrar_amigos':'SELECT NOMBRE, APELLIDO FROM USUARIO WHERE ID = %s',#nombre y apellido del amigo en base al id
    'del_amigo':'DELETE FROM amistad WHERE (ID_USUARIO1, ID_USUARIO2) = (%s, %s)',#borra de tabla Amistad... le pasamos nuestro id y el usuario2
    'validar_amigo':'SELECT ID FROM USUARIO WHERE EMAIL =%s',#trae el id cuando le pasamos el email
    'mod_posteo_usuario':'UPDATE posteo set MENSAJE = %s WHERE ID_POSTEO = %s',#modifica mensaje (no implementado)
    'list_posteo_categoria':'SELECT MENSAJE FROM posteo WHERE ID_CATEGORIA = %s',#mensaje de la categoría indicada
    'list_posteos_propios':'SELECT ID_POSTEO, MENSAJE FROM posteo WHERE ID_CATEGORIA = %s AND ID_USUARIO = %s',#muestra id_posteo y mensaje, les pasamos id_cat y id_usuario
    'loguearse':'SELECT * FROM usuario WHERE EMAIL=%s AND CLAVE=%s',#usuarios donde email y clave coincidan
    'list_posteo_usuario':'SELECT * FROM posteo WHERE ID_USUARIO=%s',#todos los poste de un usuario 
    # 'list_posteos':'SELECT * FROM posteo WHERE ',#idea para mostrar posteos propios (reemplazamos por el de arriba)
    
    
}