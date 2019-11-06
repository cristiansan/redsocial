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
    # 'list_posteo':'SELECT * FROM %s',
    'list_posteo_usuario':'SELECT * FROM posteo WHERE ID_USUARIO=%s',
    'mod_posteo_usuario':'UPDATE posteo set MENSAJE = %s where ID_POSTEO = %s',
    'list_posteos':'SELECT * FROM posteo',
    'loguearse':'SELECT * FROM usuario WHERE EMAIL=%s AND CLAVE=%s',
    
}

