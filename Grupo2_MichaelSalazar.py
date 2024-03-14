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
        self.__implantes = []

    def agregar_implante(self, implante):
        self.__implantes.append(implante)

    def eliminar_implante(self, implante):
        try:
            self.__implantes.remove(implante)
            print('Se ha eliminado correctamente del inventario.')
        except ValueError:
            print('Implante no encontrado en el sistema.')
    
    def editar_implante(self,implante):
        pass
    def getImplantes(self):
        return self.__implantes

    # def getInventario(self):
    #     for implante in self.__implante:
    #         print(f'Tipo de implante: {type(implante).__name__}')
    #         print(implante)
    #         print('----------------------------')

    # def verificar_existencia(self, tipo):
    #     for implante in self.__implante:
    #         if implante.tipo == tipo:
    #             return True
    #     return False

        
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
    def __init__(self, tipo , funcion , electrodos, conexion, frecuencia, fecha_revision, fecha_mantenimiento):
        super().__init__(tipo, funcion)
        self.__electrodos = electrodos
        self.__conexion = conexion
        self.__frecuencia = frecuencia
        self.__fecha_revision = fecha_revision
        self.__fecha_mantenimiento = fecha_mantenimiento
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
    def __str__(self):
        return f"Tipo: {self._ImplanteMedico__tipo}, Función: {self._ImplanteMedico__funcion}, Electrodos: {self.__electrodos}, Conexión: {self.__conexion}, Frecuencia: {self.__frecuencia}, Fecha de revisión: {self.__fecha_revision}, Fecha de mantenimiento: {self.__fecha_mantenimiento}"
    
class StentCoronario(ImplanteMedico):
    def __init__(self, tipo , funcion, longitud, diametro, material, fecha_revision, fecha_mantenimiento):
        super().__init__(tipo,funcion)
        self.__longitud = longitud
        self.__diametro = diametro
        self.__material = material
        self.__fecha_revision = fecha_revision
        self.__fecha_mantenimiento = fecha_mantenimiento
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
    def __str__(self):
        return f"Tipo: {self._ImplanteMedico__tipo}, Función: {self._ImplanteMedico__funcion}, Longitud: {self.__longitud}, Diámetro: {self.__diametro}, Material: {self.__material}, Fecha de revisión: {self.__fecha_revision}, Fecha de mantenimiento: {self.__fecha_mantenimiento}"
    


class ImplantesDentales(ImplanteMedico):
    def __init__(self, tipo , funcion, forma , sistema_fijacion, material, fecha_revision, fecha_mantenimiento):
        super().__init__(tipo, funcion)
        self.__forma = forma 
        self.__sistema_fijacion = sistema_fijacion
        self.__material = material
        self.__fecha_revision = fecha_revision
        self.__fecha_mantenimiento = fecha_mantenimiento
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
    def __str__(self):
        return f"Tipo: {self._ImplanteMedico__tipo}, Función: {self._ImplanteMedico__funcion}, Forma: {self.__forma}, Sistema de Fijación: {self.__sistema_fijacion}, Material: {self.__material}, Fecha de revisión: {self.__fecha_revision}, Fecha de mantenimiento: {self.__fecha_mantenimiento}"

        

class ImplanteRodilla(ImplanteMedico):
    def __init__(self, tipo , funcion, material , tipo_fijacion, tamaño, fecha_revision, fecha_mantenimiento):
        super().__init__(tipo, funcion)
        self.__material = material
        self.__tipo_fijacion = tipo_fijacion
        self.__tamaño = tamaño
        self.__fecha_revision = fecha_revision
        self.__fecha_mantenimiento = fecha_mantenimiento
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
    def __str__(self):
        return f"Tipo: {self._ImplanteMedico__tipo}, Función: {self._ImplanteMedico__funcion}, Material: {self.__material}, Tipo de fijación: {self.__tipo_fijacion}, Tamaño: {self.__tamaño}, Fecha de revisión: {self.__fecha_revision}, Fecha de mantenimiento: {self.__fecha_mantenimiento}"



class ImplanteCadera(ImplanteMedico):
    def __init__(self, tipo , funcion, material , tipo_fijacion, tamaño, fecha_revision, fecha_mantenimiento):
        super().__init__(tipo, funcion)
        self.__material = material
        self.__tipo_fijacion = tipo_fijacion
        self.__tamaño = tamaño
        self.__fecha_revision = fecha_revision
        self.__fecha_mantenimiento = fecha_mantenimiento
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
    def __str__(self):
        return f"Tipo: {self._ImplanteMedico__tipo}, Función: {self._ImplanteMedico__funcion}, Material: {self.__material}, Tipo de fijación: {self.__tipo_fijacion}, Tamaño: {self.__tamaño}, Fecha de revisión: {self.__fecha_revision}, Fecha de mantenimiento: {self.__fecha_mantenimiento}"




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
            tipo = 'MarcapasosCoronario'
            funcion = input('Ingrese la función del implante: ')
            electrodos = input('Ingrese el número de electrodos: ')
            conexion = input('Ingrese el tipo de conexión: ')
            frecuencia = input('Ingrese la frecuencia: ')
            fecha_revision = input('Ingrese la fecha de revisión del implante (YYYY-MM-DD): ')
            fecha_mantenimiento = input('Ingrese la fecha de mantenimiento del implante (YYYY-MM-DD): ')
            implante = MarcapasosCoronario( tipo, funcion, electrodos, conexion, frecuencia, fecha_revision, fecha_mantenimiento)
            return implante
        elif tipo == 2:
            tipo = 'StentCoronario'
            funcion = input('Ingrese la función del implante: ')
            longitud = input('Ingrese la longitud: ')
            diametro = input('Ingrese el diámetro: ')
            material = input('Ingrese el material: ')
            fecha_revision = input('Ingrese la fecha de revisión del implante (YYYY-MM-DD): ')
            fecha_mantenimiento = input('Ingrese la fecha de mantenimiento del implante (YYYY-MM-DD): ')
            implante = StentCoronario( tipo, funcion, longitud, diametro, material, fecha_revision, fecha_mantenimiento)
            return implante
        elif tipo == 3:
            tipo = 'ImplantesDentales '
            funcion = input('Ingrese la función del implante: ')
            forma = input('Ingrese la forma: ')
            sistema_fijacion = input('Ingrese el sistema de fijación: ')
            material = input('Ingrese el material: ')
            fecha_revision = input('Ingrese la fecha de revisión del implante (YYYY-MM-DD): ')
            fecha_mantenimiento = input('Ingrese la fecha de mantenimiento del implante (YYYY-MM-DD): ')
            implante = ImplantesDentales( tipo, funcion, forma, sistema_fijacion, material, fecha_revision, fecha_mantenimiento)
            return implante
        elif tipo == 4:
            tipo = 'ImplanteRodilla'
            funcion = input('Ingrese la función del implante: ')
            material = input('Ingrese el material: ')
            tipo_fijacion = input('Ingrese el tipo de fijación: ')
            tamaño = input('Ingrese el tamaño: ')
            fecha_revision = input('Ingrese la fecha de revisión del implante (YYYY-MM-DD): ')
            fecha_mantenimiento = input('Ingrese la fecha de mantenimiento del implante (YYYY-MM-DD): ')
            implante = ImplanteRodilla( tipo, funcion, material, tipo_fijacion, tamaño, fecha_revision, fecha_mantenimiento)
            return implante
        elif tipo == 5:
            tipo = 'ImplanteCadera '
            funcion = input('Ingrese la función del implante: ')
            material = input('Ingrese el material: ')
            tipo_fijacion = input('Ingrese el tipo de fijación: ')
            tamaño = input('Ingrese el tamaño: ')
            fecha_revision = input('Ingrese la fecha de revisión del implante (YYYY-MM-DD): ')
            fecha_mantenimiento = input('Ingrese la fecha de mantenimiento del implante (YYYY-MM-DD): ')
            implante = ImplanteCadera( tipo, funcion, material, tipo_fijacion, tamaño, fecha_revision, fecha_mantenimiento)
            
            return implante
        else:
            print('Por favor seleccione un implante válido')

def main():
    inv = Inventario()
    while True:
        menu = ValNumInt(input('''                   
                                Bienvenido al sistema.
                                Seleccione la operación que desea realizar
                                1. Agregar nuevo implante
                                2. Agregar paciente
                                3. Asignar implante a un paciente
                                4. Eliminar implante
                                5. Editar información de implante
                                6. Visualizar inventario completo
                                7. Salir
                                -> '''))
        if menu == 1:
            implante = menu_agregar_implante()
            inv.agregar_implante(implante)
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
            fecha_implantacion = input('Ingrese la fecha de implantación (YYYY-MM-DD): ')
            medico_responsable = input('Ingrese el nombre del médico responsable: ')
            estado = input('Ingrese el estado del implante: ')
            paciente.asignar_implante(implante, fecha_implantacion, medico_responsable, estado)

        elif menu == 4:
            lista_implantes = inv.getImplantes()
            if not lista_implantes:
                print('El inventario está vacío.')
            else:
                print('Lista de implantes en el inventario: ')
                for i, implante in enumerate(lista_implantes, start=1):
                    print(f'{i}. {implante}')
                Eliminar = ValNumInt(input('Seleccione el número de implante que desea eliminar: '))
                if 1 <= Eliminar <= len(lista_implantes):
                    implante_eliminado = lista_implantes[Eliminar - 1]
                    inv.eliminar_implante(implante_eliminado)
                else:
                    print('No se ha encontrado el implante seleccionado en el inventario')
        elif menu == 5:
            lista_implantes = inv.getImplantes()
            if not lista_implantes:
                print('El inventario está vacío.')
            else:
                print('Lista de implantes en el inventario: ')
                for i, implante in enumerate(lista_implantes, start=1):
                    print(f'{i}. {implante}')

                editar = ValNumInt(input('Seleccione el número de implante que desea editar: '))
                if 1 <= editar <= len(lista_implantes):
                    implante_editar = lista_implantes[editar - 1]
                    while True:
                        nuevo_nombre = ValNumInt(input('''Seleccione el nuevo tipo de implante:
                                            1. MarcapasosCoronario
                                            2. StentCoronario
                                            3. ImplantesDentales 
                                            4. ImplanteRodilla
                                            5. ImplanteCadera 
                                            -> '''))
                        if nuevo_nombre == 1:
                            tipo = 'MarcapasosCoronario'
                            funcion = input('Ingrese la función del implante: ')
                            electrodos = input('Ingrese el número de electrodos: ')
                            conexion = input('Ingrese el tipo de conexión: ')
                            frecuencia = input('Ingrese la frecuencia: ')
                            fecha_revision = input('Ingrese la fecha de revisión del implante (YYYY-MM-DD): ')
                            fecha_mantenimiento = input('Ingrese la fecha de mantenimiento del implante (YYYY-MM-DD): ')
                            implante = MarcapasosCoronario( tipo, funcion, electrodos, conexion, frecuencia, fecha_revision, fecha_mantenimiento)
                            print('Información del implante editada correctamente.')
                            return implante
                        elif nuevo_nombre== 2:
                            tipo = 'StentCoronario'
                            funcion = input('Ingrese la función del implante: ')
                            longitud = input('Ingrese la longitud: ')
                            diametro = input('Ingrese el diámetro: ')
                            material = input('Ingrese el material: ')
                            fecha_revision = input('Ingrese la fecha de revisión del implante (YYYY-MM-DD): ')
                            fecha_mantenimiento = input('Ingrese la fecha de mantenimiento del implante (YYYY-MM-DD): ')
                            implante = StentCoronario( tipo, funcion, longitud, diametro, material, fecha_revision, fecha_mantenimiento)
                            print('Información del implante editada correctamente.')
                            return implante
                        elif nuevo_nombre == 3:
                            tipo = 'ImplantesDentales '
                            funcion = input('Ingrese la función del implante: ')
                            forma = input('Ingrese la forma: ')
                            sistema_fijacion = input('Ingrese el sistema de fijación: ')
                            material = input('Ingrese el material: ')
                            fecha_revision = input('Ingrese la fecha de revisión del implante (YYYY-MM-DD): ')
                            fecha_mantenimiento = input('Ingrese la fecha de mantenimiento del implante (YYYY-MM-DD): ')
                            implante = ImplantesDentales( tipo, funcion, forma, sistema_fijacion, material, fecha_revision, fecha_mantenimiento)
                            print('Información del implante editada correctamente.')
                            return implante
                        elif nuevo_nombre== 4:
                            tipo = 'ImplanteRodilla'
                            funcion = input('Ingrese la función del implante: ')
                            material = input('Ingrese el material: ')
                            tipo_fijacion = input('Ingrese el tipo de fijación: ')
                            tamaño = input('Ingrese el tamaño: ')
                            fecha_revision = input('Ingrese la fecha de revisión del implante (YYYY-MM-DD): ')
                            fecha_mantenimiento = input('Ingrese la fecha de mantenimiento del implante (YYYY-MM-DD): ')
                            implante = ImplanteRodilla( tipo, funcion, material, tipo_fijacion, tamaño, fecha_revision, fecha_mantenimiento)
                            print('Información del implante editada correctamente.')
                            return implante
                        elif nuevo_nombre == 5:
                            tipo = 'ImplanteCadera '
                            funcion = input('Ingrese la función del implante: ')
                            material = input('Ingrese el material: ')
                            tipo_fijacion = input('Ingrese el tipo de fijación: ')
                            tamaño = input('Ingrese el tamaño: ')
                            fecha_revision = input('Ingrese la fecha de revisión del implante (YYYY-MM-DD): ')
                            fecha_mantenimiento = input('Ingrese la fecha de mantenimiento del implante (YYYY-MM-DD): ')
                            implante = ImplanteCadera( tipo, funcion, material, tipo_fijacion, tamaño, fecha_revision, fecha_mantenimiento)
                            print('Información del implante editada correctamente.')
                            return implante
                        else:
                            print('No se ha encontrado el implante seleccionado en el inventario.')
        
        elif menu == 6:
            lista_implantes = inv.getImplantes()
            if not lista_implantes:
                print('El inventario está vacío.')
            else:
                print('Lista de implantes en el inventario: ')
                for i, implante in enumerate(lista_implantes, start=1):
                    print(f'{i}. {implante}')
                
        elif menu == 7:
            break
        else:
            print('-ERROR-'*10)
            print('Debe seleccionar una opción válida')
        
main()
