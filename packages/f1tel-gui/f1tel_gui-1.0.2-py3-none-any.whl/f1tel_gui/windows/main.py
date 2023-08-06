import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QThreadPool

import numpy as np
import pandas as pd

from f1tel_gui.utils import get_design_path, get_current_season, get_json_layout_path
from f1tel_gui.F1tel import F1tel
from f1tel_gui.thread.load_f1_obj import LoadF1Obj, LoadF1Graph, LoadF1GraphLayout
from f1tel_gui.windows.MplCanvas import MplCanvas
from f1tel_gui.windows.loading_dialog import LoadingDialog, ErrorDialog

class MainWindow(QMainWindow):

    _graph_containers = []

    def __init__(self, graph_layout_path=get_json_layout_path()):
        super(MainWindow, self).__init__()
        loadUi(get_design_path("main.ui"), self)
        self.pool = QThreadPool.globalInstance()
        self._init_season_select()
        self._init_circuit_select()
        
        self.lap_number.setKeyboardTracking(False)
        self.lap_number.valueChanged.connect(self._lap_number_changed)
        self.is_fastestlap.stateChanged.connect(self._fastestlap_checkbox_changed)
        self.is_fastestlap.setChecked(True)
        self._load_f1_graph_layout(graph_layout=graph_layout_path)

    def _fastestlap_checkbox_changed(self, state):
        if state == Qt.Checked:
            self.lap_number.setEnabled(False)
        else:
            self.lap_number.setEnabled(True)

        self._update_graphs_after_lap_number_changed()

    def _lap_number_changed(self, value):
        self._update_graphs_after_lap_number_changed()

    def _load_f1_graph_layout(self, graph_layout):
        load_f1_layout =  LoadF1GraphLayout(layout_file_path=graph_layout)
        self._connect_loading_signals(load_f1_layout.signals)
        load_f1_layout.signals.signal.connect(self._upload_graph_layout)
        self.pool.start(load_f1_layout)

    def _upload_graph_layout(self, obj):
        self.show()
        graph_layout=obj
        self._graph_containers = []
        self.tabframe.clear()
        for i, graph_canvas in enumerate(graph_layout, start=1):
            tab_w = QWidget()
            self.tabframe.addTab(tab_w, graph_canvas["tabname"])
            self._graph_containers.append({"tabname": graph_canvas["tabname"], "canvas": MplCanvas(parent=tab_w, width=5, height=10, dpi=100, fig_index=i), "graphs": graph_canvas["graphs"]})
        self._load_f1_object(season=int(self.season_select.currentText()), circuit=self.circuit_select.currentText(), session='FP1', init_session=True, init_drivers=True)


    def _load_f1_object(self, season, circuit, session, disable_cache=False, init_session=True, init_drivers=True):
        
        if session == "":
            return

        load_f1 = LoadF1Obj(season, circuit, session, disable_cache, update_session=init_session, update_drivers=init_drivers)

        if init_session:
            window_title = "Loading session"
            message = "Loading session {} for {}@{}".format(session, season, circuit)
        elif init_drivers:
            window_title = "Loading drivers"
            message = "Loading drivers for {} {}@{}".format(season, circuit, session)


        load_f1.signals.signal.connect(self._update_f1_object)
        self._connect_loading_signals(load_f1.signals, window_title=window_title, window_message=message)
        self.pool.start(load_f1)

    def _print_f1_graph(self, checkbox, graph_layout, graph_widget):
        load_f1_graph = LoadF1Graph(f1=self.f1, checkbox=checkbox, graph_layout=graph_layout, graph_widget=graph_widget, is_fastestlap=self.is_fastestlap.isChecked(), lap_number=self.lap_number.value())
        if checkbox.isChecked():
            window_title = "Loading graphs"
            message = "Loading graph for {}".format(checkbox.text())
        else:
            window_title = "Removing graphs"
            message = "removing graph for {}".format(checkbox.text())
        self._connect_loading_signals(signals=load_f1_graph.signals, window_title=window_title, window_message=message, only_statusbar=True)
        load_f1_graph.signals.signal.connect(self._update_graph)
        load_f1_graph.signals.replot.connect(self._replot_graph)
        self.pool.start(load_f1_graph)

    def _update_graph(self, obj):
        obj["graph"].plot(obj["x"], obj["y"], label=obj["label"], color=obj["color"])
        obj["graph"].legend(loc='upper right')

    def _replot_graph(self, obj):
        obj["graph_canvas"].replot()

    def _update_f1_object(self, f1):
        #print("Updated F1 object")
        self.f1 = f1["f1"]

        if self.f1 is not None:
            # Update session select
            if f1["init_session"]:
                #print("Updating session")
                self._init_session_select()
            # Update drivers select
            if f1["init_drivers"]:
                #print("Updating drivers")
                self._init_drivers_select()
        self.lap_number.setMaximum(int(self.f1.get_max_laps()))
        self.lap_number.setMinimum(int(1))

    def _init_season_select(self):
        self.season_select.addItems(str(i) for i in np.arange(2022, get_current_season()+1).tolist())
        self.season_select.setCurrentText(str(get_current_season()))
        self.season_select.currentIndexChanged.connect(self._season_select_changed)
    
    def _season_select_changed(self, index):
        self._init_circuit_select(int(self.season_select.currentText()))

    def _init_circuit_select(self, year=get_current_season()):
        self.circuit_select.clear()
        circuits = F1tel.get_schedule_by_season(year)["Location"].to_list()

        self.circuit_select.addItems(circuits)
        self.circuit_select.setCurrentText(circuits[len(circuits)-1])
        self.circuit_select.currentIndexChanged.connect(self._circuit_select_changed)
    
    def _circuit_select_changed(self, index):
        self._load_f1_object(season=int(self.season_select.currentText()), circuit=self.circuit_select.currentText(), session="FP1", init_drivers=False)

    def _init_session_select(self):
        schedule = self.f1.get_schedule_by_circuit()
        self.session_select.clear()
        for i in range(1, 6):
            if "Session"+str(i) in schedule and schedule["Session"+str(i)] != "" and schedule["Session"+str(i)] != None and schedule["Session"+str(i)+"Date"] <= pd.Timestamp.now():
                self.session_select.addItem(schedule["Session"+str(i)])
        #self.session_select.setCurrentText(self.session_select.itemText(self.session_select.count()-1))
        self.session_select.currentIndexChanged.connect(self._session_select_changed)
    
    def _session_select_changed(self, index):
        self._load_f1_object(int(self.season_select.currentText()), self.circuit_select.currentText(), self.session_select.currentText(), init_session=False)

    def _init_drivers_select(self):

        
        self.lap_number.setMaximum(int(self.f1.get_max_laps()))
        self.lap_number.setMinimum(int(1))

        # Make empty list of drivers
        while self.drivers_list.count():
            item = self.drivers_list.takeAt(0)
            widget = item.widget()
            widget.deleteLater()
        # Populate list with drivers
        for i, driver in enumerate(self.f1.get_drivers_by_session()):
            checkbox = QCheckBox(driver)
            self.drivers_list.addWidget(checkbox, 0 ,i)
            checkbox.clicked.connect(self._drivers_select_changed)

        for graph_canvas in self._graph_containers:
            graph_canvas["canvas"].clear()
            for graph in graph_canvas["graphs"]:
                graph_canvas["canvas"].add_subgraph(position=graph["position"], data_x=[], data_y=[], sharex=graph["sharex"], graphName=graph["graphName"])

    def _update_graphs_after_lap_number_changed(self):
        #print("Updating graphs after lap number changed")
        for i in range(self.drivers_list.count()):
            item = self.drivers_list.itemAt(i)
            checkbox = item.widget()
            if checkbox.isChecked():
                #print("Updating graph for driver: " + checkbox.text())
                for graph_canvas in self._graph_containers:
                    self._print_f1_graph(checkbox=checkbox, graph_layout=graph_canvas["graphs"], graph_widget=graph_canvas["canvas"])

    def _drivers_select_changed(self, item):
        checkbox = self.sender()
        
        for graph_canvas in self._graph_containers:
            self._print_f1_graph(checkbox=checkbox, graph_layout=graph_canvas["graphs"], graph_widget=graph_canvas["canvas"])

    def _connect_loading_signals(self, signals, window_title="Loading...", window_message="Loading...", display_on_statusbar=True, only_statusbar=False):
        if not only_statusbar:
            dialog = LoadingDialog(parent=self, window_title=window_title, text=window_message)
            signals.started.connect(dialog.exec)
            signals.finished.connect(dialog.hide)
        signals.error.connect(self._show_error_dialog)
        if display_on_statusbar or only_statusbar:
            self.statusbar.showMessage(window_message)
            signals.finished.connect(lambda: self.statusbar.showMessage(""))

    def _show_error_dialog(self, error):
        error_dialog = ErrorDialog(parent=self, window_title=error["title"], text=error["message"])
        res=error_dialog.exec()
        if res:
            sys.exit(1)