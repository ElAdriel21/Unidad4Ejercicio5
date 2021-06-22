from ClaseRepositorioPacientesJSON import RespositorioPacientes
from Vista import PacientesView
from ClaseControlador import Controlador
from ObjectEncoder import ObjectEncoder

if __name__ == "__main__":
    jsonF = ObjectEncoder("provincias.json")
    repo = RespositorioPacientes(jsonF)
    vista = PacientesView()
    controlador = Controlador(repo, vista)
    vista.setControlador(controlador)
    controlador.Start()
    controlador.SalirGrabarDatos()
