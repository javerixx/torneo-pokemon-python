class Pokemon:
    def __init__(self, nombre, tipo, tipo_sec, ataque, atq_es, defensa, def_es, velocidad, HP, evasion, nivel):
        """
        It takes in 10 parameters, and assigns them to the attributes of the object
        
        :param nombre: Name of the pokemon
        :param tipo: The type of the pokemon
        :param tipo_sec: secondary type
        :param ataque: Attack
        :param atq_es: Special Attack
        :param defensa: defense
        :param def_es: defense especial
        :param velocidad: Speed
        :param HP: Hit Points
        :param evasion: The chance of the pokemon dodging an attack
        :param nivel: level
        """
        self.nombre = nombre;
        self.tipo = tipo;
        self.tipo_sec = tipo_sec;
        self.ataque = ataque;
        self.atq_es = atq_es;
        self.defensa = defensa;
        self.def_es = def_es;
        self.velocidad = velocidad;
        self.HP = HP;
        self.evasion = evasion;
        self.nivel = nivel;

    def estadisticas(self):
        """
        It prints the stats of the pokemon.
        """
        print(self.nombre, self.tipo, self.tipo_sec, self.ataque, self.atq_es, self.defensa, self.def_es, self.velocidad, self.HP, self.evasion, self.nivel)


pikachu= Pokemon("PIKACHU", "ELECTRICO","ELECTRICO", 55, 50, 40,50,90,35,1,10);
pikachu.estadisticas();