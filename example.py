diccionario_uno = {'usernames' : 'Eduardo Ismael'}
data_model = {'username': 'Garcia Perez'}

mensaje = 'El username es {username} !'.format( **diccionario_uno or **data_model)
print mensaje