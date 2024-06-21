import re

def verificar_contraseña(contraseña):
    # Verifica la longitud de la contraseña
    if len(contraseña) < 8 or len(contraseña) > 10:
        print("La longitud de la contraseña debe ser entre 8 y 10 caracteres.")
        return False

    # Verifica si contiene al menos una letra mayúscula
    if not re.search(r'[A-Z]', contraseña):
        print("La contraseña debe contener al menos una letra mayúscula.")
        return False

    # Verifica si contiene al menos una letra minúscula
    if not re.search(r'[a-z]', contraseña):
        print("La contraseña debe contener al menos una letra minúscula.")
        return False

    # Verifica si contiene al menos un número
    if not re.search(r'\d', contraseña):
        print("La contraseña debe contener al menos un número.")
        return False

    # Verifica si contiene al menos un carácter especial
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña):
        print("La contraseña debe contener al menos un carácter especial.")
        return False

    # Verifica si contiene al menos dos letras (mayúsculas o minúsculas)
    if len(re.findall(r'[a-zA-Z]', contraseña)) < 2:
        print("La contraseña debe contener al menos dos letras.")
        return False

    return True


# Programa principal
while True:
    contraseña = input("Introduce una contraseña: ")
    if verificar_contraseña(contraseña):
        print("Contraseña válida.")
        break
    else:
        print("Contraseña no válida, inténtalo de nuevo.")
        
#  casos de rpueba y los resulltados esperados 

# ("Ab1!", False),           # Menor a 8 caracteres
#         ("Abc123!@", True),        # Longitud válida
#         ("Abcdefg123!", False),    # Mayor a 10 caracteres
#         ("abcdefgh", False),       # Sin mayúsculas
#         ("ABCDEFGH", False),       # Sin minúsculas
#         ("Abcdefgh", False),       # Sin números
#         ("Abcdef12", False),       # Sin caracteres especiales
#         ("1a!", False),            # Menos de dos letras