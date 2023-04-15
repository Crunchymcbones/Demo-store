import sys

from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import csv
import datetime

from controller import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('easy-cheese.ui', self)
        self.initializeCheckoutWindow()
        self.initializeInventory()
        self.initializeAllProductsTable()
        self.initializeCustomers()
        self.initializeManager()
        self.intializeLogin()

        self.initializeInvoicesTable()

    def intializeLogin(self):
        self.cashId = self.findChild(QLineEdit, 'cashId')
        self.cashPass = self.findChild(QLineEdit, 'cashPass')
        self.cashLoginBtn = self.findChild(QPushButton, 'cashLoginBtn')
        self.cashLoginBtn.clicked.connect(self.cashLoginBtnClickedHandler)
        self.cashLoginFeedback = self.findChild(QLabel, 'cashLoginFeedback')
        self.tab = self.findChild(QWidget, 'tab')
        self.tab_2 = self.findChild(QWidget, 'tab_2')
        self.tab_3 = self.findChild(QWidget, 'tab_3')
        self.tab_4 = self.findChild(QWidget, 'tab_4')
        self.tab_5 = self.findChild(QWidget, 'tab_5')
        self.tab_6 = self.findChild(QWidget, 'tab_6')
        self.tab.setEnabled(False)
        self.tab_2.setEnabled(False)
        self.tab_3.setEnabled(False)
        self.tab_4.setEnabled(False)
        self.tab_6.setEnabled(True)

    def cashLoginBtnClickedHandler(self):
        if self.cashId.text() == '' or self.cashPass.text() == '':
            msg = QMessageBox(self)
            msg.setWindowTitle("Error")
            msg.setText(f"Please enter your login information.")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setIcon(QMessageBox.Icon.Question)
            button = msg.exec()
        else:
            ID = int(self.cashId.text())
            password = self.cashPass.text().replace('-', '')
            colnames, rows = getCashierInfo()
            for row in rows:
                if ID == row[0]:
                    if password == row[1]:
                        self.cashLoginFeedback.setText('Login successful')
                        if row[2] == 1:
                            self.tab.setEnabled(True)
                            self.tab_2.setEnabled(True)
                            self.tab_3.setEnabled(True)
                            self.tab_4.setEnabled(True)
                            self.tab_5.setEnabled(True)
                            self.tab_6.setEnabled(False)
                        elif row[2] == 0:
                            self.tab.setEnabled(True)
                            self.tab_2.setEnabled(True)
                            self.tab_3.setEnabled(True)
                            self.tab_4.setEnabled(False)
                            self.tab_6.setEnabled(False)
                    else:
                        self.cashLoginFeedback.setText('Incorrect username or password.')

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

        self.ecCboCustomer_2 = self.findChild(QComboBox, 'ecCboCustomer_2')
        self.eccidLineEdit_2 = self.findChild(QLineEdit, 'eccidLineEdit_2')
        self.ecfnameLineEdit_2 = self.findChild(QLineEdit, 'ecfnameLineEdit_2')
        self.eclnameLineEdit_2 = self.findChild(QLineEdit, 'eclnameLineEdit_2')
        self.ecaddressLineEdit_2 = self.findChild(QLineEdit, 'ecaddressLineEdit_2')
        self.ecemailLineEdit_2 = self.findChild(QLineEdit, 'ecemailLineEdit_2')
        self.ecphoneLineEdit_2 = self.findChild(QLineEdit, 'ecphoneLineEdit_2')

        # Random
        self.vsvFileRdo = self.findChild(QRadioButton, 'vsvFileRdo')

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

        colNames1, rows1 = getCustomerIdAndName()
        print(colNames1, rows1)
        for row in rows1:
            self.ecCboCustomer_2.addItem(row[1], userData=row[0])
        self.ecCboCustomer_2.currentIndexChanged.connect(self.customerInfoCurrentIndexChangedHandler)
        self.refreshCustomerComboBox()

    def addToTableBtnClickedHandler(self):
        rowPosition = self.coTbl.rowCount()
        pID = self.coProdNameCbo.currentData()
        info = getProductNameByID(pID)
        qty = self.coQtyBO.value()

        matching_items = self.coTbl.findItems(info['name'], Qt.MatchFlag.MatchContains)
        if matching_items:
            for row in range(rowPosition):
                item = self.coTbl.item(row, 0).text()
                if info['name'] == item:
                    product_quantity = int(self.coTbl.item(row, 1).text())
                    new_product_quantity = product_quantity + qty
                    if new_product_quantity > info['qty']:
                        msg = QMessageBox(self)
                        msg.setWindowTitle("Error")
                        msg.setText(f"You cannot purchase this amount of {item}... Please try again.")
                        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                        msg.setIcon(QMessageBox.Icon.Question)
                        button = msg.exec()
                        self.refreshCheckoutComboBox()
                    else:
                        self.coTbl.setItem(row, 1, QTableWidgetItem(str(new_product_quantity)))
                        product_total = new_product_quantity * info['price']
                        self.coTbl.setItem(row, 2, QTableWidgetItem(str(product_total)))
        else:
            if qty <= 0:
                msg = QMessageBox(self)
                msg.setWindowTitle("Error")
                msg.setText(f"You cannot purchase {info['name']} as it is out of stock.")
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.setIcon(QMessageBox.Icon.Question)
                button = msg.exec()
            else:
                self.coTbl.insertRow(rowPosition)
                self.coTbl.setColumnCount(3)

                product_total = qty * info['price']

                self.coTbl.setItem(rowPosition, 0, QTableWidgetItem(info['name']))
                self.coTbl.setItem(rowPosition, 1, QTableWidgetItem(str(qty)))
                self.coTbl.setItem(rowPosition, 2, QTableWidgetItem(str(product_total)))

        self.get_total()

    def get_total(self):
        rowPosition = self.coTbl.rowCount()
        overall_total = 0
        qtyPrice = []

        for i in range(rowPosition):
            qtyPrice.append([self.coTbl.item(i, 0).text(), self.coTbl.item(i, 2).text()])

        for i in qtyPrice:
            overall_total += float(i[1])

        self.lblCoTotal.setText(str(round(overall_total, 2)))

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

        # Random
        self.invTbl = self.findChild(QTableWidget, 'invTbl')
        self.rdoOutOfStock = self.findChild(QRadioButton, 'rdoOutOfStock')
        self.rdoOutOfStock.toggled.connect(self.initializeAllProductsTable)
        self.activeCustomersCbo = self.findChild(QComboBox, 'activeCustomersCbo')
        self.activeCustomersCbo.currentIndexChanged.connect(self.initializeActiveCustomerTable)

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
        if self.rdoOutOfStock.isChecked():
            colNames, data = getAllProductsQtyZero()
            self.displayDataInTable(colNames, data, self.invTbl)
        else:
            colNames, data = getAllProducts()
            self.displayDataInTable(colNames, data, self.invTbl)

    def coDeleteBtnClickHandler(self):
        qtyPrice = []
        overall_total = 0

        self.coTbl.removeRow(self.coTbl.currentRow())
        for i in range(self.coTbl.rowCount()):
            qtyPrice.append([self.coTbl.item(i, 0).text(), self.coTbl.item(i, 2).text()])

        for i in qtyPrice:
            overall_total += float(i[1])
        self.lblCoTotal.setText(str(round(overall_total, 2)))

        print('Item Deleted')

    def coCOnfirmClickHandler(self):
        rowPosition = self.coTbl.rowCount()
        information = []
        cid = self.eccidLineEdit_2.text()
        self.createInvoiceAndLineItems(int(cid))

        for row in range(rowPosition):
            name = self.coTbl.item(row, 0).text()
            qty = self.coTbl.item(row, 1).text()
            in_store_qty = getProductQtyByName(name)[1][0][1]
            pid = getProductQtyByName(name)[1][0][0]
            updated_qty = int(in_store_qty) - int(qty)
            information.append({pid: updated_qty})
        result = removeInStoreQuantity(information)
        if result == 1:
            for row in range(rowPosition):
                name = self.coTbl.item(row, 0).text()
                qty = self.coTbl.item(row, 1).text()
                invoice_id = getInvoiceId()[1][0][0]
                product_id = getProductQtyByName(name)[1][0][0]
                insertIntoLineItems(int(invoice_id), int(product_id), int(qty))
            self.refreshProductTable()
            self.refreshProductComboBox()
            self.coTbl.clear()
            self.coTbl.setRowCount(0)
            self.coTbl.setColumnCount(3)
            self.coTbl.setHorizontalHeaderItem(0, QTableWidgetItem(f'Product Name'))
            self.coTbl.setHorizontalHeaderItem(1, QTableWidgetItem(f'Product Quantity'))
            self.coTbl.setHorizontalHeaderItem(2, QTableWidgetItem(f'Product Price'))
            self.lblCoTotal.setText(str((0)))
            self.refreshInvoiceTable()

            csvData = getLastInvoice()
            print(csvData)

            self.createNewInvoiceCSV(csvData)

    def createInvoiceAndLineItems(self, cid):
        createInvoice(cid)

    def peditBtnClickHandler(self):
        if self.pnameLineEdit.text() == '' or self.pdescLineEdit.text() == '' or self.ppriceLineEdit.text() == '' or self.pqtyLineEdit.text() == '' or self.vidLineEdit.text() == '':
            msg = QMessageBox(self)
            msg.setWindowTitle("Error")
            msg.setText(f"Please enter the product information.")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setIcon(QMessageBox.Icon.Question)
            button = msg.exec()
        else:
            try:
                pid = self.pidLineEdit.text()
                name = self.pnameLineEdit.text()
                assert name != "", 'Product name is mandatory... Please try again.'
                assert name != int or float, 'Product name has to be a string... Please try again.'
                desc = self.pdescLineEdit.text()
                assert desc != "", 'Product description is mandatory... Please try again.'
                assert desc != int or float, 'Product description has to be a string... Please try again.'
                price = self.ppriceLineEdit.text()
                assert price != str or int, 'Product price has to be a float... Please try again.'
                assert price != "", 'Product price is mandatory... Please try again.'
                pqty = self.pqtyLineEdit.text()
                assert pqty != str, 'Product quantity has to be an integer... Please try again.'
                assert pqty != "", 'Product quantity is mandatory... Please try again.'
                vid = self.vidLineEdit.text()
                assert vid != str, 'Vendor ID has to be an integer... Please try again.'
                assert vid != "", 'Vendor ID is mandatory... Please try again.'

                result = updateProduct(pid, name, desc, vid, pqty, price)
                if result == 1:
                    self.refreshProductTable()
                    self.refreshProductComboBox()
                    self.refreshCheckoutComboBox()
                    self.lblEditDeleteProd.setText('Product edited successfully!')
                    self.invPnameCbo.clear()
                    self.coProdNameCbo.clear()
                    colNames, rows = getProductIdsAndNames()
                    for row in rows:
                        self.invPnameCbo.addItem(row[1], userData=row[0])
                    self.invPnameCbo.currentIndexChanged.connect(self.productInfoCurrentIndexChangedHandler)
                    self.refreshProductComboBox()

                    colNames1, rows1 = getProductIdsAndNames()
                    for row in rows1:
                        self.coProdNameCbo.addItem(row[1], userData=row[0])
                    self.coProdNameCbo.currentIndexChanged.connect(self.checkInfoCurrentIndexChangedHandler)
                    self.refreshCheckoutComboBox()


                else:
                    self.lblEditDeleteProd.setText('Product could not be edited... Please try again.')


            except AssertionError as ae:
                self.lblEditDeleteProd.setText(f"{ae}")

    def pdelBtnClickHandler(self):
        try:
            name = self.pnameLineEdit.text()
            msg = QMessageBox(self)
            msg.setWindowTitle("Delete Confirmation")
            msg.setText(f"Are you sure you want to delete {name}")
            msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            msg.setIcon(QMessageBox.Icon.Question)
            button = msg.exec()
            if button == QMessageBox.StandardButton.Yes:
                pid = self.pidLineEdit.text()
                result = deleteProduct(pid)
                if result == 1:
                    self.lblEditDeleteProd.setText('Product deleted successfully!')
                    self.refreshCheckoutComboBox()
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
        try:
            if self.apnameLineEdit.text() == '' or self.apdescLineEdit.text() == '' or self.appriceLineEdit.text() == '' or self.apqtyLineEdit.text() == '' or self.avidLineEdit.text() == '':
                msg = QMessageBox(self)
                msg.setWindowTitle("Error")
                msg.setText(f"Please enter the product information.")
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.setIcon(QMessageBox.Icon.Question)
                button = msg.exec()
            else:
                pname = self.apnameLineEdit.text()
                assert pname != "", "Product name is mandatory"
                assert pname != int or float, 'Product name has to be a string... Please try again.'
                pdesc = self.apdescLineEdit.text()
                assert pdesc != "", "Product description is mandatory"
                assert pdesc != int or float, 'Product description has to be a string... Please try again.'
                pprice = self.appriceLineEdit.text()
                assert pprice != "", "Product price is mandatory"
                assert pprice != str, 'Product price has to be a float. Please try again.'
                pqty = self.apqtyLineEdit.text()
                assert pqty != "", "Product quantity is mandatory"
                assert pqty != str, 'Product quantity has to be an int... Please try again.'
                vid = self.avidLineEdit.text()
                assert vid != "", "Vendor ID is mandatory"
                assert vid != str, 'Vendor ID has to be an int... Please try again.'

                result = addProduct(pname, pdesc, vid, pqty, pprice)

                if result == 1:
                    self.refreshProductTable()
                    self.refreshProductComboBox()
                    self.lblAddProd.setText('Product added successfully!')
                    colNames, rows = getLastProduct()
                    print(colNames, rows)
                    for row in rows:
                        self.invPnameCbo.addItem(row[1], userData=row[0])
                        self.coProdNameCbo.addItem(row[1], userData=row[0])
                else:
                    self.lblAddProd.setText('Product could not be added... Please try again.')
        except AssertionError as ae:
            self.lblAddProd.setText(f"{ae}")

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
            self.coQtyBO.setValue(0)
            self.coQtyBO.setMinimum(1)
            self.coQtyBO.setMaximum(info['qty'])
        except Exception as e:
            print(e)

    def productInfoCurrentIndexChangedHandler(self):
        self.refreshProductComboBox()

    def checkInfoCurrentIndexChangedHandler(self):
        self.refreshCheckoutComboBox()

    def customerInfoCurrentIndexChangedHandler(self):
        self.refreshCustomerComboBox()

    def initializeAllProductsTable(self):
        if self.rdoOutOfStock.isChecked():
            self.invTbl = self.findChild(QTableWidget, 'invTbl')
            colNames, data = getAllProductsQtyZero()
            self.displayDataInTable(colNames, data, self.invTbl)
        else:
            self.invTbl = self.findChild(QTableWidget, 'invTbl')
            colNames, data = getAllProducts()
            self.displayDataInTable(colNames, data, self.invTbl)

    def initializeActiveCustomerTable(self):
        try:
            self.activeTableWidget_2 = self.findChild(QTableWidget, 'activeTableWidget_2')

            if self.activeCustomersCbo.currentText == 'Select':
                msg = QMessageBox(self)
                msg.setWindowTitle("Error")
                msg.setText(f"Please select an option.")
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.setIcon(QMessageBox.Icon.Question)
                msg.exec()

            elif self.activeCustomersCbo.currentText() == 'All Customers':
                colNames, data = getAllCustomers()
                self.displayActiveCustomersInTable(colNames, data, self.activeTableWidget_2)

            elif self.activeCustomersCbo.currentText() == '1 Month':
                colNames, data = getActiveCustomers(1)
                self.displayActiveCustomersInTable(colNames, data, self.activeTableWidget_2)

            elif self.activeCustomersCbo.currentText() == '3 Months':
                colNames, data = getActiveCustomers(3)
                self.displayActiveCustomersInTable(colNames, data, self.activeTableWidget_2)

            elif self.activeCustomersCbo.currentText() == '6 Months':
                colNames, data = getActiveCustomers(6)
                self.displayActiveCustomersInTable(colNames, data, self.activeTableWidget_2)

            elif self.activeCustomersCbo.currentText() == '9 Months':
                colNames, data = getActiveCustomers(9)
                self.displayActiveCustomersInTable(colNames, data, self.activeTableWidget_2)

        except IndexError as ie:
            # I have no idea why it is spitting this error out, but it still works
            pass

    def initializeCustomers(self):
        self.acfnameLineEdit = self.findChild(QLineEdit, 'acfnameLineEdit')
        self.aclnameLineEdit = self.findChild(QLineEdit, 'aclnameLineEdit')
        self.acaddressLineEdit = self.findChild(QLineEdit, 'acaddressLineEdit')
        self.acemailLineEdit = self.findChild(QLineEdit, 'acemailLineEdit')
        self.acphoneLineEdit = self.findChild(QLineEdit, 'acphoneLineEdit')
        self.acBtn = self.findChild(QPushButton, 'acBtn')
        self.acBtn.clicked.connect(self.acBtnClickHandler)
        self.acLabel = self.findChild(QLabel, 'acLabel')

        self.ecCboCustomer = self.findChild(QComboBox, 'ecCboCustomer')
        self.eccidLineEdit = self.findChild(QLineEdit, 'eccidLineEdit')
        self.ecfnameLineEdit = self.findChild(QLineEdit, 'ecfnameLineEdit')
        self.eclnameLineEdit = self.findChild(QLineEdit, 'eclnameLineEdit')
        self.ecaddressLineEdit = self.findChild(QLineEdit, 'ecaddressLineEdit')
        self.ecemailLineEdit = self.findChild(QLineEdit, 'ecemailLineEdit')
        self.ecphoneLineEdit = self.findChild(QLineEdit, 'ecphoneLineEdit')
        self.ecBtn = self.findChild(QPushButton, 'ecBtn')
        self.ecBtn.clicked.connect(self.ecBtnClickHandler)
        self.ecLabel = self.findChild(QLabel, 'ecLabel')

        colNames, rows = getCustomerIdAndName()
        print(colNames, rows)
        for row in rows:
            self.ecCboCustomer.addItem(row[1], userData=row[0])
        self.ecCboCustomer.currentIndexChanged.connect(self.customerInfoCurrentIndexChangedHandler)
        self.refreshCustomerComboBox()

    def initializeManager(self):
        self.initializeInvoicesTable()

    def acBtnClickHandler(self):
        try:
            fname = self.acfnameLineEdit.text()
            assert fname != "", 'First name is mandatory... Please try again.'
            assert fname != int or float, 'First name has to be a string... Please try again.'
            lname = self.aclnameLineEdit.text()
            assert lname != "", 'Last name is mandatory... Please try again.'
            assert lname != int or float, 'Last name has to be a string... Please try again.'
            address = self.acaddressLineEdit.text()
            email = self.acemailLineEdit.text()
            assert email != "", 'Email is mandatory... Please try again.'
            assert email != int or float, 'Email has to be a string... Please try again.'
            phone = self.acphoneLineEdit.text()
            assert phone != "", 'Phone number is mandatory... Please try again.'
            assert phone != int or float, 'Phone number has to be a string... Please try again.'
            result = addCustomer(fname, lname, address, email, phone)
            if result == 1:
                self.acLabel.setText('Customer added')
                self.refreshCustomersTab()
                colNames, rows = getLastCustomer()
                print(colNames, rows)
                for row in rows:
                    self.ecCboCustomer_2.addItem(row[1], userData=row[0])
                    self.ecCboCustomer.addItem(row[1], userData=row[0])
            else:
                self.acLabel.setText('Customer not added')

        except AssertionError as ae:
            self.acLabel.setText(str(ae))

    def ecBtnClickHandler(self):
        try:

            cid = self.eccidLineEdit.text()
            fname = self.ecfnameLineEdit.text()
            assert fname != "", 'First name is mandatory... Please try again.'
            assert fname != int or float, 'First name has to be a string... Please try again.'
            lname = self.eclnameLineEdit.text()
            assert lname != "", 'Last name is mandatory... Please try again.'
            assert lname != int or float, 'Last name has to be a string... Please try again.'
            address = self.ecaddressLineEdit.text()
            email = self.ecemailLineEdit.text()
            assert email != "", 'Email is mandatory... Please try again.'
            assert email != int or float, 'Email has to be a string... Please try again.'
            phone = self.ecphoneLineEdit.text()
            assert phone != "", 'Phone number is mandatory... Please try again.'
            assert phone != int or float, 'Phone number has to be a string... Please try again.'
            result = editCustomer(cid, fname, lname, address, email, phone)
            if result == 1:
                self.ecLabel.setText('Customer updated')
                self.ecCboCustomer_2.clear()
                self.ecCboCustomer.clear()
                colNames, rows = getCustomerIdAndName()
                print(colNames, rows)
                for row in rows:
                    self.ecCboCustomer_2.addItem(row[1], userData=row[0])
                    self.ecCboCustomer.addItem(row[1], userData=row[0])
            else:
                self.ecLabel.setText('Customer not updated')
        except AssertionError as ae:
            self.ecLabel.setText(str(ae))

        self.refreshCustomersTab()

    def refreshCustomersTab(self):
        self.acfnameLineEdit.clear()
        self.aclnameLineEdit.clear()
        self.acaddressLineEdit.clear()
        self.acemailLineEdit.clear()
        self.acphoneLineEdit.clear()

    def initializeInvoicesTable(self):
        self.invoicesTableWidget_2 = self.findChild(QTableWidget, 'invoicesTableWidget_2')
        self.invoicesTableWidget = self.findChild(QTableWidget, 'invoicesTableWidget')
        self.getLineItemsBtn = self.findChild(QPushButton, 'getLineItemsBtn')
        self.getLineItemsBtn.clicked.connect(self.invoiceLineItemsClickedHandler)

        colNames, data = getInvoices()
        self.displayInvoiceDataInTable(colNames, data, self.invoicesTableWidget)

    def refreshInvoiceTable(self):
        colNames, data = getInvoices()
        self.displayInvoiceDataInTable(colNames, data, self.invoicesTableWidget)

    def invoiceLineItemsClickedHandler(self):
        row = self.invoicesTableWidget.currentRow()
        if row == -1:
            msg = QMessageBox(self)
            msg.setWindowTitle("Error")
            msg.setText(f"Please select an invoice.")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setIcon(QMessageBox.Icon.Question)
            button = msg.exec()
        else:
            item = self.invoicesTableWidget.item(row, 0).text()
            self.displayLineItemsInTable(item)

    def displayInvoiceDataInTable(self, columns, rows, table: QTableWidget):
        table.setRowCount(len(rows))
        table.setColumnCount(len(columns))
        for i in range(len(rows)):
            row = rows[i]
            for j in range(len(row)):
                table.setItem(i, j, QTableWidgetItem(str(row[j])))
        columns = ['Invoice_ID', 'Name', 'email', 'pnumber', 'date', 'item total', 'inv tax', 'inv total',
                   'qty purchased']
        for i in range(table.columnCount()):
            table.setHorizontalHeaderItem(i, QTableWidgetItem(f'{columns[i]}'))

    def displayActiveCustomersInTable(self, columns, rows, table: QTableWidget):
        table.setRowCount(len(rows))
        table.setColumnCount(len(columns))
        for i in range(len(rows)):
            row = rows[i]
            for j in range(len(row)):
                table.setItem(i, j, QTableWidgetItem(str(row[j])))
        columns = ['customer_id', 'name', 'address', 'email', 'phone_number', 'date']
        for i in range(table.columnCount()):
            table.setHorizontalHeaderItem(i, QTableWidgetItem(f'{columns[i]}'))

    def displayLineItemsInTable(self, iid):
        self.invoicesTableWidget_2.clear()
        self.invoicesTableWidget_2.setRowCount(0)
        self.invoicesTableWidget_2.setColumnCount(3)
        self.invoicesTableWidget_2.setHorizontalHeaderItem(0, QTableWidgetItem(f'Product_name'))
        self.invoicesTableWidget_2.setHorizontalHeaderItem(1, QTableWidgetItem(f'Product_qty'))
        self.invoicesTableWidget_2.setHorizontalHeaderItem(2, QTableWidgetItem(f'Product_total'))
        info = getInvoiceLineItems(iid)
        rowPosition = self.invoicesTableWidget_2.rowCount()
        for i in range(len(info)):
            self.invoicesTableWidget_2.insertRow(rowPosition)
            self.invoicesTableWidget_2.setItem(rowPosition, 0, QTableWidgetItem(info[i][0]))
            self.invoicesTableWidget_2.setItem(rowPosition, 1, QTableWidgetItem(str(info[i][1])))
            self.invoicesTableWidget_2.setItem(rowPosition, 2, QTableWidgetItem(str(info[i][2])))

    def refreshCustomerComboBox(self):
        try:
            cid = self.ecCboCustomer.currentData()
            info = getCustomerNameByID(cid)
            self.eccidLineEdit.setText(str(info['cust_id']))
            self.ecfnameLineEdit.setText(info['fname'])
            self.eclnameLineEdit.setText(info['lname'])
            self.ecaddressLineEdit.setText(info['address'])
            self.ecemailLineEdit.setText(info['email'])
            self.ecphoneLineEdit.setText(info['phone_number'])

            cid1 = self.ecCboCustomer_2.currentData()
            info1 = getCustomerNameByID(cid1)
            self.eccidLineEdit_2.setText(str(info1['cust_id']))
            self.ecfnameLineEdit_2.setText(info1['fname'])
            self.eclnameLineEdit_2.setText(info1['lname'])
            self.ecaddressLineEdit_2.setText(info1['address'])
            self.ecemailLineEdit_2.setText(info1['email'])
            self.ecphoneLineEdit_2.setText(info1['phone_number'])
        except Exception as e:
            print(e)

    def createNewInvoiceCSV(self,data):
        """Creates a new Invoice CSV file with a header row and single data row
        Args:
            row (tuple): Row of data to store in new CSV file
        """
        if self.vsvFileRdo.isChecked():
            header = ['invoice_id', 'name', 'email_address', 'phone_number', 'item_total', 'invoice_tax', 'invoice_total',
                      'items_purchased']
            # Generates a unique file name with the date and time - Replace is used to avoid having files with : as some os will not enjoy
            uniq_filename = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':',
                                                                                                                    '.') + ".csv"

            # Opens and writes to a new CSV file
            with open(uniq_filename, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerow(data)
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
