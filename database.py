import sqlite3 as s

connection = s.connect("customers.db")

cursor = connection.execute("select * from info")

data = list(cursor.fetchall())

connection.close()


def select(iban):
    connection = s.connect("customers.db")

    cursor = connection.execute("select * from info where iban = '%s'" % iban)

    data = cursor.fetchall()

    connection.close()

    return data




def update_customer(guncellenecek_alan, yeni_deger, kriter):
    connection = s.connect("customers.db")

    connection.execute("update info set " + guncellenecek_alan + " = " + str(yeni_deger) + " where id = " + str(kriter))

    connection.commit()
    connection.close()