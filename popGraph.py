import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2TkAgg)
from population import Population

class PopGraphPage(tk.Frame):
    def __init__(self, parent: tk.Frame, pop: Population, emulated_pop: int = 0) :
        tk.Frame.__init__(self, parent)
        self.legend=[]

        label = tk.Label(self, text=pop.specie.name, font=("Verdana", 12))
        label.pack(pady=10,padx=10)

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)

        self._draw_population(a, pop)
        self._emulate(a, pop, emulated_pop)
        self._predict(a, pop)

        a.set_xlabel("Time")
        a.set_ylabel("Population")

        a.legend(self.legend)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    def _draw_population(self, subplot, pop: Population, custom_color='black'):
        subplot.plot(range(0,len(pop.pop_stat.progression)),[int(x[1]) for x in pop.pop_stat.progression], color=custom_color)
        self.legend.append(pop.get_name())

    def _predict(self, subplot, pop: Population):
        if pop.specie.equilibrium() <= 0:
            pred = [pop.pop_stat.progression[0][1]] # N at time 0
            for _ in range(0,len(pop.pop_stat.progression)-1):
                pred.append(pred[len(pred)-1]+pop.specie.expectedChange(pred[len(pred)-1]))
            subplot.plot(range(0,len(pop.pop_stat.progression)), pred, color='r', linestyle='-')
        else:
            subplot.axhline(y=pop.specie.equilibrium(), color='r', linestyle='-')
        self.legend.append("Expected")
    
    def _emulate(self, subplot, pop: Population, N: int):
        if N != 0:
            # Emulate N populations like pop
            pop_list = []
            for _ in range(N):
                pop_list.append(Population(pop.specie, pop.pop_stat.progression[0][1]))
                for _ in range(1,len(pop.pop_stat.progression)):
                    pop_list[len(pop_list)-1].progress()
            # Calculate average of N populations
            avg = []
            for i in range(0,len(pop.pop_stat.progression)):
                avg.append(0)
                for p in pop_list:
                    avg[i] += p.pop_stat.progression[i][1]
                avg[i] = round(avg[i] / N, 2)

            # Draw population
            #for p in pop_list:
            #    self._drawPopulation(subplot, p, 'b')

            # Draw average population
            subplot.plot(range(0,len(pop.pop_stat.progression)),avg, color='g')
            self.legend.append("["+str(N)+"] Average")