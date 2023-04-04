from mysql_functions import *

def addProduct(pname, pdesc, vid, pqty, pprice):
    sql = f"INSERT INTO `easy_cheese`.`products` (`name`, `product_desc`, `vendor_id`, `in_store_qty`, `price`) VALUES ('{pname}', '{pdesc}', '{vid}', '{pqty}', '{pprice}');"
    return executeQueryAndCommit(sql)


def getAllProducts():
    sql = f"select * from `easy_cheese`.`products`;"
    return executeQueryAndReturnResult(sql)


def getProductNameByID(pid):
    sql = f"SELECT * from `easy_cheese`.`products` where product_id = {pid}"
    prodInfo = executeQueryAndReturnResult(sql)[1][0]
    print('prodinfo', prodInfo)
    data = {'prod_id': prodInfo[0], 'name': prodInfo[1], 'desc': prodInfo[2], 'vid': prodInfo[3], 'qty': prodInfo[4], 'price': prodInfo[5]}
    print(data)
    return(data)


def getProductIdsAndNames():
    sql = f"select product_id, name from `easy_cheese`.`products`;"
    return executeQueryAndReturnResult(sql)


def updateProduct(pid, name, desc, vid, qty, price):
    sql = f"UPDATE `easy_cheese`.`products` SET name = '{name}', product_desc = '{desc}', vendor_id = {vid}, in_store_qty = {qty}, price = {price} where product_id = {pid};"
    return executeQueryAndCommit(sql)


def deleteProductById(pid):
    sql = f"DELETE FROM `easy_cheese`.`products` where product_id = {pid};"
    return executeQueryAndCommit(sql)