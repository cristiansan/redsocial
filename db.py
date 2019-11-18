dbconf = {
    'host':'localhost',
    'database':'red_social',
    'user':'root',
    'password':''
}

queries = {
    'list_table':'SELECT * FROM %s',
    'add_usuario':'INSERT INTO usuario ( NOMBRE, APELLIDO, CLAVE, EMAIL, Ciudad, edad, sexo, fecha_nac) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
    'add_posteo':'INSERT INTO posteo ( MENSAJE, ID_USUARIO, ID_CATEGORIA) VALUES (%s, %s, %s)',
    # 'del_posteo':'delete from posteo where ID_POSTEO = (ID_POSTEO) VALUES (%s)',
    'del_posteo':'delete from posteo where ID_POSTEO = %s',
    
    'mostrar_categoria':'SELECT * from categoria',
    'consultar_id':'select ID from USUARIO where EMAIL = %s',
    'del_usuario':'DELETE FROM usuario WHERE EMAIL = %s',
    'add_amigo':'INSERT INTO amistad (ID_USUARIO1, ID_USUARIO2) VALUES (%s, %s)',
    'validar_amigo':'SELECT ID from USUARIO WHERE EMAIL =%s',
    # 'list_posteo':'SELECT * FROM %s',
    'list_posteo_usuario':'SELECT * FROM posteo WHERE ID_USUARIO=%s',
    'mod_posteo_usuario':'UPDATE posteo set MENSAJE = %s where ID_POSTEO = %s',
    'list_posteos':'SELECT * FROM posteo',
    'loguearse':'SELECT * FROM usuario WHERE EMAIL=%s AND CLAVE=%s',
    
}