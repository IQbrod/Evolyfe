from specie import Specie
from creature import Creature
import random

class Population():
    def __init__(self, specie:Specie, N:int):
        self.specie = specie
        self.pop = []
        self.toAppend = []
        self.toKill = []
        for _ in range(1,N+1):
            self.pop.append( Creature((len(self.pop)+1), self.specie) )

    def progress(self):
        for creature in self.pop:
            ret = creature.progress()
            if ret == "Reproduction":
                self.reproduction(creature)
            elif ret == "Death":
                self.kill(creature)
        for app in self.toAppend:
            self.pop.append(app)
        for kil in self.toKill:
            self.pop.remove(kil)
        self.toAppend = []
        self.toKill = []

        rand = random.random()
        if (rand <= self.specie.B):
            self.pop.append( Creature((len(self.pop)+1), self.specie) )

        print(len(self.pop))
    
    def reproduction(self, father: Creature):
        son = Creature( (len(self.pop)+len(self.toAppend)+1), father.specie )
        self.toAppend.append(son)
        #print (father.getName() + " duplicates as " + son.getName())

    def kill(self, victim: Creature):
        self.toKill.append(victim)
        #print (victim.getName() + " died")
