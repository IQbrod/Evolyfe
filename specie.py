class Specie():
    def __init__(self, name:str, B:float, R:float, D:float, C: float = 0):
        self.name = name
        self.B = B
        self.R = R
        self.D = D
        self.C = C
    
    def expectedChange(self,N):
        return self.B + (self.R - self.D - self.C * N) * N

    def equilibrium(self):
    # -1 : Continuous growth | 0 : Extinction | 1+ : Equilibrium of the specie
        if self.R >= self.D:
            return -1
        else:
            return self.B / (self.D - self.R)

    def carrying_capacity(self):
    # Define maximum number of creatures when the population is on continuous growth
        if self.R >= self.D:
            return (self.R - self.D) / self.C
        else:
            return -1