from mysql_functions import *

def addProduct(pname, pdesc, vid, pqty, pprice):
    sql = f"INSERT INTO `easy_cheese`.`products` (`name`, `product_desc`, `vendor_id`, `qty`, `price`) VALUES ('{pname}', '{pdesc}', '{vid}', '{pqty}', '{pprice}');"
    return executeQueryAndCommit(sql)


def getAllProducts():
    sql = f"select * from `easy_cheese`.`products`;"
    return executeQueryAndReturnResult(sql)


def getProductNameByID(pid):
    sql = f"select product_id, name from `easy_cheese`.`products` where product_id = {pid}"
    return executeQueryAndReturnResult(sql)


def getProductIdsAndNames():
    sql = f"select product_id, name from `easy_cheese`.`products`;"
    return executeQueryAndReturnResult(sql)