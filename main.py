import sys

from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
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
        self.lblCoTotal = self.findChild(QLabel, 'lblCoTotal')
        self.coQtyBO = self.findChild(QSpinBox, 'coQtyBO')
        self.coAddBtn = self.findChild(QPushButton, 'coAddBtn')
        self.coAddBtn.clicked.connect(self.addToTableBtnClickedHandler)
        self.coDeleteBtn = self.findChild(QPushButton, 'coDeleteBtn')
        self.coDeleteBtn.clicked.connect(self.coDeleteBtnClickHandler)
        self.coCOnfirmBtn = self.findChild(QPushButton, 'coCOnfirmBtn')
        self.coCOnfirmBtn.clicked.connect(self.coCOnfirmClickHandler)
        self.coTbl = self.findChild(QTableWidget, 'coTbl')
        self.coTbl.setColumnCount(3)
        self.coTbl.setHorizontalHeaderItem(0, QTableWidgetItem(f'Product Name'))
        self.coTbl.setHorizontalHeaderItem(1, QTableWidgetItem(f'Product Quantity'))
        self.coTbl.setHorizontalHeaderItem(2, QTableWidgetItem(f'Product Price'))

        colNames, rows = getProductIdsAndNames()
        print(colNames, rows)
        for row in rows:
            self.coProdNameCbo.addItem(row[1], userData=row[0])
        self.coProdNameCbo.currentIndexChanged.connect(self.checkInfoCurrentIndexChangedHandler)
        self.refreshCheckoutComboBox()

    def addToTableBtnClickedHandler(self):
        rowPosition = self.coTbl.rowCount()
        pID = self.coProdNameCbo.currentData()
        info = getProductNameByID(pID)
        qty = self.coQtyBO.value()

        matching_items = self.coTbl.findItems(info['name'], Qt.MatchFlag.MatchContains)
        if matching_items:
            for column in range(3):
                for row in range(rowPosition):
                    item = self.coTbl.item(row, column).text()
                    if info['name'] == item:
                        product_quantity = int(self.coTbl.item(row, 1).text())
                        new_product_quantity = product_quantity + qty
                        self.coTbl.setItem(row, 1, QTableWidgetItem(str(new_product_quantity)))
        else:
            self.coTbl.insertRow(rowPosition)
            self.coTbl.setColumnCount(3)

            self.coTbl.setItem(rowPosition, 0, QTableWidgetItem(info['name']))
            self.coTbl.setItem(rowPosition, 1, QTableWidgetItem(str(qty)))
            self.coTbl.setItem(rowPosition, 2, QTableWidgetItem(str(info['price'])))


    def initializeInventory(self):
        # Edit Product
        self.invPnameCbo = self.findChild(QComboBox, 'invPnameCbo')
        self.pidLineEdit = self.findChild(QLineEdit, 'pidLineEdit')
        self.pnameLineEdit = self.findChild(QLineEdit, 'pnameLineEdit')
        self.pdescLineEdit = self.findChild(QLineEdit, 'pdescLineEdit')
        self.ppriceLineEdit = self.findChild(QLineEdit, 'ppriceLineEdit')
        self.pqtyLineEdit = self.findChild(QLineEdit, 'pqtyLineEdit')
        self.vidLineEdit = self.findChild(QLineEdit, 'vidLineEdit')
        self.lblEditDeleteProd = self.findChild(QLabel, 'lblEditDeleteProd')
        self.lblAddProd = self.findChild(QLabel, 'lblAddProd')
        self.peditBtn = self.findChild(QPushButton, 'peditBtn')
        self.peditBtn.clicked.connect(self.peditBtnClickHandler)
        self.pdelBtn = self.findChild(QPushButton, 'pdelBtn')
        self.pdelBtn.clicked.connect(self.pdelBtnClickHandler)

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

    def coDeleteBtnClickHandler(self):
        self.coTbl.removeRow(self.coTbl.currentRow())
        print('Item Deleted')

    def coCOnfirmClickHandler(self):
        rowPosition = self.coTbl.rowCount()
        information = []

        for row in range(rowPosition):
            name = self.coTbl.item(row, 0).text()
            qty = self.coTbl.item(row, 1).text()
            information.append({name: qty})
            in_store_qty = getProductQtyByName(name)[1][0][1]
            pid = getProductQtyByName(name)[1][0][0]
            updated_qty = int(in_store_qty) - int(qty)
            print(updated_qty)
            result = removeInStoreQuantity(pid, updated_qty)
            if result == 1:
                self.refreshProductTable()
                self.refreshProductComboBox()
                self.coTbl.clear()
                self.coTbl.setRowCount(0)
                self.coTbl.setColumnCount(3)
                self.coTbl.setHorizontalHeaderItem(0, QTableWidgetItem(f'Product Name'))
                self.coTbl.setHorizontalHeaderItem(1, QTableWidgetItem(f'Product Quantity'))
                self.coTbl.setHorizontalHeaderItem(2, QTableWidgetItem(f'Product Price'))
            print(information)

    def peditBtnClickHandler(self):
        pid = self.pidLineEdit.text()
        name = self.pnameLineEdit.text()
        desc = self.pdescLineEdit.text()
        price = self.ppriceLineEdit.text()
        pqty = self.pqtyLineEdit.text()
        vid = self.vidLineEdit.text()

        result = updateProduct(pid, name, desc, vid, pqty, price)
        if result == 1:
            self.refreshProductTable()
            self.refreshProductComboBox()
            self.lblEditDeleteProd.setText('Product edited successfully!')
        else:
            self.lblEditDeleteProd.setText('Product could not be edited... Please try again.')

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
                result = deleteProduct(pid)
                if result == 1:
                    self.lblEditDeleteProd.setText('Product deleted successfully!')
                    self.refreshProductTable()
                    self.refreshProductComboBox()
                else:
                    self.lblEditDeleteProd.setText('Product could not be deleted... please try again.')
            elif button == QMessageBox.StandardButton.No:
                self.lblEditDeleteProd.setText('Product deletion canceled.')


        except Exception as e:
            if "1451 (23000): " in str(e):
                self.lblEditDeleteProd.setText(e)

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
            self.refreshProductTable()
            self.refreshProductComboBox()
            self.lblAddProd.setText('Product added successfully!')
        else:
            self.lblAddProd.setText('Product could not be added... Please try again.')

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

    def refreshCheckoutComboBox(self):
        try:
            pID = self.coProdNameCbo.currentData()
            info = getProductNameByID(pID)
            print("info", info)
        except Exception as e:
            print(e)

    def productInfoCurrentIndexChangedHandler(self):
        self.refreshProductComboBox()

    def checkInfoCurrentIndexChangedHandler(self):
        self.refreshCheckoutComboBox()

    def initializeAllProductsTable(self):
        self.invTbl = self.findChild(QTableWidget, 'invTbl')
        colNames, data = getAllProducts()
        self.displayDataInTable(colNames, data, self.invTbl)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
