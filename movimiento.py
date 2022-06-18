class Movimiento:
    def __init__(self, nombre, tipo, categoria, daño, precision, pp, efecto_sec):
        self.nombre = nombre;
        self.tipo = tipo;
        self.categoria = categoria;
        self.daño = daño;
        self.precision = precision;
        self.pp=pp;
        self.efecto_sec=efecto_sec;

    def estadistica(self):
        print(self.nombre, self.tipo, self.categoria, self.daño, self.precision, self.pp, self.efecto_sec)

impactrueno=Movimiento("IMPACTURENO", "ELECTRICO", "ESPECIAL", 40,100,30,"paralizar")
impactrueno.estadistica();