from database.DB_connect import DBConnect
from model.prodotto import Prodotto


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct year(gds.`Date`) as year
    from go_daily_sales gds"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllColors():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct gp.Product_color as color
from go_products gp """

        cursor.execute(query)

        for row in cursor:
            result.append(row["color"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getVertci():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
        from go_products"""

        cursor.execute(query)

        for row in cursor:
            result.append(Prodotto(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getSameDaySales(p1,p2,a):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT COUNT(DISTINCT s1.Date) as N 
                   FROM go_daily_sales s1, go_daily_sales s2
                   WHERE s1.Date = s2.Date
                   AND s1.Retailer_code = s2.Retailer_code
                   AND s1.Product_Number = %s 
                   AND s2.Product_Number = %s
                   AND YEAR(s1.Date) = %s"""

        cursor.execute(query,(p1.Product_number,p2.Product_number,str(a)))

        for row in cursor:
            result.append(row["N"])

        cursor.close()
        conn.close()
        return result



