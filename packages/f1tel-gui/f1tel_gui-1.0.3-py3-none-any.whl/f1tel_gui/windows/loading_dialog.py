from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

class LoadingDialog(QMessageBox):

    def __init__(self, parent=None, window_title="", text="") -> None:
        super(LoadingDialog, self).__init__(parent)
        self.setWindowTitle(window_title)
            
        self.setText(str(text))
        self.setStandardButtons(QMessageBox.NoButton)
        self.setIcon(QMessageBox.Information)
        self.setWindowModality(Qt.ApplicationModal)
        
        #remove close button
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint & ~Qt.WindowMinimizeButtonHint & ~Qt.WindowMaximizeButtonHint & ~Qt.WindowContextHelpButtonHint)
        self.setEscapeButton(QMessageBox.NoButton)
        self.move(self.frameGeometry().center() - self.rect().center())

    def hide(self):
        self.setVisible(False)
        return super().hide()

class ErrorDialog(QMessageBox):

    def __init__(self, parent=None, window_title="", text="") -> None:
        super(ErrorDialog, self).__init__(parent)
        self.setWindowTitle(window_title)
            
        self.setText(str(text))
        self.setIcon(QMessageBox.Critical)
        self.setWindowModality(Qt.ApplicationModal)
        
        #add ok button
        self.setWindowFlags(self.windowFlags())
        self.setStandardButtons(QMessageBox.Ok)