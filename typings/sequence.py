"""
要成为 Sequence 类型，数据结构需要实现 collections.abc.Sequence 协议。Sequence 是一个抽象基类（ABC），定义了序列类型应实现的方法和属性。具体来说，要实现 Sequence 协议，类型必须实现以下几个方法和属性：

__getitem__(self, index): 支持索引访问。
__len__(self): 返回序列的长度。
__contains__(self, item): 支持成员测试 (in 操作符)。
__iter__(self): 返回一个迭代器。
__reversed__(self): 返回一个反向迭代器。
index(self, value, start, stop): 返回值在序列中的索引。
count(self, value): 返回值在序列中出现的次数。
下面是一个简单的例子，实现了自定义的 Sequence：
"""

from collections.abc import Sequence


class CustomSequence(Sequence):
    def __init__(self, data):
        self._data = data

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item in self._data

    def __iter__(self):
        return iter(self._data)

    def __reversed__(self):
        return reversed(self._data)

    def index(self, value, start=0, stop=None):
        if stop is None:
            stop = len(self._data)
        return self._data.index(value, start, stop)

    def count(self, value):
        return self._data.count(value)


# 使用例子
custom_sequence = CustomSequence([1, 2, 3, 4, 5])

print(len(custom_sequence))  # 输出 5
print(custom_sequence[2])  # 输出 3
print(3 in custom_sequence)  # 输出 True
print(list(iter(custom_sequence)))  # 输出 [1, 2, 3, 4, 5]
print(list(reversed(custom_sequence)))  # 输出 [5, 4, 3, 2, 1]
print(custom_sequence.index(3))  # 输出 2
print(custom_sequence.count(3))  # 输出 1

