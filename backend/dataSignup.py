import psycopg2

def addClient(userName, password, email, company):
    conn = psycopg2.connect(host="localhost", dbname="E-Hub", user="postgres", password="sbskln2412S", port=5432)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute('select * from client')
    rows=cur.fetchall()
    num=0
    for row in rows:
        temp=row[0]
        temp=int(temp[3:])
        if(num<temp):
            num=temp+1
    num=str(num)
    while(len(num)<3):
        num='0'+num
    id='CLI'+num
    cur.execute(f"insert into person values(\'{id}\', \'{userName}\', \'{email}\')")
    cur.execute(f"insert into login values(\'{id}\', \'{userName}\', \'{password}\', \'{email}\')")
    cur.execute(f"insert into client values(\'{id}\', \'{company}\', \'{0}\')")
    cur.close()
    conn.close()
    