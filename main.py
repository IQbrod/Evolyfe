from population import Population
from specie import Specie
from creature import Creature

if __name__ == "__main__":
    sp = Specie("Blob",0.2,0.03,0.05)
    pop = Population(sp,10)

    for _ in range(100):
        pop.progress()
    print(round(pop.specie.equilibrium(),1))
    print(pop.popStat.progression)