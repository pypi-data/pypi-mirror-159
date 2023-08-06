class Sign:
    """ 标记，用于创建不冲突的常量 """
    def __init__(self, name:str) -> None:
        self.name = name

# 数据表列没有被使用
UNUSED = Sign('UnUsed')

# python类型对应的sqlite类型
PYTHON_TYPE_SQLITE = {
    None: "NULL",
    int: "INTEGER",
    float: "REAL",
    str: "TEXT",
    bytes: "BLOB"
}