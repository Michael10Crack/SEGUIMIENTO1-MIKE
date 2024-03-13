def ValNumInt(x):
    while True:
        try:
            x = int(x)
            return x
        except ValueError:
            return ValNumInt(input('Debe ingresar un dato numérico: '))
        
class ImplanteMedico:
    def __init__(self, tipo , funcion ):
        self.__tipo = tipo
        self.__funcion = funcion

class Paciente:
    def __init__(self, Nombre, Apellido, Edad):
        self.__nombre = Nombre
        self.__apellido = Apellido
        self.__edad = Edad


class ProtesisCadera(ImplanteMedico):
    def __init__(self, tipo , funcion):
        pass

class MarcapasosCoronoario(ImplanteMedico):
    def __init__(self, tipo , funcion):
        pass

class StentCoronario(ImplanteMedico):
    def __init__(self, tipo , funcion):
        pass

class ImplantesDentales(ImplanteMedico):
    def __init__(self, tipo , funcion):
        pass

class ProtesisRodilla(ImplanteMedico):
    def __init__(self, tipo , funcion):
        pass

class Inventario:
    def __init__(self):
        self.protesis = []

    def agregar_protesis(self, protesis):
        self.protesis.append(protesis)

    def eliminar_protesis(self, protesis):
        self.protesis.remove(protesis)

    def mostrar_inventario(self):
        for protesis in self.protesis:
            print(f'Tipo de protesis: {type(protesis).__name__}')
            print(protesis)
            print('----------------------------')



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
        
