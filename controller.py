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

def getProductNameByID(pid):
    """
    Retrieves product information for the given product ID from the database.

    Args:
    pid (int): The ID of the product to retrieve information for.

    Returns:
    dict: A dictionary containing the product ID, name, description, vendor ID, quantity, and price.
    """
    sql = f"SELECT * from `easy_cheese`.`products` where product_id = {pid}"
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

def removeInStoreQuantity(pid, new_qty_value):
    sql = f"UPDATE `easy_cheese`.`products` SET in_store_qty = {new_qty_value} where product_id = {pid};"
    return executeQueryAndCommit(sql)

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
    sql = f"select * from `easy_cheese`.`invoices`;"
    return executeQueryAndReturnResult(sql)

def getActiveCustomers():
    sql = f"SELECT customer_id, date FROM easy_cheese.invoices where date >= date_sub(now(), Interval 1 month);"
    return executeQueryAndReturnResult(sql)

def getOutOfStock():
    sql = f"SELECT * FROM easy_cheese.products where in_store_qty = 0;"
    return executeQueryAndReturnResult(sql)

def getCustomerIdAndName():
    sql = f"SELECT customer_id, concat(first_name, ' ', last_name) from `easy_cheese`.`customers`"
    return executeQueryAndReturnResult(sql)

def getCustomerNameByID(cid):
    sql = f"SELECT * from `easy_cheese`.`customers` where customer_id = {cid}"
    custInfo = executeQueryAndReturnResult(sql)[1][0]
    data = {'cust_id': custInfo[0], 'fname': custInfo[1], 'lname': custInfo[2], 'address': custInfo[3], 'email': custInfo[4], 'phone_number': custInfo[5]}
    return data

