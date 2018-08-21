#!/usr/bin/python

import sqlite3
from passlib.hash import sha256_crypt
conn = sqlite3.connect('test.db')
email='dummy@mail.com'
password1='12345'
password = sha256_crypt.encrypt(password1)
cursor = conn.execute('SELECT * FROM user WHERE email=(?) AND password=(?)',(email,password,))
results = cursor.fetchall()
print(results)
conn.close()
