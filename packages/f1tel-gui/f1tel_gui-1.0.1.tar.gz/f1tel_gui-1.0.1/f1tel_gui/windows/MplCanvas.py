from curses import wrapper
import sys
import matplotlib
import pandas as pd
matplotlib.use('Qt5Agg')

from PyQt5.QtWidgets import QVBoxLayout, QWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100, fig_index = 1):
        self.fig = plt.figure(figsize=(width, height), dpi=dpi, tight_layout=True, num=fig_index)
        super(MplCanvas, self).__init__(self.fig)
        self.toolbar = NavigationToolbar(self, parent)
        self.graphs = pd.DataFrame(columns=['graphName', 'graph'])
        self.layout =  QVBoxLayout()
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self)
        self.wrapper = parent
        self.wrapper.setLayout(self.layout)
        plt.grid(True)
        
        
    def add_subgraph(self,position, graphName=None, data_x=[], data_y=[], y_label=None, x_label=None, sharex=False, grid=True) -> None:

        plt.figure(self.fig.number)

        if not self.graphs.empty:
            if sharex:
                ax = self.fig.add_subplot(position, sharex=self.graphs.loc[0, "graph"].axes)
                ax.plot(data_x, data_y)
                
        else:
            ax = plt.subplot(position)
            ax.plot(data_x, data_y)
        
        
        if y_label is not None:
            ax.set_ylabel(y_label)
        if x_label is not None:
            ax.set_xlabel(x_label)
        if graphName is not None or graphName != "":
            ax.set_title(graphName)
        ax.grid(grid, linestyle = '--', linewidth = 0.2)
        self.graphs.loc[len(self.graphs)] = [graphName if graphName != None else "graphName{}".format(len(self.graphs))] + [ax]
        

        self.replot()
        return ax

    def get_graph(self, index):
        plt.figure(self.fig.number)
        return self.graphs.loc[self.graphs.graphName==index, "graph"].to_list()[0]

    def replot(self):
        plt.figure(self.fig.number)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def clear(self):
        plt.figure(self.fig.number)
        self.fig.clear()
        self.graphs = pd.DataFrame(columns=['graphName', 'graph'])
        self.replot()
        