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
        self.implantes = []


class MarcapasosCoronario(ImplanteMedico):
    def __init__(self, tipo , funcion , electrodos, conexion, frecuencia):
        super().__init__(tipo, funcion, electrodos, conexion, frecuencia)
        self.__electrodos = electrodos
        self.__conexion = conexion
        self.__frecuencia = frecuencia



class StentCoronario(ImplanteMedico):
    def __init__(self, tipo , funcion, longitud, diametro, material):
        super().__init__(tipo,funcion,longitud,diametro,material)
        self.__longitud = longitud
        self.__diametro = diametro
        self.__material = material


class ImplantesDentales(ImplanteMedico):
    def __init__(self, tipo , funcion, forma , sistema_fijacion, material):
        super().__init__(tipo, funcion, forma, sistema_fijacion, material)
        self.__forma = forma 
        self.__sistema_fijacion = sistema_fijacion
        self.__material = material

        

class implanteRodilla(ImplanteMedico):
    def __init__(self, tipo , funcion, material , tipo_fijacion, tamaño):
        super().__init__(tipo, funcion, material , tipo_fijacion, tamaño)
        self.__material = material
        self.__tipo_fijacion = tipo_fijacion
        self.__tamaño = tamaño



class ImplanteCadera(ImplanteMedico):
    def __init__(self, tipo , funcion, material , tipo_fijacion, tamaño):
        super().__init__(tipo, funcion, material , tipo_fijacion, tamaño)
        self.__material = material
        self.__tipo_fijacion = tipo_fijacion
        self.__tamaño = tamaño


class Inventario:
    def __init__(self):
        self.implante = []

    def agregar_implante(self, implante):
        self.implante.append(implante)

    def eliminar_implante(self, implante):
        self.implante.remove(implante)
    
    def editar_implante(self,implante):
        pass

    def mostrar_inventario(self):
        for implante in self.implante:
            print(f'Tipo de implante: {type(implante).__name__}')
            print(implante)
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
        
