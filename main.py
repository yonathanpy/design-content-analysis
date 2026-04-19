from core import connect_db, load_data, table_statistics


def run():
    host = input("Host: ")
    user = input("User: ")
    password = input("Password: ")
    database = input("Database: ")

    try:
        conn = connect_db(host, user, password, database)
    except Exception as e:
        print("Connection failed:", e)
        return

    data = load_data(conn)

    print("\nCommands: list | search <word> | stats <table> | show <table> | quit\n")

    while True:
        cmd = input("> ").strip().split()

        if not cmd:
            continue

        action = cmd[0]

        if action == "quit":
            break

        elif action == "list":
            print(list(data.keys()))

        elif action == "search" and len(cmd) > 1:
            term = cmd[1]
            results = [k for k in data if term in k]
            print(results)

        elif action == "stats" and len(cmd) > 1:
            table = cmd[1]
            full = next((k for k in data if table in k), None)

            if full:
                print(table_statistics(data[full]))
            else:
                print("Not found")

        elif action == "show" and len(cmd) > 1:
            table = cmd[1]
            full = next((k for k in data if table in k), None)

            if full:
                print(data[full][:10])
            else:
                print("Not found")

        else:
            print("Invalid command")


if __name__ == "__main__":
    run()
