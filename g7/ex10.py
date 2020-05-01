import sqlite3 as sql
import sys

def main(argv):
    if len(argv) < 2:
        print("Usage: python3 {} dbfile".format(argv[0]))
        sys.exit(0)
    
    db = sql.connect(argv[1]) # estabelecer ligação à BD
    # realizar operações sobre a BD

    result = db.execute("SELECT * FROM contacts")
    rows = result.fetchall()
    for row in rows:
        print(row)
    print()

    result = db.execute("SELECT * FROM contacts")
    while True:
        row = result.fetchone()
        if not row:
            break;
        print(row)
    print()

    result = db.execute("SELECT * FROM contacts")
    for row in result:
        print(row)
    print()

    db.close() # terminar ligação


if __name__ == "__main__":
    main(sys.argv)
