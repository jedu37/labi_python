import sqlite3 as sql
import sys

def main(argv):
    if len(argv) < 3:
        print("Usage: python3 {} dbfile name".format(argv[0]))
        sys.exit(0)
    
    db = sql.connect(argv[1])

    c = 0

    result = db.execute("SELECT * FROM contacts WHERE firstname LIKE ? OR middlename LIKE ? OR lastname LIKE ?",(argv[2],argv[2],argv[2],))
    while True:
        row = result.fetchone()
        if not row:
            break;
        company = db.execute("SELECT * FROM companies WHERE id LIKE ?",(row[6],))
        print("{} {} {} trabalha na empresa {}".format(row[1],row[2],row[3],company.fetchone()[1]))
        c += 1
    print("%d contactos"%(c))

    db.close() 


if __name__ == "__main__":
    main(sys.argv)