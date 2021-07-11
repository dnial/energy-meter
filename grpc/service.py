import sqlite3
import meter_pb2 as pb2
from google.protobuf.timestamp_pb2 import Timestamp


DB_NAME = "measurement.db"

def get_measurement(start, end):
    print(f"get_measurement from {start} to {end}")
    con = create_connection(DB_NAME)
    cur = con.cursor()

    query = """SELECT id, time, meter FROM  meterusage WHERE time >= ? AND time <= ?"""

    cur.execute(query, (start, end))

    rows = cur.fetchall()

    result = []
    for row in rows:
        time_ts = Timestamp()
        time_ts.seconds = row[1]
        try:
            data = pb2.Meter(time=time_ts, value=row[2])
            result.append(data)
        except Exception as ex:
            print(f'get_measurement Exception: {ex}')
    
    return result


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    con = None
    try:
        con = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return con
