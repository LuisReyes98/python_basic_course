""" Ejemplo del uso de decoradores en python que permiten enviar 
una función por parametro y ejecutar codigo antes 
y despues de la funcion"""

PASSWORD = "123456"

def password_required(func):
    def wrapper():
        password = input('Cual es tu contraseña? ')

        if password == PASSWORD:
            return func()
        else:
            print("contraseña incorrecta")

    return wrapper


@password_required
def needs_password():
    print("la contraseña es correcta")


def to_upper(func):
    def wrapper(*args, **kwargs):
        result = func( *args, **kwargs )

        return result.upper()

    return wrapper


@to_upper
def say_my_name(name):
    return 'Hola, {}'.format(name)

if __name__ == '__main__':
    # needs_password()
    print(say_my_name("Luis"))
