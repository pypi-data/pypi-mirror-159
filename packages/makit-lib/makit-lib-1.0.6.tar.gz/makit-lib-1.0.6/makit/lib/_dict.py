# coding=utf-8

"""
@Author: LiangChao
@Email: liang20201101@163.com
@Created: 2022/1/10
@Desc: 
"""
import re


class AttrDict(dict):
    def __getattr__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            return self.get(item)

    def to_query_str(self):
        """
        将字典转换为查询字符串
        :return:
        """
        return '&'.join([k + '=' + str(v) for k, v in self.items()])

    def from_query_str(self, query_str):
        """
        从查询字符串转换并更新键值
        :param query_str:
        :return:
        """
        query_str = query_str + '&'
        p = re.compile(r'[^=&]+=[^=]+(?=&)')
        _list = p.findall(query_str)
        for item in _list:
            _arr = item.split('=', maxsplit=1)
            self[_arr[0]] = _arr[1]
        return self


Dict = AttrDict
