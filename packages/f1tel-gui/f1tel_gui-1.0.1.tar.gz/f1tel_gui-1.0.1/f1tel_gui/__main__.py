import sys
import argparse

from PyQt5.QtWidgets import QApplication
import qdarkstyle

from fastf1.plotting import setup_mpl

from f1tel_gui.windows.main import MainWindow
from f1tel_gui.windows.jsoneditor.JSONitor import JSONitorWindow as JsonEditor
setup_mpl()

parser = argparse.ArgumentParser(description='Plot driver data')
parser.add_argument('-e',  action='store_true', help='Open the JSON editor')
parser.add_argument('--json_layout',  type=str, default="graph_layout.json", help='JSON graph layout file')

args = parser.parse_args()



parser.parse_args(['-e'])

#Create the application
app = QApplication([])
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

if not args.e:
    if args.json_layout:
        win = MainWindow(graph_layout_path=args.json_layout)
    else:
        win = MainWindow()
    
else:
    win = JsonEditor()

win.showMaximized()
# Run the application's main loop
sys.exit(app.exec())