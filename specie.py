class Specie():
    def __init__(self, name:str, B:float, R:float, D:float):
        self.name = name
        self.B = B
        self.R = R
        self.D = D
    
    def expectedChange(self,N):
        return self.B + (self.R - self.D) * N

    def equilibrium(self):
    # -1 : Continuous growth | 0 : Extinction | 1+ : Equilibrium of the specie
        if self.R >= self.D:
            return -1
        else:
            return self.B / (self.D - self.R)
