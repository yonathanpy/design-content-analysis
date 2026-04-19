def extract_tables(cursor):
    cursor.execute(
        "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'field_data%';"
    )
    return [x[2] for x in cursor]
