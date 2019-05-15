from specie import Specie
from creature import Creature
import random

class Population():
    def __init__(self, specie:Specie, N:int):
        # Parameters
        self.specie = specie
        self.pop = []
        # Core objects
        self.popStat = _StatPopulation()
        self._toAppend = []
        self._toKill = []
        # Init
        for _ in range(1,N+1):
            self.pop.append( Creature((len(self.pop)+1), self.specie) )
        # Init log
        self.popStat.prepareLog()
        self.popStat.logSize(N)

    def progress(self):
        # Prepare Log 
        self.popStat.prepareLog()
        # Creatures progression
        for creature in self.pop:
            ret = creature.progress()
            if random.random() <= creature.specie.R:
                self.reproduction(creature)
            if random.random() <= creature.specie.D + creature.specie.C * len(self.pop):
                self.kill(creature)
        # Application
        for app in self._toAppend:
            self.pop.append(app)
        for kil in self._toKill:
            self.pop.remove(kil)
        self._toAppend = []
        self._toKill = []
        # Spontaneous Birth
        rand = random.random()
        if (rand <= self.specie.B):
            self.pop.append( Creature((len(self.pop)+1), self.specie) )
            self.popStat.logAction("B")
        # Log size
        self.popStat.logSize(len(self.pop))
    
    def reproduction(self, father: Creature):
        son = Creature( (len(self.pop)+len(self._toAppend)+1), father.specie )
        self._toAppend.append(son)
        self.popStat.logAction("R")

    def kill(self, victim: Creature):
        self._toKill.append(victim)
        self.popStat.logAction("D")

    def getName(self):
        return self.specie.name

class _StatPopulation():
    def __init__(self):
        self.progression = []

    def prepareLog(self):
        self.progression.append(["",0])

    def logAction(self, action: str):
        self.progression[len(self.progression)-1][0] += action

    def logSize(self, popSize: int):
        self.progression[len(self.progression)-1][1] = popSize