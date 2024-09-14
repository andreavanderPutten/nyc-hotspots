from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNodi(provider):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct n.Location as localita 
from `nyc-hotspots`.nyc_wifi_hotspot_locations n
where n.Provider = %s"""

        cursor.execute(query,(provider,) )

        for row in cursor:
            result.append(row["localita"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getProvider():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct n.Provider as provider 
from `nyc-hotspots`.nyc_wifi_hotspot_locations n
order by Provider asc"""

        cursor.execute(query, )

        for row in cursor:
            result.append(row["provider"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(loc,provider):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select sum(n.Latitude)/count(n.Latitude) as latitudine, sum(n.Longitude)/count(n.Longitude) as longitudine
from `nyc-hotspots`.nyc_wifi_hotspot_locations n
where n.Location = %s 
and n.Provider = %s
group by n.Location"""

        cursor.execute(query, (loc,provider))

        for row in cursor:
            result.append((float(row["latitudine"]),float(row["longitudine"])))

        cursor.close()
        conn.close()
        return result
