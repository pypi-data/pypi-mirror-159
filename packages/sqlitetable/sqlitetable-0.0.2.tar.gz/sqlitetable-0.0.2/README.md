# SqliteTable

Use sqlite just like classes!

## Create Table
```python
from sqlitetable import SqliteTable
class Student(SqliteTable):
    uid:int
    name:str
Student.create_table('test.db')
```
The above code creates the following table
```sql
CREATE TABLE "student"(
    "uid" INTEGER,
    "name" TEXT
);
```

## Simple Insert
```python
s = Student()
s.uid = 10001
s.name = 'Hu Tao'
s.sqlite_insert()
```
The above code runs
```sql
INSERT INTO "student" ("uid", "name") VALUES (10001, 'Hu Tao');
```

## Simple Select
```python
s = Student()
s.name = 'Hu Tao'
for e in s.sqlite_select():
    print(e, e.uid, e.name)
```
The above code runs
```sql
SELECT "uid" FROM "student" WHERE "name"='Hu Tao';
```