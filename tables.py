import sqlite3

conn = sqlite3.connect('clients.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS registration (
    first_name text, 
    surname text, 
    age integer, 
    location text, 
    phone_no integer, 
    email text)""")

c.execute("INSERT INTO registration(first_name, surname, age, location, phone_no, email) VALUES"(
    'prince', 'naveen', 23, 'london', 25789654, 'naveen@gmail.com')
)

conn.commit()
conn.close()

