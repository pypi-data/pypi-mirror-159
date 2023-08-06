from . import PYTHON_TYPE_SQLITE, ColumnInfo
from re import sub

def camel_cased_to_underlined(name:str) -> str:
    """ 驼峰转下划线 """
    return sub(r'([a-z])([A-Z])', r'\1_\2', name).lower()

def class_to_sql(cls:type, table:str) -> str:
    """ 从类cls中获取数据表列信息并生产创建该数据表table的sql语句 """
    # 列sql容器
    cols:list[str] = []
    # PRIMARY KEY容器
    pks:list[str] = []
    # 遍历类注解，获取列信息
    for n, t in cls.__annotations__.items():
        # 提取类变量名作为列名、类变量注解作为列类型
        v = getattr(cls, n, ColumnInfo(name=n, type=PYTHON_TYPE_SQLITE[t]))
        # 当类变量的值不是ColumnInfo时将该值作为列的默认取值
        if not isinstance(v, ColumnInfo):
            v = ColumnInfo(name=n, type=PYTHON_TYPE_SQLITE[t], dflt_value='NULL' if v is None else str(v))
        # 转换类变量值为UNUSED
        setattr(cls, n, v)
        # 组装列sql
        cols.append(f'"{v.name}" {v.type}{" NOT NULL" if v.notnull else ""}{f" DEFAULT {v.dflt_value}" if v.dflt_value is not None else ""}')
        # 记录PRIMARY KEY
        if v.pk:
            pks.append(f'"{v.name}"')
    # 组装sql语句
    return f'''CREATE TABLE IF NOT EXISTS "{table}"({",".join(cols)}{f',CONSTRAINT "pk_{table}" PRIMARY KEY ({",".join(pks)})' if pks else ""});'''
