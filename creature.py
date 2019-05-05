import random
from specie import Specie

class Creature():
    def __init__(self, id:int, specie:Specie):
        self.specie = specie
        self.id = id
        self.age = 0

    def progress(self) -> str:
        self.age += 1
        rand = random.random()
        if (rand <= self.specie.R):
            return "Reproduction"
        elif (rand <=  self.specie.R + self.specie.D):
            return "Death"

    def getName(self) -> str:
        return self.specie.name + "_" + str(self.id)