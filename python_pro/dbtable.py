import pymysql
conn=pymysql.connect(user='root',password='root',port=3306,database='pythonmysql')
cursor=conn.cursor()
def create_table():
    try:
        query = '''
        create table customer(
        id int primary key,
        name varchar(100),
        mobile bigint unique,
        balance bigint
        );
        '''
        cursor



































def drop_record(cid):
    query=f'delete from customer where id={cid}'
    cursor.execute(query)
    con.commit()
    print('record removed')

