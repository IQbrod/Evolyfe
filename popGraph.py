import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from population import Population

class popGraphPage(tk.Frame):
    def __init__(self, parent: tk.Frame, pop: Population, emulatedPop: int = 0) :
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=pop.specie.name, font=("Verdana", 12))
        label.pack(pady=10,padx=10)

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)

        self._emulate(a, pop, emulatedPop)
        self._drawPopulation(a, pop)
        self._predict(a, pop)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    def _drawPopulation(self, subplot, pop: Population, customColor='black'):
        subplot.plot(range(0,len(pop.popStat.progression)),[int(x[1]) for x in pop.popStat.progression], color=customColor)

    def _predict(self, subplot, pop: Population):
        if pop.specie.equilibrium() <= 0:
            pred = [pop.popStat.progression[0][1]] # N at time 0
            for _ in range(0,len(pop.popStat.progression)-1):
                pred.append(pred[len(pred)-1]+pop.specie.expectedChange(pred[len(pred)-1]))
            subplot.plot(range(0,len(pop.popStat.progression)), pred, color='r', linestyle='-')
        else:
            subplot.axhline(y=pop.specie.equilibrium(), color='r', linestyle='-')
    
    def _emulate(self, subplot, pop: Population, N: int):
        # Emulate N populations like pop
        popList = []
        for _ in range(N):
            popList.append(Population(pop.specie, pop.popStat.progression[0][1]))
            for _ in range(1,len(pop.popStat.progression)):
                popList[len(popList)-1].progress()
        # Calculate average of N populations
        avg = []
        for i in range(0,len(pop.popStat.progression)):
            avg.append(0)
            for p in popList:
                avg[i] += p.popStat.progression[i][1]
            avg[i] = round(avg[i] / N, 2)

        # Draw population
        #for p in popList:
        #    self._drawPopulation(subplot, p, 'b')

        # Draw average population
        subplot.plot(range(0,len(pop.popStat.progression)),avg, color='g')