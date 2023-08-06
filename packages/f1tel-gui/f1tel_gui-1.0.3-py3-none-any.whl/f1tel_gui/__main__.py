import sys
import argparse

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, QT_VERSION_STR
import qdarkstyle

from fastf1.plotting import setup_mpl

from f1tel_gui.windows.main import MainWindow
from f1tel_gui.windows.jsoneditor.JSONitor import JSONitorWindow as JsonEditor
from f1tel_gui.utils import get_json_layout_path, get_img_path

"""import ctypes
myappid = 'developer.f1tel.gui.1_0_0' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
"""

def main():
    setup_mpl()

    parser = argparse.ArgumentParser(description='Plot driver data')
    parser.add_argument('-e',  action='store_true', help='Open the JSON editor')
    parser.add_argument('--json_layout',  type=str, default=get_json_layout_path(), help='JSON graph layout file')

    args = parser.parse_args()



    parser.parse_args(['-e'])

    #Create the application
    app = QApplication([])
    QCoreApplication.setOrganizationName("Developer310301")
    QCoreApplication.setApplicationName("F1 Telemetry")
    QCoreApplication.setApplicationVersion(QT_VERSION_STR)
    app.setWindowIcon(QIcon(get_img_path("logo.jpg")))
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

main()