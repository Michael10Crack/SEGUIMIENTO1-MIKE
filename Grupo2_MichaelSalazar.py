def ValNumInt(x):
    while True:
        try:
            x = int(x)
            return x
        except ValueError:
            return ValNumInt(input('Debe ingresar un dato numérico: '))
class Sistema():
    def __init__(self):
        self.__bd = []
    def registrar_paciente(self,paciente):
        self.__bd.append(paciente)
    def getbase_datos(self):
        return self.__bd
class Inventario:
    def __init__(self):
        self.__implante = []

    def agregar_implante(self, implante):
        self.__implante.append(implante)

    def eliminar_implante(self, implante):
        self.__implante.remove(implante)
    
    def editar_implante(self,implante):
        pass

    def getInventario(self):
        for implante in self.__implante:
            print(f'Tipo de implante: {type(implante).__name__}')
            print(implante)
            print('----------------------------')

    def verificar_existencia(self, tipo):
        for implante in self.__implante:
            if implante.tipo == tipo:
                return True
        return False

        
class ImplanteMedico:
    def __init__(self, tipo , funcion):
        self.__tipo = tipo
        self.__funcion = funcion
        self.__fecha_implantacion = None
        self.__medico_responsable = None
        self.__estado = None
    def getTipo(self):
        return self.__tipo
    def getFuncion(self):
        return self.__funcion
    def getFechaImplantacion(self):
        return self.__fecha_implantacion
    def getMedico(self):
        return self.__medico_responsable
    def getEstado(self):
        return self.__estado
    
    def setTipo(self, t):
        self.__tipo = t
    def setFuncion(self, f):
        self.__funcion = f
    def setFechaImplantacion(self, f):
        self.__fecha_implantacion = f
    def setMedico(self, m):
        self.__medico_responsable = m
    def setEstado(self, e):
        self.__estado = e
class Paciente:
    def __init__(self, Nombre, Apellido, Edad):
        self.__nombre = Nombre
        self.__apellido = Apellido
        self.__edad = Edad
        self.__implantes = []
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getEdad(self):
        return self.__edad
    def getImplante(self):
        return self.__implantes
    def setNombre(self, n):
        self.__nombre = n
    def setApellido(self,a):
        self.__apellido = a
    def setEdad(self,e):
        self.__edad = e
    def asignar_implante(self, implante, fecha_implantacion, medico_responsable, estado):
        implante.__setFecha_implantacion = fecha_implantacion
        implante.__setMedico_responsable = medico_responsable
        implante.__setEstado = estado
        self.__implantes.append(implante)



class MarcapasosCoronario(ImplanteMedico):
    def __init__(self, tipo , funcion , electrodos, conexion, frecuencia):
        super().__init__(tipo, funcion)
        self.__electrodos = electrodos
        self.__conexion = conexion
        self.__frecuencia = frecuencia
    def getElectrodos(self):
        return self.__electrodos
    def getConexion(self):
        return self.__conexion
    def getFrecuencia(self):
        return self.__frecuencia
    def setElectrodos(self, n):
        self.__electrodos = n
    def setConexion(self,c):
        self.__conexion = c
    def setFrecuencia(self, f):
        self.__frecuencia = f
class StentCoronario(ImplanteMedico):
    def __init__(self, tipo , funcion, longitud, diametro, material):
        super().__init__(tipo,funcion)
        self.__longitud = longitud
        self.__diametro = diametro
        self.__material = material
    def getLongitud(self):
        return self.__longitud
    def getDiametro(self):
        return self.__diametro
    def getMaterial(self):
        return self.__material
    def setLongitud(self, l):
        self.__longitud = l
    def setDiametro(self,d):
        self.__diametro = d
    def setMaterial(self,m):
        self.__material = m


class ImplantesDentales(ImplanteMedico):
    def __init__(self, tipo , funcion, forma , sistema_fijacion, material):
        super().__init__(tipo, funcion)
        self.__forma = forma 
        self.__sistema_fijacion = sistema_fijacion
        self.__material = material
    def getForma(self):
        return self.__forma
    def getSisFijacion(self):
        return self.__sistema_fijacion
    def getMaterial(self):
        return self.__material
    def setForma(self, f):
        self.__forma = f
    def setSisFijacion(self,s):
        self.__sistema_fijacion = s
    def setMaterial(self,m):
        self.__material = m

        

class ImplanteRodilla(ImplanteMedico):
    def __init__(self, tipo , funcion, material , tipo_fijacion, tamaño):
        super().__init__(tipo, funcion)
        self.__material = material
        self.__tipo_fijacion = tipo_fijacion
        self.__tamaño = tamaño
    def getMaterial(self):
        return self.__material
    def getTipoFijacion(self):
        return self.__tipo_fijacion
    def getTamaño(self):
        return self.__tamaño
    def setMaterial(self,m):
        self.__material = m
    def setTipoFijacion(self, tf):
        self.__tipo_fijacion = tf
    def setTamaño(self, t):
        self.__tamaño = t



class ImplanteCadera(ImplanteMedico):
    def __init__(self, tipo , funcion, material , tipo_fijacion, tamaño):
        super().__init__(tipo, funcion)
        self.__material = material
        self.__tipo_fijacion = tipo_fijacion
        self.__tamaño = tamaño
    def getMaterial(self):
        return self.__material
    def getTipoFijacion(self):
        return self.__tipo_fijacion
    def getTamaño(self):
        return self.__tamaño
    def setMaterial(self,m):
        self.__material = m
    def setTipoFijacion(self, tf):
        self.__tipo_fijacion = tf
    def setTamaño(self, t):
        self.__tamaño = t



def menu_agregar_implante():
    while True:
        tipo = ValNumInt(input('''Ingrese el tipo de implante: 
                                        1. MarcapasosCoronario
                                        2. StentCoronario
                                        3. ImplantesDentales 
                                        4. ImplanteRodilla
                                        5. ImplanteCadera 
                                        -> '''))
        if tipo == 1:
            funcion = input('Ingrese la función del implante: ')
            electrodos = input('Ingrese el número de electrodos: ')
            conexion = input('Ingrese el tipo de conexión: ')
            frecuencia = input('Ingrese la frecuencia: ')
            implante = MarcapasosCoronario( tipo, funcion, electrodos, conexion, frecuencia)
            return implante
        elif tipo == 2:
            funcion = input('Ingrese la función del implante: ')
            longitud = input('Ingrese la longitud: ')
            diametro = input('Ingrese el diámetro: ')
            material = input('Ingrese el material: ')
            implante = StentCoronario( tipo, funcion, longitud, diametro, material)
            return implante
        elif tipo == 3:
            funcion = input('Ingrese la función del implante: ')
            forma = input('Ingrese la forma: ')
            sistema_fijacion = input('Ingrese el sistema de fijación: ')
            material = input('Ingrese el material: ')
            implante = ImplantesDentales( tipo, funcion, forma, sistema_fijacion, material)
            return implante
        elif tipo == 4:
            funcion = input('Ingrese la función del implante: ')
            material = input('Ingrese el material: ')
            tipo_fijacion = input('Ingrese el tipo de fijación: ')
            tamaño = input('Ingrese el tamaño: ')
            implante = ImplanteRodilla( tipo, funcion, material, tipo_fijacion, tamaño)
            return implante
        elif tipo == 5:
            funcion = input('Ingrese la función del implante: ')
            material = input('Ingrese el material: ')
            tipo_fijacion = input('Ingrese el tipo de fijación: ')
            tamaño = input('Ingrese el tamaño: ')
            implante = ImplanteCadera( tipo, funcion, material, tipo_fijacion, tamaño)
            return implante
        else:
            print('Por favor seleccione un implante válido')

def main():
    while True:
        menu = ValNumInt(input('''                   
                                Bienvenido al sistema.
                                Seleccione la operación que desea realizar
                                1. Agregar nuevo implante
                                2. Agregar paciente
                                3. Asignar implante a un paciente
                                4. Eliminar implante
                                5. Editar información 
                                6. Visualizar inventario completo
                                7. Salir
                                -> '''))
        if menu == 1:
            implante = menu_agregar_implante()
            Inventario().agregar_implante(implante)
            print('Se ha ingresado el implante correctamente')
        elif menu == 2:
            sis = Sistema()
            p = Paciente
            nombre = input('Ingrese el/los nombre del paciente: ')
            apellido = input('Ingrese los apellidos del paciente: ')
            edad = ValNumInt(input('Digite la edad del paciente: '))
            paciente = p(nombre,apellido,edad)
            sis.registrar_paciente(paciente)
            print('Información agregada exitósamente')
            print('-'*50)
            # print(f' Nombre del paciente: {paciente.getNombre()}')
            # print(f' Apellido del paciente: {paciente.getApellido()}')
            # print(f' Edad del paciente: {paciente.getEdad()}')
        elif menu == 3:
            p = Paciente
            nombre = input('Ingrese el/los nombre del paciente: ')
            apellido = input('Ingrese los apellidos del paciente: ')
            edad = ValNumInt(input('Digite la edad del paciente: '))
            paciente = p(nombre, apellido, edad)
            tipo_implante = input('Ingrese el tipo de implante: ')
            funcion_implante = input('Ingrese la función del implante: ')
            implante = ImplanteMedico(tipo_implante, funcion_implante)

        elif menu == 4:
            pass
        elif menu == 5:
            Inv = Inventario()
            print(Inv.getInventario())
        
        elif menu == 6:
            Inv = Inventario()
            print(Inv.getInventario())
        elif menu == 7:
            break
        else:
            print('-ERROR-'*10)
            print('Debe seleccionar una opción válida')
        
main()
