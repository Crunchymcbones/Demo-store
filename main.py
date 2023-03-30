import sys

from PyQt6 import uic
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('easy-cheese.ui', self)
        self.initializeCheckoutWindow()


    def initializeCheckoutWindow(self):
        self.coProdNameCbo = self.findChild(QComboBox, 'coProdNameCbo')
        self.coQtyBO = self.findChild(QSpinBox, 'coQtyBO')
        self.coAddBtn = self.findChild(QPushButton, 'coAddBtn')
        self.coUpBtn = self.findChild(QPushButton, 'coUpBtn')
        self.coDownBtn = self.findChild(QPushButton, 'coDownBtn')
        self.coDeleteBtn = self.findChild(QPushButton, 'coDeleteBtn')
        self.coCOnfirmBtn = self.findChild(QPushButton, 'coCOnfirmBtn')
        self.coTbl = self.findChild(QTableWidget, 'coTbl')


    def initializeInventory(self):
        #Edit Product
        self.invPnameCbo = self.findChild(QComboBox, 'invPnameCbo')
        self.pidLineEdit = self.findChild(QLineEdit, 'pidLineEdit')
        self.pnameLineEdit = self.findChild(QLineEdit, 'pnameLineEdit')
        self.pdescLineEdit = self.findChild(QLineEdit, 'pdescLineEdit')
        self.ppriceLineEdit = self.findChild(QLineEdit, 'ppriceLineEdit')
        self.pqtyLineEdit = self.findChild(QLineEdit, 'pqtyLineEdit')
        self.vidLineEdit = self.findChild(QLineEdit, 'vidLineEdit')
        self.peditBtn = self.findChild(QPushButton, 'peditBtn')
        self.pdelBtn = self.findChild(QPushButton, 'pdelBtn')

        #Add Product
        self.apnameLineEdit = self.findChild(QLineEdit, 'apnameLineEdit')
        self.apdescLineEdit = self.findChild(QLineEdit, 'apdescLineEdit')
        self.appriceLineEdit = self.findChild(QLineEdit, 'appriceLineEdit')
        self.apqtyLineEdit = self.findChild(QLineEdit, 'apqtyLineEdit')
        self.avidLineEdit = self.findChild(QLineEdit, 'avidLineEdit')
        self.aaddProductBtn = self.findChild(QPushButton, 'aaddProductBtn')

    def coAddBtnClickHandler(self):
        pass


    def coUpBtnClickHandler(self):
        pass


    def coDownBtnClickHandler(self):
        pass


    def coDeleteBtnClickHandler(self):
        pass


    def coCOnfirmClickHandler(self):
        pass


    def peditBtnClickHandler(self):
        pass


    def pdelBtnClickHandler(self):
        pass


    def aaddProductBtnClickHandler(self)
        pass:








if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
