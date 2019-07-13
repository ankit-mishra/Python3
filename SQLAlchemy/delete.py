from sqlalchemy import create_engine,Table, Column, Integer, String, MetaData

meta = MetaData()
engine = create_engine('sqlite:///./local.db')
con = engine.connect()
students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)

s = students.delete().where(students.c.lastname == 'Khanna')

result = con.execute(s)
 
con.execute(s)
s = students.select()
con.execute(s).fetchall()