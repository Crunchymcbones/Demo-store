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
    """
    Retrieves all products from the database with in-store quantity equal to zero.

    Returns:
        list: A list of dictionaries, where each dictionary contains the following product information:
            - product_id (int): The ID of the product.
            - name (str): The name of the product.
            - in_store_qty (int): The in-store quantity of the product.
            - price (float): The price of the product.
    """
    sql = f"SELECT * FROM `easy_cheese`.`products` WHERE in_store_qty = 0;"
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


def removeInStoreQuantity(data):
    """
    Removes quantity from in-store quantity for products in the database.

    Args:
        data (list): A list of dictionaries, where each dictionary contains the following keys:
            - product_id (int): The ID of the product.
            - quantity (int): The quantity to be removed from the in-store quantity.

    Returns:
        bool: True if the update was successful, False otherwise.
    """
    def removeInStoreQuantity(dict):
        for i in dict:
            for key, value in i.items():
                sql = f"UPDATE `easy_cheese`.`products` SET in_store_qty = {value} where product_id = {key};"
                executeQueryAndCommit(sql)
    return True


def getProductQtyByName(product_name):
    """
    Retrieves product ID and in-store quantity for a given product name from the database.

    Args:
        product_name (str): The name of the product.

    Returns:
        list: A list of tuples, each containing the following product information:
            - product_id (int): The ID of the product.
            - in_store_qty (int): The in-store quantity of the product.
    """
    sql = f"SELECT product_id, in_store_qty FROM `easy_cheese`.`products` WHERE name = '{product_name}';"
    return executeQueryAndReturnResult(sql)


def addCustomer(fname, lname, address, email, phone):
    """
    Adds a new customer to the database.

    Args:
        fname (str): The first name of the customer.
        lname (str): The last name of the customer.
        address (str): The address of the customer.
        email (str): The email address of the customer.
        phone (str): The phone number of the customer.

    Returns:
        bool: True if the customer was added successfully, False otherwise.
    """
    sql = f"INSERT INTO `easy_cheese`.`customers` (`first_name`, `last_name`, `address`, `email_address`, `phone_number`) VALUES ('{fname}', '{lname}', '{address}', '{email}', '{phone}');"
    return executeQueryAndCommit(sql)


def editCustomer(cid, fname, lname, address, email, phone):
    """
    Edits an existing customer in the database.

    Args:
        cid (int): The customer ID.
        fname (str): The first name of the customer.
        lname (str): The last name of the customer.
        address (str): The address of the customer.
        email (str): The email address of the customer.
        phone (str): The phone number of the customer.

    Returns:
        bool: True if the customer was edited successfully, False otherwise.
    """
    sql = f"UPDATE `easy_cheese`.`customers` SET `first_name` = '{fname}', `last_name` = '{lname}', `address` = '{address}', `email_address` = '{email}', `phone_number` = '{phone}' WHERE (`customer_id` = '{cid}');"
    return executeQueryAndCommit(sql)


def getInvoices():
    """
    Retrieves information about all invoices from the database.

    Returns:
        list: A list of tuples, each containing information about an invoice.
    """
    sql = f"SELECT * FROM `easy_cheese`.`complete_invoice`;"
    return executeQueryAndReturnResult(sql)


def getActiveCustomers(months):
    """
    Retrieves information about active customers based on the number of months since their last purchase.

    Args:
        months (int): The number of months since the last purchase.

    Returns:
        list: A list of tuples, each containing information about an active customer.
    """
    sql = f"CALL `easy_cheese`.`active_customers`({months});"
    return executeQueryAndReturnResult(sql)


def getAllCustomers():
    """
    Retrieves information about all customers from the database.

    Returns:
        list: A list of tuples, each containing the following customer information:
            - customer_id (int): The customer ID.
            - name (str): The name of the customer.
            - address (str): The address of the customer.
            - email_address (str): The email address of the customer.
            - phone_number (str): The phone number of the customer.
    """
    sql = f"""
        SELECT c.customer_id, CONCAT(c.first_name, ' ', c.last_name) AS name, c.address, c.email_address, c.phone_number
        FROM easy_cheese.customers c
        GROUP BY c.customer_id, c.address, c.email_address, c.phone_number;
    """
    return executeQueryAndReturnResult(sql)


def getCustomerIdAndName():
    """
    Retrieves customer ID and name information for all customers from the database.

    Returns:
        list: A list of tuples, each containing the following customer information:
            - customer_id (int): The customer ID.
            - name (str): The name of the customer.
    """
    sql = f"SELECT customer_id, CONCAT(first_name, ' ', last_name) FROM `easy_cheese`.`customers`;"
    return executeQueryAndReturnResult(sql)


def getLastCustomer():
    """
    Retrieves information about the last customer from the database.

    Returns:
        tuple: A tuple containing the customer ID and the name of the customer.
    """
    sql = f"""
        SELECT customer_id, CONCAT(first_name, ' ', last_name)
        FROM `easy_cheese`.`customers`
        ORDER BY customer_id DESC
        LIMIT 1;
    """
    return executeQueryAndReturnResult(sql)


def getCustomerNameByID(cid):
    """
    Retrieves information about a customer by their customer ID.

    Args:
        cid (int): The customer ID.

    Returns:
        dict: A dictionary containing the following customer information:
            - cust_id (int): The customer ID.
            - fname (str): The first name of the customer.
            - lname (str): The last name of the customer.
            - address (str): The address of the customer.
            - email (str): The email address of the customer.
            - phone_number (str): The phone number of the customer.
    """
    sql = f"""
        SELECT *
        FROM `easy_cheese`.`customers`
        WHERE customer_id = {cid};
    """
    custInfo = executeQueryAndReturnResult(sql)[1][0]
    data = {
        'cust_id': custInfo[0],
        'fname': custInfo[1],
        'lname': custInfo[2],
        'address': custInfo[3],
        'email': custInfo[4],
        'phone_number': custInfo[5]
    }
    return data


def getInvoiceLineItems(iid):
    """
    Retrieves information about line items in an invoice by invoice ID.

    Args:
        iid (int): The invoice ID.

    Returns:
        list: A list of tuples, each containing the following information:
            - product_id (int): The product ID of the line item.
            - product_name (str): The name of the product.
            - qty (int): The quantity of the product.
            - price (float): The price of the product.
    """
    sql = f"CALL easy_cheese.name_qty_price({iid});"
    return executeQueryAndReturnResult(sql)[1]


def createInvoice(cid):
    """
    Creates a new invoice for a customer in the database.

    Args:
        cid (int): The customer ID for which the invoice is created.

    Returns:
        int: The invoice ID of the newly created invoice.
    """
    sql = f"INSERT INTO `easy_cheese`.`invoices` (customer_id, date) VALUES({cid}, NOW());"
    return executeQueryAndCommit(sql)


def getInvoiceId():
    """
    Retrieves the invoice_id of the latest invoice from the 'invoices' table in the 'easy_cheese' database.

    Returns:
    - A tuple containing:
        - column_names (list): A list of column names returned by the query.
        - rows (list of tuples): A list of tuples, where each tuple represents a row returned by the query.
    """
    sql = f"select invoice_id from `easy_cheese`.`invoices` order by invoice_id desc limit 1;"
    return executeQueryAndReturnResult(sql)


def insertIntoLineItems(invoice_id, product_id, qty):
    """
    Inserts a new record into the 'invoice_line_items' table in the 'easy_cheese' database.

    Args:
    - invoice_id (int): The invoice ID to which the line item belongs.
    - product_id (int): The product ID of the item.
    - qty (int): The quantity of the item.

    Returns:
    - The number of rows affected by the query.
    """
    sql = f"insert into `easy_cheese`.`invoice_line_items`(invoice_id, product_id, qty) VALUES({invoice_id}, {product_id}, {qty});"
    return executeQueryAndCommit(sql)


def getCashierInfo():
    """
    Retrieves all records from the 'cashiers' table in the 'easy_cheese' database.

    Returns:
    - A tuple containing:
        - column_names (list): A list of column names returned by the query.
        - rows (list of tuples): A list of tuples, where each tuple represents a row returned by the query.
    """
    sql = f"select * from `easy_cheese`.`cashiers`;"
    return executeQueryAndReturnResult(sql)


def getLastInvoice():
    """
    Retrieves information about the last invoice from the database.

    Returns:
        tuple: A tuple containing the following information:
            - invoice_id (int): The invoice ID.
            - name (str): The name of the customer associated with the invoice.
            - email_address (str): The email address of the customer.
            - phone_number (str): The phone number of the customer.
            - date (str): The date of the invoice.
            - item total (float): The total cost of all items in the invoice.
            - invoice tax (float): The tax amount applied to the invoice.
            - invoice total (float): The total cost of the invoice including tax.
            - items purchased (int): The total number of items purchased in the invoice.
    """
    sql = f"    SELECT \
        `i`.`invoice_id` AS `invoice_id`, \
        CONCAT(`c`.`first_name`, ' ', `c`.`last_name`) AS `name`, \
        `c`.`email_address` AS `email_address`, \
        `c`.`phone_number` AS `phone_number`, \
        `i`.`date` AS `date`, \
        SUM((`li`.`qty` * `p`.`price`)) AS `item total`, \
        ROUND((SUM((`li`.`qty` * `p`.`price`)) * 0.15), \
                2) AS `invoice tax`, \
        ROUND((SUM((`li`.`qty` * `p`.`price`)) * 1.15), \
                2) AS `invoice total`, \
        SUM(`li`.`qty`) AS `items purchased` \
    FROM \
        (((`easy_cheese`.`invoices` `i` \
        JOIN `easy_cheese`.`customers` `c` ON ((`i`.`customer_id` = `c`.`customer_id`))) \
        JOIN `easy_cheese`.`invoice_line_items` `li` ON ((`i`.`invoice_id` = `li`.`invoice_id`))) \
        JOIN `easy_cheese`.`products` `p` ON ((`li`.`product_id` = `p`.`product_id`))) \
    GROUP BY `i`.`invoice_id`\
	order by i.invoice_id desc limit 1;"
 
    csvInfo = executeQueryAndReturnResult(sql)[1][0]
    data = (csvInfo[0], csvInfo[1], csvInfo[2], csvInfo[3], csvInfo[5], csvInfo[6], csvInfo[7], csvInfo[8])
    return data