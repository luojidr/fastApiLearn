from typing import List, Tuple, Dict, Any, Union, Optional, TypeVar, Callable, Sequence

# 列表，通常指定相同类型的元素
List[int]  # 整型
List[str]  # 字符串
List[float]  # 浮点型
List[bool]  # 布尔型
List[List[int]]  # 整型列表
List[Tuple[int, str]]  # 包含整型和字符串的元组
List[Any]  # 任何类型的袁旭
List[Union[int, str]]  # 联合类型，可以是整型或者字符串

Dict[str, int]  # 字典，键为字符串，值为整型
Dict[str, List[int]]  # 字典，键为字符串，值为整型列表
Dict[str, Tuple[int, str]]  # 字典，键为字符串，值为包含整型和字符串的元组
Dict[str, Any]  # 字典，键为字符串，值为任何类型的袁旭
Dict[str, Union[int, str]]  # 字典，键为字符串，值为联合类型，可以是整型或者字符串
Dict[str, Dict[str, int]]  # 字典，键为字符串，值为字典，键为字符串，值为整型
Dict[str, Dict[str, List[int]]]  # 字典，键为字符串，值为字典，键为字符串，值为整型列表
Dict[str, Dict[str, Tuple[int, str]]]  # 字典，键为字符串，值为字典，键为字符串，值为包含整型和字符串的元组
Dict[str, Dict[str, Any]]  # 字典，键为字符串，值为字典，键为字符串，值为任何类型的袁旭
Dict[str, Dict[str, Union[int, str]]]  # 字典，键为字符串，值为字典，键为字符串，值为联合类型，可以是整型或者字符串
Dict[str, Dict[str, Dict[str, int]]]  # 字典，键为字符串，值为字典，键为字符串，值为字典，键为字符串，值为整型

Tuple[int, str]  # 包含整型和字符串的元组
Tuple[int, str, List[int]]  # 包含整型、字符串和整型列表的元组
Tuple[int, str, Tuple[int, str]]  # 包含整型、字符串和包含整型和字符串的元组的元组
Tuple[int, str, Any]  # 包含整型、字符串和任何类型的元组的元组
Tuple[int, str, Union[int, str]]  # 包含整型、字符串和联合类型，可以是整型或者字符串的元组的元组

# Union[a, b, c] 可以是 a, b, c 中的任意一种类型
Union[int, str]  # 整型或者字符串
Union[int, str, List[int]]  # 整型、字符串或者整型列表
Union[int, str, Tuple[int, str]]  # 整型、字符串或者包含整型和字符串的元组
Union[int, str, Any]  # 整型、字符串或者任何类型的元组

Optional[int]  # 可能是整型，也可能是 None
Optional[str]  # 可能是字符串，也可能是 None
Optional[List[int]]  # 可能是整型列表，也可能是 None
Optional[Tuple[int, str]]  # 可能是包含整型和字符串的元组，也可能是 None
Optional[Any]  # 可能是任何类型的元组，也可能是 None

# TypeVar 可以定义泛型类型
T = TypeVar('T')  # T 可以是任何类型
List[T]  # List[T] 可以是任何类型列表
Dict[str, T]  # Dict[str, T] 可以是字典，键为字符串，值为任何类型
Tuple[T, T]  # Tuple[T, T] 可以是包含两个相同类型的元组

# Callable[args, return] 可以定义函数类型
Callable[[int, str], int]  # 函数类型，参数为整型和字符串，返回值为整型
Callable[[int, str], List[int]]  # 函数类型，参数为整型和字符串，返回值为整型列表
Callable[[int, str], Tuple[int, str]]  # 函数类型，参数为整型和字符串，返回值为包含整型和字符串的元组
Callable[[int, str], Any]  # 函数类型，参数为整型和字符串，返回值为任何类型的元组
Callable[[int, str], Union[int, str]]  # 函数类型，参数为整型和字符串，返回值为联合类型，可以是整型或者字符串
Callable[[int, str], Dict[str, int]]  # 函数类型，参数为整型和字符串，返回值为字典，键为字符串，值为整型
Callable[[int, str], Dict[str, List[int]]]  # 函数类型，参数为整型和字符串，返回值为字典，键为字符串，值为整型列表
Callable[[int, str], Dict[str, Tuple[int, str]]]  # 函数类型，参数为整型和字符串，返回值为字典，键为字符串，值为包含整型和字符串的元组

# Sequence[T] 可以定义序列类型 ，T 可以是任何类型
Sequence[int]  # 整型序列
Sequence[str]  # 字符串序列
Sequence[float]  # 浮点型序列
Sequence[bool]  # 布尔型序列
Sequence[Sequence[int]]  # 整型序列序列
Sequence[Sequence[str]]  # 字符串序列序列
Sequence[Sequence[float]]  # 浮点型序列序列
Sequence[Sequence[bool]]  # 布尔型序列序列
Sequence[Sequence[Sequence[int]]]  # 整型序列序列序列
Sequence[Sequence[Sequence[str]]]  # 字符串序列序列序列
Sequence[Sequence[Sequence[float]]]  # 浮点型序列序列序列
Sequence[Sequence[Sequence[bool]]]  # 布尔型序列序列序列
Sequence[Sequence[Sequence[Sequence[int]]]]  # 整型序列序列序列序列
# 举个Sequence的例子 可以定义一个序列类型，比如一个序列中的元素是字典，字典的键是字符串，值是整型
numbers_list: Sequence[int] = [1, 2, 3, 4, 5] # 整型列表
numbers_tuple: Sequence[int] = (1, 2, 3, 4, 5) # 整型元组
numbers_dict: Sequence[Dict[str, int]] = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}] # 字典列表
numbers_dict_tuple: Sequence[Dict[str, int]] = ({'a': 1, 'b': 2}, {'c': 3, 'd': 4}) # 字典元组
string_sequence: Sequence[str] = "hello" # 字符串序列
range_sequence: Sequence[int] = range(1, 6) # 整型范围



# 类型别名 可以定义类型别名
ListInt = List[int]  # 整型列表
DictStrInt = Dict[str, int]  # 字典，键为字符串，值为整型
TupleIntStr = Tuple[int, str]  # 包含整型和字符串的元组
UnionIntStr = Union[int, str]  # 联合类型，可以是整型或者字符串
OptionalInt = Optional[int]  # 可能是整型，也可能是 None
CallableIntStrInt = Callable[[int, str], int]  # 函数类型，参数为整型和字符串，返回值为整型
SequenceInt = Sequence[int]  # 整型序列

# 类型注解 可以定义类型注解
def add(a: int, b: int) -> int:
    return a + b
add(1, 2) # 3
