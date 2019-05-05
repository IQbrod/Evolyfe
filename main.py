import tkinter as tk
from popGraph import popGraphPage
from population import Population
from specie import Specie
from creature import Creature

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "Evolyfe")
        
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand = True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def displayPop(self, pop: Population, emulated: int = 0):
        frame = popGraphPage(self.container, pop, emulated)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

if __name__ == "__main__":
    sp = Specie("Blob",0,0.05,0.02,0.0004)
    pop = Population(sp,10)
    print(sp.carryingCapacity())
    for _ in range(300):
        pop.progress()

    app = App()
    app.displayPop(pop,10)
    app.mainloop()