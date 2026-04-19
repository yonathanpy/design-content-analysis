import mysql.connector
from html.parser import HTMLParser


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = []

    def handle_data(self, d):
        self.data.append(d)

    def get_data(self):
        return ''.join(self.data)


def strip_tags(html):
    s = MLStripper()
    s.feed(str(html))
    return s.get_data()


def character_count(text):
    return len(text)


def word_count(text):
    return len(text.split())


def mean(data):
    return sum(data) / len(data) if data else 0


def mode(data):
    return max(set(data), key=data.count) if data else 0


def pstdev(data):
    if len(data) < 2:
        return 0
    avg = mean(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)
    return round(variance ** 0.5, 2)


def table_statistics(table_data):
    char_lengths = [character_count(x) for x in table_data]
    word_lengths = [word_count(x) for x in table_data]

    return {
        "Characters": {
            "max": max(char_lengths) if table_data else 0,
            "min": min(char_lengths) if table_data else 0,
            "avg": mean(char_lengths),
            "mode": mode(char_lengths),
            "std": pstdev(char_lengths),
        },
        "Words": {
            "max": max(word_lengths) if table_data else 0,
            "min": min(word_lengths) if table_data else 0,
            "avg": mean(word_lengths),
            "mode": mode(word_lengths),
            "std": pstdev(word_lengths),
        },
    }


def connect_db(host, user, password, database):
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )


def load_data(connection):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'field_data%';"
    )

    tables = [row[0] for row in cursor]
    data = {}

    for table in tables:
        field_name = table.replace("field_data_", "") + "_value"
        query = f"SELECT {field_name} FROM {table}"

        try:
            cursor.execute(query)
            values = [strip_tags(row[0]) for row in cursor if row[0]]
            if values:
                data[table] = values
        except:
            continue

    return data
