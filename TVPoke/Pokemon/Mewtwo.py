from TVPoke.BaseClasses.PokeTypes import Psychic
from TVPoke.BaseClasses.Move import Move

class Mewtwo(Psychic):
    def __init__(self):
        moves = [
            Move("Physco Cut", "PHYSCIC", 70),
            Move("Aura Sphere", "FIGHTING", 80),
            Move("Confusion", "PHYSCIC", 50),
            Move("PsyBeam", "PHYSCIC", 65)
        ]
        super().__init__("MewTwo", 80, moves, "./TVPoke/Pokemon/imgs/Mewtwo.png")