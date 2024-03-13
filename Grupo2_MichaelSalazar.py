def ValNumInt(x):
    while True:
        try:
            x = int(x)
            return x
        except ValueError:
            return ValNumInt(input('Debe ingresar un dato numérico: '))
        
class ImplanteMedico:
    def __init__(self, tipo , funcion, fecha_implantacion, medico_responsable, estado):
        self.__tipo = tipo
        self.__funcion = funcion
        self.__fecha_implantacion = fecha_implantacion
        self.__medico_responsable = medico_responsable
        self.__estado = estado
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
        implante.__fecha_implantacion = fecha_implantacion
        implante.__medico_responsable = medico_responsable
        implante.__estado = estado
        self.__implantes.append(implante)



class MarcapasosCoronario(ImplanteMedico):
    def __init__(self, tipo , funcion , electrodos, conexion, frecuencia):
        super().__init__(tipo, funcion, electrodos, conexion, frecuencia)
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
        super().__init__(tipo,funcion,longitud,diametro,material)
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
        super().__init__(tipo, funcion, forma, sistema_fijacion, material)
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

        

class implanteRodilla(ImplanteMedico):
    def __init__(self, tipo , funcion, material , tipo_fijacion, tamaño):
        super().__init__(tipo, funcion, material , tipo_fijacion, tamaño)
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
        super().__init__(tipo, funcion, material , tipo_fijacion, tamaño)
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
        
