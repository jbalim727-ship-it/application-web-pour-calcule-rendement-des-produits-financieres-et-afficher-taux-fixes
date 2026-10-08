import sqlite3

connection = sqlite3.connect('produit.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# N-zidou chwaya données bch n-testou bihom
cur.execute("INSERT INTO produits (nom, taux) VALUES (?, ?)", ('Taux Fixe A', 4.5))
cur.execute("INSERT INTO produits (nom, taux) VALUES (?, ?)", ('Taux Fixe B', 5.2))

connection.commit()
connection.close()
print("Base de données créée!")
