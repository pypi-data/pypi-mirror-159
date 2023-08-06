from . import PYTHON_TYPE_SQLITE, UNUSED

class ColumnInfo:
    """ 数据表的列信息，对应sql语句 f'pragma table_info("{table}")' 的返回结果 """
    def __init__(self,cid:int = None,name:str = None,type:str = None,notnull:int = 0,dflt_value:None|str = None,pk:int = 0) -> None:
        self.cid:int = cid
        self.name:str = name
        self.type:str = type
        self.notnull:int = notnull
        self.dflt_value:None|str = dflt_value
        self.pk:int = pk

    def __set_name__(self, cls:type, name:str):
        # 提取类变量名作为列名
        if self.name is None:
            self.name = name
        # 提取类变量注解作为列类型
        if self.type is None:
            self.type = PYTHON_TYPE_SQLITE[cls.__annotations__[name]]
    
    def __get__(self, obj:object, cls:type=None) -> any:
        if obj is None:
            return self
        if self.name in obj.__dict__:
            return obj.__dict__[self.name]
        return UNUSED

    def __set__(self, obj:object, value):
        obj.__dict__[self.name] = value