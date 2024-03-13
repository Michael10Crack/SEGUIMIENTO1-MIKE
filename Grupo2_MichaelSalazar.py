def ValNumInt(x):
    while True:
        try:
            x = int(x)
            return x
        except ValueError:
            return ValNumInt(input('Debe ingresar un dato numérico: '))
        
class ImplanteMedico:
    def __init__(self):
        pass

class ProtesisCadera(ImplanteMedico):
    def __init__(self):
        pass

class MarcapasosCoronoario(ImplanteMedico):
    def __init__(self):
        pass

class StentCoronario(ImplanteMedico):
    def __init__(self):
        pass

class ImplantesDentales(ImplanteMedico):
    def __init__(self):
        pass

class ProtesisRodilla(ImplanteMedico):
    def __init__(self):
        pass

def main():
    while True:
        menu = ValNumInt('''
                         Bienvenido al sistema.
                         Seleccione la operación que desea realizar
                         1. Agregar nuevo implante
                         2. Eliminar implante
                         3. Editar información 
                         4. Visualizar inventario completo.
                         -> ''')
        if menu == 1:
            pass
        elif menu == 2:
            pass
        elif menu == 3:
            pass
        elif menu == 4:
            pass
        elif menu == 5:
            break
        else:
            print('-ERROR-'*10)
            print('Debe seleccionar una opción válida')
        
