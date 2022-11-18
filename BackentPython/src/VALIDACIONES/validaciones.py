from flask import request
#Validar que el campo este lleno
def validar_campo(request)-> bool:
    print(request['cedula'])
    
# Valida el código (si es numérico y de longitud 6).
def validar_nombres(nombres: str) -> bool:
    return (len(nombres) > 0 and len(nombres) <= 30)

# Valida el nombre (si es un texto sin espacios en blanco de entre 1 y 30 caracteres).
def validar_apellidos(apellidos: str) -> bool:
    apellidos = apellidos.strip()
    return (len(apellidos) > 0 and len(apellidos) <= 30)

# Valida que los créditos estén entre 1 y 9.
def validar_correo(cedula: str) -> bool:
    cedula = cedula.strip()
    return (len(cedula) > 0 and len(cedula) <= 30)

