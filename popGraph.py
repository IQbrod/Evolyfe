import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from population import Population

class popGraphPage(tk.Frame):
    def __init__(self, parent: tk.Frame, pop: Population):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=pop.specie.name, font=("Verdana", 12))
        label.pack(pady=10,padx=10)

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)

        a.plot(range(0,len(pop.popStat.progression)),[int(x[1]) for x in pop.popStat.progression], color='b')
        if pop.specie.equilibrium() <= 0:
            pred = [pop.popStat.progression[0][1]] # N at time 0
            for _ in range(0,len(pop.popStat.progression)-1):
                pred.append(pred[len(pred)-1]+pop.specie.expectedChange(pred[len(pred)-1]))
            a.plot(range(0,len(pop.popStat.progression)), pred, color='r', linestyle='-')
        else:
            a.axhline(y=pop.specie.equilibrium(), color='r', linestyle='-')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)