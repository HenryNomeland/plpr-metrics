import duckdb
import sys


def execute_sql(connection, script):
    file = open(script, "r")
    content = file.read()
    file.close()
    commands = content.split(";")
    for command in commands:
        print(command)
        connection.sql(command)


if __name__ == "__main__":
    script = sys.argv[1]
    conn = duckdb.connect(".\\pronunciation.db")
    execute_sql(conn, script)
    conn.table("frames").show()
    conn.close()
