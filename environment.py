from population import Population

class Environment():
    def __init__(self, arr: []):
        self.pops = []
        for element in arr:
            self.pops.append(Population(element[0],element[1]))

    def progress(self):
        for pop in self.pops:
            pop.progress()