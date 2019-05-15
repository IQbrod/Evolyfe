import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2TkAgg)
import matplotlib.pyplot as pyplot

from environment import Environment
from population import Population

def get_cmap(n, name='hsv'):
    return pyplot.cm.get_cmap(name, n)

class PopListHistogram(tk.Frame):
    def __init__(self, parent: tk.Frame, env: Environment):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=env.name, font=("Verdana", 12))
        label.pack(pady=10,padx=10)

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)

        self._draw_populations(a, env.pops)
        a.set_xlabel("Time")
        a.set_ylabel("Population")

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def _draw_populations(self, subplot, pops: []):
        cmap = get_cmap(len(pops)+1)
        subplot.bar(
            range(0,len(pops[0].pop_stat.progression)), #Timeline
            [int(x[1]) for x in pops[0].pop_stat.progression], #Pop
            1, #SizeBar
            color = cmap(0) #Color
        )

        if (len(pops) > 1):
            for i in range(1,len(pops)):
                prev = [int(x[1]) for x in pops[i-1].pop_stat.progression]
                for j in range(0,i-1):
                    prev = [y+int(x[1]) for y,x in zip(prev,pops[j].pop_stat.progression)]

                subplot.bar(
                    range(0,len(pops[i].pop_stat.progression)),
                    [int(x[1]) for x in pops[i].pop_stat.progression],
                    1,
                    bottom=prev,
                    color = cmap(i)
                ) 
        
        subplot.legend([x.get_name() for x in pops])