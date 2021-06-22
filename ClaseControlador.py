#from ClaseManejadorPacientes import ManejadorPacientes
from Vista import NuevoPaciente, PacientesList, PacientesView, NuevoPaciente

class Controlador():

    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.pacientes = list(repo.obtenerListaPacientes())

    # comandos que se ejecutan a través de la vista
    def crearPaciente(self):
        nuevoPaciente = NuevoPaciente(self.vista).show()
        if nuevoPaciente:
            paciente = self.repo.agregarPaciente(nuevoPaciente)
            self.pacientes.append(paciente)
            self.vista.agregarPaciente(paciente)

    def seleccionarPaciente(self, index):
        self.seleccion = index
        paciente = self.pacientes[index]
        self.vista.verPacienteEnForm(paciente)

    def modificarPaciente(self):
        if self.seleccion == -1:
            return
        rowid = self.pacientes[self.seleccion].rowid
        detallesPaciente = self.vista.obtenerDetalles()
        detallesPaciente.rowid = rowid
        paciente = self.repo.ModificarPaciente(detallesPaciente)
        self.pacientes[self.seleccion] = paciente
        self.vista.modificarPaciente(paciente, self.seleccion)
        self.seleccion = -1

    def borrarPaciente(self):
        if self.seleccion == -1:
            return
        paciente = self.pacientes[self.seleccion]
        self.repo.BorrarProvincia(paciente)
        self.pacientes.pop(self.seleccion)
        self.vista.borrarPaciente(self.seleccion)
        self.seleccion = -1

    def calcularIMC(self):
        if self.seleccion == -1:
            return
        paciente = self.pacientes[self.seleccion]
        return paciente.getIMC()

    def Start(self):
        for p in self.pacientes:
            self.vista.agregarPaciente(p)
        self.vista.mainloop()

    def SalirGrabarDatos(self):
        self.repo.GrabarDatos()
