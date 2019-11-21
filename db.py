#updated

dbconf = {
    'host':'localhost',
    'database':'red_social',
    'user':'root',
    'password':''
}

queries = {
    'list_table':'SELECT * FROM %s',
    'add_usuario':'INSERT INTO usuario ( NOMBRE, APELLIDO, CLAVE, EMAIL, Ciudad, edad, sexo, fecha_nac) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
    'del_usuario':'DELETE FROM usuario WHERE EMAIL = %s', 
    'add_posteo':'INSERT INTO posteo ( MENSAJE, ID_USUARIO, ID_CATEGORIA) VALUES (%s, %s, %s)',
    'del_posteo':'DELETE FROM posteo WHERE ID_POSTEO = %s',
    'mostrar_categoria':'SELECT * FROM categoria',
    'consultar_id':'select ID FROM USUARIO WHERE EMAIL = %s',
    'add_amigo':'INSERT INTO amistad (ID_USUARIO1, ID_USUARIO2) VALUES (%s, %s)',
    'del_amigo':'DELETE FROM amistad WHERE (ID_USUARIO1, ID_USUARIO2) = (%s, %s)',
    'validar_amigo':'SELECT ID FROM USUARIO WHERE EMAIL =%s',
    'list_posteo_usuario':'SELECT * FROM posteo WHERE ID_USUARIO=%s',
    'mod_posteo_usuario':'UPDATE posteo set MENSAJE = %s WHERE ID_POSTEO = %s',
    'list_posteo_categoria':'SELECT MENSAJE FROM posteo WHERE ID_CATEGORIA = %s',
    'list_posteos':'SELECT * FROM posteo',
    'loguearse':'SELECT * FROM usuario WHERE EMAIL=%s AND CLAVE=%s',
}