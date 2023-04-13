from mysql_functions import *

def addProduct(pname, pdesc, vid, pqty, pprice):
    """
    Adds a new product to the database with the given information.

    Args:
    pname (str): The name of the new product.
    pdesc (str): The description of the new product.
    vid (int): The ID of the vendor associated with the new product.
    pqty (int): The quantity of the new product.
    pprice (float): The price of the new product.

    Returns:
    bool: True if the addition was successful, False otherwise.
    """
    sql = f"INSERT INTO `easy_cheese`.`products` (`name`, `product_desc`, `vendor_id`, `in_store_qty`, `price`) VALUES ('{pname}', '{pdesc}', '{vid}', '{pqty}', '{pprice}');"
    return executeQueryAndCommit(sql)

def getAllProducts():
    """
    Retrieves all products from the database.

    Returns:
    list: A list of tuples containing information for each product in the database, including the product ID, name, description, vendor ID, quantity, and price.
    """
    sql = f"select * from `easy_cheese`.`products`;"
    return executeQueryAndReturnResult(sql)

def getAllProductsQtyZero():
    sql = f"select * from `easy_cheese`.`products` where in_store_qty = 0;"
    return executeQueryAndReturnResult(sql)

def getProductNameByID(pid):
    """
    Retrieves product information for the given product ID from the database.

    Args:
    pid (int): The ID of the product to retrieve information for.

    Returns:
    dict: A dictionary containing the product ID, name, description, vendor ID, quantity, and price.
    """
    sql = f"SELECT * from `easy_cheese`.`products` where product_id = {pid};"
    prodInfo = executeQueryAndReturnResult(sql)[1][0]
    data = {'prod_id': prodInfo[0], 'name': prodInfo[1], 'desc': prodInfo[2], 'vid': prodInfo[3], 'qty': prodInfo[4], 'price': prodInfo[5]}
    return data


def getProductIdsAndNames():
    """
    Retrieves the IDs and names of all products from the database.

    Returns:
    list: A list of tuples containing the product ID and name for each product in the database.
    """
    sql = f"select product_id, name from `easy_cheese`.`products`;"
    return executeQueryAndReturnResult(sql)

def getLastProduct():
    """
    Retrieves the IDs and names of all products from the database.

    Returns:
    list: A list of tuples containing the product ID and name for each product in the database.
    """
    sql = f"select product_id, name from `easy_cheese`.`products` order by product_id desc limit 1;"
    return executeQueryAndReturnResult(sql)


def updateProduct(pid, name, desc, vid, qty, price):
    """
    Updates the information for a product with the given ID in the database.

    Args:
    pid (int): The ID of the product to update.
    name (str): The new name of the product.
    desc (str): The new description of the product.
    vid (int): The ID of the vendor associated with the product.
    qty (int): The new quantity of the product.
    price (float): The new price of the product.

    Returns:
    bool: True if the update was successful, False otherwise.
    """
    sql = f"UPDATE `easy_cheese`.`products` SET name = '{name}', product_desc = '{desc}', vendor_id = {vid}, in_store_qty = {qty}, price = {price} where product_id = {pid};"
    return executeQueryAndCommit(sql)

def deleteProduct(pid):
    """
    Deletes the product with the given ID from the database.

    Args:
    pid (int): The ID of the product to delete.

    Returns:
    bool: True if the deletion was successful, False otherwise.
    """
    sql = f"delete from `easy_cheese`.`products` where product_id = {pid};"
    return executeQueryAndCommit(sql)

def removeInStoreQuantity(dict):
    for i in dict:
        for key, value in i.items():
            sql = f"UPDATE `easy_cheese`.`products` SET in_store_qty = {value} where product_id = {key};"
            executeQueryAndCommit(sql)
    return True

def getProductQtyByName(product_name):
    sql = f"select product_id, in_store_qty from `easy_cheese`.`products` where name = '{product_name}';"
    return executeQueryAndReturnResult(sql)

def addCustomer(fname,lname, address, email, phone):
    sql = f"INSERT INTO `easy_cheese`.`customers` (`first_name`, `last_name`, `address`, `email_address`, `phone_number`) VALUES ('{fname}', '{lname}', '{address}', '{email}', '{phone}');"
    return executeQueryAndCommit(sql)

def editCustomer(cid, fname,lname, address, email, phone):
    sql = f"UPDATE `easy_cheese`.`customers` SET `first_name` = '{fname}', `last_name` = '{lname}', `address` = '{address}', `email_address` = '{email}', `phone_number` = '{phone}' WHERE (`customer_id` = '{cid}');"
    return executeQueryAndCommit(sql)

def getInvoices():
    sql = f"SELECT * FROM `easy_cheese`.`complete_invoice`;"
    return executeQueryAndReturnResult(sql)

def getActiveCustomers(months):
    sql = f"call `easy_cheese`.`active_customers`({months});"
    return executeQueryAndReturnResult(sql)

def getAllCustomers():
    sql = f"SELECT c.customer_id,CONCAT(c.first_name, ' ', c.last_name) AS name, c.address, c.email_address, c.phone_number, i.date FROM easy_cheese.customers c JOIN easy_cheese.invoices i on c.customer_id = i.customer_id;"
    return executeQueryAndReturnResult(sql)

def getCustomerIdAndName():
    sql = f"SELECT customer_id, concat(first_name, ' ', last_name) from `easy_cheese`.`customers`;"
    return executeQueryAndReturnResult(sql)

def getLastCustomer():
    sql = f"SELECT customer_id, concat(first_name, ' ', last_name) from `easy_cheese`.`customers` order by customer_id desc limit 1;;"
    return executeQueryAndReturnResult(sql)

def getCustomerNameByID(cid):
    sql = f"SELECT * from `easy_cheese`.`customers` where customer_id = {cid};"
    custInfo = executeQueryAndReturnResult(sql)[1][0]
    data = {'cust_id': custInfo[0], 'fname': custInfo[1], 'lname': custInfo[2], 'address': custInfo[3], 'email': custInfo[4], 'phone_number': custInfo[5]}
    return data

def getInvoiceLineItems(iid):
    sql = f"call easy_cheese.name_qty_price({iid});"
    return executeQueryAndReturnResult(sql)[1]

def createInvoice(cid):
    sql = f"insert into `easy_cheese`.`invoices`(customer_id, date) VALUES({cid}, NOW());"
    return executeQueryAndCommit(sql)

def getInvoiceId():
    sql = f"select invoice_id from `easy_cheese`.`invoices` order by invoice_id desc limit 1;"
    return executeQueryAndReturnResult(sql)

def insertIntoLineItems(invoice_id, product_id, qty):
    sql = f"insert into `easy_cheese`.`invoice_line_items`(invoice_id, product_id, qty) VALUES({invoice_id}, {product_id}, {qty});"
    return executeQueryAndCommit(sql)

def getCashierInfo():
    sql = f"select * from `easy_cheese`.`cashiers`;"
    return executeQueryAndReturnResult(sql)
