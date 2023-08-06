import json
import jsonschema
from jsonschema import validate
from typing import Union
from PyQt5.QtCore import pyqtSignal, QThread, QRunnable, QObject
from PyQt5.QtWidgets import QCheckBox

from f1tel_gui.F1tel import F1tel
from f1tel_gui.windows.MplCanvas import MplCanvas
from f1tel_gui.utils import get_json_layout_path


class Signal(QObject):
    started = pyqtSignal()
    signal = pyqtSignal(object)
    finished = pyqtSignal()
    error = pyqtSignal(object)
    replot = pyqtSignal(object)

class LoadF1Obj(QRunnable):

    def __init__(self, season: Union[str, int], circuit: str, session: str, disable_cache: bool = False, parent=None, update_session: bool = True, update_drivers: bool = True):
        super().__init__()
        self.is_running = True
        self.season = int(season)
        self.circuit = circuit
        self.session = session
        self.disable_cache = disable_cache
        self.update_session_value = update_session
        self.update_drivers_value = update_drivers
        self.f1 = None
        self.signals = Signal()

    def run(self):
        self.signals.started.emit()
        try:
            self.f1 = F1tel(self.season, self.circuit,
                            self.session, self.disable_cache)
            
            self.signals.signal.emit(
                {"f1": self.f1, "init_session": self.update_session_value, "init_drivers": self.update_drivers_value})
            self.signals.finished.emit()
        except Exception as e:
            self.signals.error.emit({"title": "Error Loading F1 session", "message": e})

    def stop(self):
        self.is_running = False
        self.terminate()


class LoadF1Graph(QRunnable):

    def __init__(self, parent=None, f1: F1tel = None, checkbox: QCheckBox = None, graph_layout: list = None, graph_widget: MplCanvas = None, is_fastestlap: bool = False, lap_number: int = 1):
        super().__init__()
        self.is_running = True
        self.f1 = f1
        self.checkbox = checkbox
        self.graph_layout = graph_layout
        self.graph_widget = graph_widget
        self.is_fastestlap = is_fastestlap
        self.lap_number = lap_number
        self.signals = Signal()

    def run(self):
        try:
            self.signals.started.emit()
            driver_tel = self.f1.get_driver_telemetry(
                self.checkbox.text(), self.is_fastestlap, self.lap_number)
            for graph in self.graph_layout:
                curr_graph = self.graph_widget.get_graph(graph["graphName"])
                handles, labels = curr_graph.get_legend_handles_labels()
                if not driver_tel.empty:
                    if self.checkbox.isChecked():
                        # If line already exists, remove it
                        if self.checkbox.text() in labels:
                            label_index = labels.index(self.checkbox.text())
                            curr_graph.axes.lines[label_index+1].remove()
                        #curr_graph.plot(driver_tel[graph["xlabel"]], driver_tel[graph["ylabel"]], label=self.checkbox.text(), color=self.f1.get_driver_color(self.checkbox.text()))
                        self.signals.signal.emit({"graph": curr_graph, "x": driver_tel[graph["xlabel"]], "y": driver_tel[graph["ylabel"]], "label": self.checkbox.text(), "color": self.f1.get_driver_color(self.checkbox.text())})
                    else:
                        if self.checkbox.text() in labels:
                            label_index = labels.index(self.checkbox.text())
                            curr_graph.axes.lines[label_index+1].remove()
                else:
                    if self.checkbox.text() in labels:
                        label_index = labels.index(self.checkbox.text())
                        curr_graph.axes.lines[label_index+1].remove()

                if len(curr_graph.lines) > 0:
                    curr_graph.legend(loc='upper right')
                curr_graph.set_xlabel(graph["xlabel"])
                curr_graph.set_ylabel(graph["ylabel"])

            #self.graph_widget.replot()
            self.signals.replot.emit({"graph_canvas":self.graph_widget})
            self.signals.finished.emit()
        except Exception as e:
            self.signals.error.emit({"title": "Error Printing Graph", "message": e})

    def stop(self):
        self.is_running = False
        self.terminate()


class LoadF1GraphLayout(QRunnable):

    json_schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "array",
        "items": [
            {
                "type": "object",
                "properties": {
                    "tabname": {
                        "type": "string"
                    },
                    "graphs": {
                        "type": "array",
                        "items": [
                            {
                                "type": "object",
                                "properties": {
                                    "position": {
                                        "type": "integer"
                                    },
                                    "sharex": {
                                        "type": "boolean"
                                    },
                                    "graphName": {
                                        "type": "string"
                                    },
                                    "xlabel": {
                                        "type": "string"
                                    },
                                    "ylabel": {
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "position",
                                    "sharex",
                                    "graphName",
                                    "xlabel",
                                    "ylabel"
                                ]
                            }
                        ]
                    }
                },
                "required": [
                    "tabname",
                    "graphs"
                ]
            }
        ]
    }

    def __init__(self, parent=None, layout_file_path: str = get_json_layout_path()):
        super().__init__()
        self.is_running = True
        self.path_file = layout_file_path
        self.signals = Signal()

    def run(self):
        try:
            self.signals.started.emit()
            with open(self.path_file) as f:
                json_data = json.load(f)
                if self._validate_json(json_data):
                    self.signals.signal.emit(json_data)
                else:
                    self.signals.error.emit({"title": "Error Validating JSON", "message": "Invalid JSON file"})
            self.signals.finished.emit()
        except Exception as e:
            self.signals.error.emit({"title": "Error Loading Json Schema", "message": e})

    def _validate_json(self, json_data) -> bool:
        try:
            validate(json_data, self.json_schema)
            return True
        except jsonschema.ValidationError as e:
            #print("Validation error: {}".format(e))
            return False

    def stop(self):
        self.is_running = False
        self.terminate()
