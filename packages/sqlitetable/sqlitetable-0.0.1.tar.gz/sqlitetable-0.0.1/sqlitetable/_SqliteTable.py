from sqlite3 import connect, Connection, Cursor
from . import PYTHON_TYPE_SQLITE, UNUSED, ColumnInfo, camel_cased_to_underlined, class_to_sql

class SqliteTable:
    @classmethod
    def create_table(cls, database:str|Connection, table:str=None, drop:bool=False):
        # 记录默认数据库
        @classmethod
        def sqlite_database(_) -> str|Connection:
            return database
        cls.sqlite_database = sqlite_database
        # 记录数据表的名称
        if table is None:
            table = camel_cased_to_underlined(cls.__name__)
        @classmethod
        def sqlite_table(_) -> str:
            return table
        cls.sqlite_table = sqlite_table
        # 执行数据表的CREATE语句
        is_connection:bool = isinstance(database, Connection)
        connection:Connection  = database if is_connection else connect(database)
        if drop:
            connection.execute(f'DROP TABLE IF EXISTS "{table}";')
        connection.execute(class_to_sql(cls, table))
        connection.commit()
        if not is_connection:
            connection.close()

    @classmethod
    def drop_table(cls, database:str|Connection=None):
        database = cls.sqlite_database() if database is None else database
        # 执行数据表的DROP语句
        is_connection:bool = isinstance(database, Connection)
        connection:Connection  = database if is_connection else connect(database)
        connection.execute(f'DROP TABLE IF EXISTS "{cls.sqlite_table()}";')
        connection.commit()
        if not is_connection:
            connection.close()

    def sqlite_insert(self, database:str|Connection=None) -> int:
        cls = self.__class__
        database = cls.sqlite_database() if database is None else database
        lastrowid:int = None
        # 列名容器
        cols:list[str] = []
        vals:list[str] = []
        # 获取插入的键和值
        for n in cls.__annotations__.keys():
            v = getattr(self, n, UNUSED)
            if v!=UNUSED:
                cols.append(f'"{n}"')
                vals.append(f':{n}')
        # 执行数据表的INSERT语句
        is_connection:bool = isinstance(database, Connection)
        connection:Connection  = database if is_connection else connect(database)
        lastrowid = connection.execute(f'INSERT INTO "{cls.sqlite_table()}" ({",".join(cols)}) VALUES ({",".join(vals)});', self.__dict__).lastrowid
        connection.commit()
        if not is_connection:
            connection.close()
        return lastrowid

    def sqlite_select(self, database:str|Connection=None) -> 'SqliteTable':
        cls = self.__class__
        database = cls.sqlite_database() if database is None else database
        cols:list[str] = []
        # 条件语句容器
        wheres:list[str] = []
        # 获取条件的键和值
        for n in cls.__annotations__.keys():
            v = getattr(self, n, UNUSED)
            if v != UNUSED:
                wheres.append(f'"{n}"=:{n}')
            cols.append(n)
        # 执行数据表的SELECT语句
        is_connection:bool = isinstance(database, Connection)
        connection:Connection  = database if is_connection else connect(database)
        cursor:Cursor = connection.execute(f'''SELECT {",".join((f'"{n}"' for n in cols))} FROM "{cls.sqlite_table()}"{" WHERE " if wheres else ""}{" AND ".join(wheres)};''', self.__dict__)
        for row in cursor:
            obj = cls()
            for n, v in zip(cols, row):
                setattr(obj,n,v)
            yield obj
        if not is_connection:
            connection.close()

    @classmethod
    def sqlite_database(_) -> str|Connection:
        """ 获取创建数据表时使用的数据库 """
        return None

    @classmethod
    def sqlite_table(_) -> str:
        """ 获取创建数据表时使用的数据表名称 """
        return None

