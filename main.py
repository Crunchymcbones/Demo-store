import sys

from PyQt6 import uic
from PyQt6.QtWidgets import *
import winsound

from controller import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('easy-cheese.ui', self)
        self.initializeCheckoutWindow()
        self.initializeInventory()
        self.initializeAllProductsTable()

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
        # Edit Product
        self.invPnameCbo = self.findChild(QComboBox, 'invPnameCbo')
        self.pidLineEdit = self.findChild(QLineEdit, 'pidLineEdit')
        self.pnameLineEdit = self.findChild(QLineEdit, 'pnameLineEdit')
        self.pdescLineEdit = self.findChild(QLineEdit, 'pdescLineEdit')
        self.ppriceLineEdit = self.findChild(QLineEdit, 'ppriceLineEdit')
        self.pqtyLineEdit = self.findChild(QLineEdit, 'pqtyLineEdit')
        self.vidLineEdit = self.findChild(QLineEdit, 'vidLineEdit')
        self.peditBtn = self.findChild(QPushButton, 'peditBtn')
        self.pdelBtn = self.findChild(QPushButton, 'pdelBtn')

        # Table
        self.invTbl = self.findChild(QTableWidget, 'invTbl')

        # Add Product
        self.apnameLineEdit = self.findChild(QLineEdit, 'apnameLineEdit')
        self.apdescLineEdit = self.findChild(QLineEdit, 'apdescLineEdit')
        self.appriceLineEdit = self.findChild(QLineEdit, 'appriceLineEdit')
        self.apqtyLineEdit = self.findChild(QLineEdit, 'apqtyLineEdit')
        self.avidLineEdit = self.findChild(QLineEdit, 'avidLineEdit')
        self.aaddProductBtn = self.findChild(QPushButton, 'aaddProductBtn')
        self.aaddProductBtn.clicked.connect(self.aaddProductBtnClickHandler)

        colNames, rows = getProductIdsAndNames()
        print(colNames, rows)
        for row in rows:
            self.invPnameCbo.addItem(row[1], userData=row[0])
        self.invPnameCbo.currentIndexChanged.connect(self.productInfoCurrentIndexChangedHandler)
        self.refreshProductComboBox()


    def refreshProductTable(self):
        colNames, data = getAllProducts()
        self.displayDataInTable(colNames, data, self.invTbl)


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
        pid = self.pidLineEdit.text()
        name = self.pnameLineEdit.text()
        desc = self.pdescLineEdit.text()
        price = self.ppriceLineEdit.text()
        pqty = self.pqtyLineEdit.text()
        vid = self.vidLineEdit.text()

        result = updateProduct(pid, name, desc, vid, pqty, price)
        if result == 1:
            print('Big PP')
        else:
            print('Small PP')

    def pdelBtnClickHandler(self):
        try:
            name = self.pnameLineEdit.text()
            msg = QMessageBox(self)
            msg.setWindowTitle("Delete Confirmation")
            msg.setText(f"Are you sure you want to delete {name}")
            msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            msg.setIcon(QMessageBox.Icon.Question)
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            button = msg.exec()
            if button == QMessageBox.StandardButton.Yes:
                pid = self.pidLineEdit.text()
                result = deleteProductById(pid)
                if result == 1:
                    self.refreshStudentTab()
                    self.refreshUpdateStudent()
                else:
                    print('Skill issue')
            elif button == QMessageBox.StandardButton.No:
                print('Your a weiner')


        except Exception as e:
            if "1451 (23000): " in str(e):
                self.lblModifyStuFeedback.setText('First Delete Enrollments')

    def aaddProductBtnClickHandler(self):
        pname = self.apnameLineEdit.text()
        assert pname != "", "Product name is mandatory"
        pdesc = self.apdescLineEdit.text()
        assert pdesc != "", "Product description is mandatory"
        pprice = self.appriceLineEdit.text()
        assert pprice != "", "Product price is mandatory"
        pqty = self.apqtyLineEdit.text()
        assert pqty != "", "Product quantity is mandatory"
        vid = self.avidLineEdit.text()
        assert vid != "", "Vendor ID is mandatory"

        result = addProduct(pname, pdesc, vid, pqty, pprice)

        if result == 1:
            print('You have big PP')
        else:
            print('You have small PP')

    def displayDataInTable(self, columns, rows, table: QTableWidget):
        table.setRowCount(len(rows))
        table.setColumnCount(len(columns))
        for i in range(len(rows)):
            row = rows[i]
            for j in range(len(row)):
                table.setItem(i, j, QTableWidgetItem(str(row[j])))
        columns = ['pid', 'name', 'desc', 'vid', 'qty', 'price']
        for i in range(table.columnCount()):
            table.setHorizontalHeaderItem(i, QTableWidgetItem(f'{columns[i]}'))

    def refreshProductComboBox(self):
        try:
            pID = self.invPnameCbo.currentData()
            info = getProductNameByID(pID)
            print("info", info)
            self.pidLineEdit.setText(str(info['prod_id']))
            self.pnameLineEdit.setText(info['name'])
            self.pdescLineEdit.setText(info['desc'])
            self.ppriceLineEdit.setText(str(info['price']))
            self.pqtyLineEdit.setText(str(info['qty']))
            self.vidLineEdit.setText(str(info['vid']))
        except Exception as e:
            print(e)

    def productInfoCurrentIndexChangedHandler(self):
        self.refreshProductComboBox()

    def initializeAllProductsTable(self):
        self.invTbl = self.findChild(QTableWidget, 'invTbl')
        colNames, data = getAllProducts()
        self.displayDataInTable(colNames, data, self.invTbl)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
