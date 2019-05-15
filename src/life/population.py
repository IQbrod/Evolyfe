from specie import Specie
from creature import Creature
import random

class Population():
    def __init__(self, specie:Specie, N:int):
        # Parameters
        self.specie = specie
        self.pop = []
        # Core objects
        self.pop_stat = _StatPopulation()
        self._to_append = []
        self._to_kill = []
        # Init
        for _ in range(1,N+1):
            self.pop.append( Creature((len(self.pop)+1), self.specie) )
        # Init log
        self.pop_stat.prepare_log()
        self.pop_stat.log_size(N)

    def progress(self):
        # Prepare Log 
        self.pop_stat.prepare_log()
        # Creatures progression
        for creature in self.pop:
            creature.progress()
            if random.random() <= creature.specie.R:
                self.reproduction(creature)
            if random.random() <= creature.specie.D + creature.specie.C * len(self.pop):
                self.kill(creature)
        # Application
        for app in self._to_append:
            self.pop.append(app)
        for kil in self._to_kill:
            self.pop.remove(kil)
        self._to_append = []
        self._to_kill = []
        # Spontaneous Birth
        rand = random.random()
        if (rand <= self.specie.B):
            self.pop.append( Creature((len(self.pop)+1), self.specie) )
            self.pop_stat.log_action("B")
        # Log size
        self.pop_stat.log_size(len(self.pop))
    
    def reproduction(self, father: Creature):
        son = Creature( (len(self.pop)+len(self._to_append)+1), father.specie )
        self._to_append.append(son)
        self.pop_stat.log_action("R")

    def kill(self, victim: Creature):
        self._to_kill.append(victim)
        self.pop_stat.log_action("D")

    def get_name(self):
        return self.specie.name

class _StatPopulation():
    def __init__(self):
        self.progression = []

    def prepare_log(self):
        self.progression.append(["",0])

    def log_action(self, action: str):
        self.progression[len(self.progression)-1][0] += action

    def log_size(self, pop_size: int):
        self.progression[len(self.progression)-1][1] = pop_size