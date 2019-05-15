import tkinter as tk
from popGraph import PopGraphPage
from population import Population
from specie import Specie
from creature import Creature
from environment import Environment
from popListHistogram import PopListHistogram

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "Evolyfe")
        
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand = True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def display_pop(self, pop: Population, emulated: int = 0):
        frame = PopGraphPage(self.container, pop, emulated)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
    
    def display_environment_populations(self, env: Environment):
        frame = PopListHistogram(self.container, env)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

if __name__ == "__main__":
    pops = [[Specie("Blob-Stable",0,0.02,0.02),40],[Specie("Blob-Increase",0,0.023,0.02),50],[Specie("Blob-Decrease",0,0.02,0.025),50]]

    e = Environment("BlobLand",pops)

    for _ in range(300):
        e.progress()

    app = App()
    app.display_environment_populations(e)
    app.mainloop()