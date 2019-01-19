import sqlite3

with sqlite3.connect("accounts.db") as connection:
    c = connection.cursor()
    c.execute('CREATE TABLE accounts(firstName TEXT, lastName TEXT, email TEXT, groupName TEXT)')

    c.execute('INSERT INTO accounts VALUES("Ram", "Muthukumaran", "rammk1999@gmail.com", "group")')
    c.execute('INSERT INTO accounts VALUES("David", "Terp", "dterp@gmail.com", "group1")')

with sqlite3.connect("items.db") as connection2:
    c2 = connection2.cursor()
    c2.execute('CREATE TABLE items(groupID INTEGER, description TEXT, requester INTEGER, p1 INTEGER, p2 INTEGER, p3 INTEGER, p4 INTEGER, completer INTEGER, chore BLOB, item BLOB, date TEXT)')

    c2.execute('INSERT INTO items VALUES(1234, "description", 0825, 0825, 0942, 0239, 0125, 0825, "chore", "item", "date")')

with sqlite3.connect("users.db") as connection3:
    c3 = connection3.cursor()
    c3.execute('CREATE TABLE users(groupID INTEGER, userID INTEGER, balance REAL, owed REAL)')

    c3.execute('INSERT INTO users VALUES(1234,4321,124.123,5123.293)')
