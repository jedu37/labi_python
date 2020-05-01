import sqlite3 as sql
import sys

def main(argv):
    if len(argv) < 2:
        print("Usage: python3 {} dbfile".format(argv[0]))
        sys.exit(0)
    
    db = sql.connect(argv[1])

    c = 0

    result = db.execute("SELECT * FROM contacts")
    while True:
        row = result.fetchone()
        if not row:
            break;
        print(row[1])
        c += 1
    print("%d contactos"%(c))

    db.close() 


if __name__ == "__main__":
    main(sys.argv)
