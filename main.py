from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUiType
import subprocess
import sys
import os

from src.modules.borderText import *


PROJECT_DIR = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(__file__)
UI_MainWindow_PATH = os.path.join(PROJECT_DIR, 'ui', 'printWithBorder.ui')

Ui_MainWindow, QMainWindowBase = loadUiType(UI_MainWindow_PATH)

class Ui_MainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self):
    super().__init__()

    self.output_file_path = "./output/output.txt"

    self.setupUi(self)

    self.convertButton.clicked.connect(self.convertText)
    
    self.openInNotepadButton.setHidden(True)
    self.openInNotepadButton.clicked.connect(self.openInNotepad)

  def getText(self):
        # return list
        return self.textField.toPlainText().split('\n')

  def convertText(self):
      listText = self.getText()
      bt = borderText(listText)
      bt.draw()
      bt.saveText(self.output_file_path)
      self.openInNotepadButton.setHidden(False)
  
  def openInNotepad(self):
    subprocess.run(["notepad.exe", self.output_file_path])

if __name__ =='__main__':
  app = QApplication([])
  window = Ui_MainWindow()
  window.show()
  app.exec_()