#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Verifica que se proporcionen los 3 argumentos esperados
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Conecta al servidor MySQL en localhost:3306
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)

    # Crea un cursor
    cursor = db.cursor()

    # Ejecuta la consulta SQL
    try:
        cursor.execute("SELECT * FROM states ORDER BY id")
    except MySQLdb.Error as e:
        print("Error executing SQL query:", e)
        db.close()
        sys.exit(1)

    # Obtén y muestra los resultados
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Cierra la conexión
    db.close()