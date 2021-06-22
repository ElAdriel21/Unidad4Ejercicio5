#from ClasePaciente import Paciente
#from ObjectEncoder import ObjectEncoder
#from ClaseManejadorPacientes import ManejadorPacientes

class RespositorioPacientes(object):
    __conn = None
    __manejador = None

    def __init__(self, conn):
        self.__conn = conn
        diccionario = self.__conn.leerJSONArchivo()
        self.__manejador = self.__conn.decodificadorDiccionario(diccionario)

    def obtenerListaPacientes(self):
        return self.__manejador.getListaPacientes()

    def agregarPaciente(self, paciente):
        self.__manejador.agregarPaciente(paciente)
        return paciente

    def modificarPaciente(self, paciente):
        self.__manejador.updatePaciente(paciente)
        return paciente

    def borrarPaciente(self, paciente):
        self.__manejador.eliminarPaciente(paciente)

    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())
