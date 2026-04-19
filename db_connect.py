import MySQLdb as mdb

def connect(host, user, password, database):
    return mdb.connect(host, user, password, database)
