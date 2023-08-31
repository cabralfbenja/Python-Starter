class Profesional:
    def __init__(self, dni, nom, imp, tipo_a, tipo_t):
        self.dni = dni
        self.nombre = nom
        self.importe = imp
        self.afiliacion = tipo_a
        self.trabajo = tipo_t

def to_string(profesional):
    r = ""
    r += "{:<25}".format("DNI: " + str(profesional.dni))
    r += "{:<20}".format("Nombre: " + profesional.nombre)
    r += "{:<25}".format("Importe: " + str(profesional.importe))
    r += "{:<20}".format("Afiliación: " + str(profesional.afiliacion))
    r += "{:<25}".format("Trabajo: " + str(profesional.trabajo))

    return r
