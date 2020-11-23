

from data_inv.db import *


def singup(self):
    print("registro, oh si")
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    d1 = self.ids.singup_User.text
    d2 = self.ids.singup_Email.text
    d3 = self.ids.singup_Pass.text
    a1 = (d1, d2, d3)
    s1 = 'INSERT INTO LOGIN(user_L, email_L, password)'
    s2 = 'VALUES ("%s", "%s", "%s")' % a1
    try:
        cursor.execute(s1 +''+ s2)
        connection.commit()
        connection.close()
        #app.root.current = 'index'
    except Exception as e:
        print('error')
        connection.close()