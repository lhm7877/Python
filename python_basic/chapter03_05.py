# dictionary

'''
dict.__init__() 설명

def __init__(self, seq=None, **kwargs): # known special case of dict.__init__
    """
    dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)
    # (copied from class doc)
    """
    pass


1. 아무런 인자도 제공하지 않은 경우: 이 경우, 빈 사전이 생성됩니다.
2. mapping 객체를 제공한 경우: 이 경우, 제공된 mapping 객체의 키-값 쌍을 사용하여 사전이 생성됩니다.
3. iterable 객체를 제공한 경우: 이 경우, iterable 객체의 각 요소를 키-값 쌍으로 사용하여 사전이 생성됩니다. iterable 객체의 각 요소는 두 개의 요소를 가진 iterable이어야 합니다.
4. 키워드 인자를 제공한 경우: 이 경우, 각 키워드 인자의 이름을 키로, 값을 값으로 사용하여 사전이 생성됩니다.

# 방법 1: 빈 사전 생성
d1 = dict()
print(d1)  # 출력: {}

# 방법 2: mapping 객체를 사용하여 사전 생성
d2 = dict({'one': 1, 'two': 2})
print(d2)  # 출력: {'one': 1, 'two': 2}

# 방법 3: iterable 객체를 사용하여 사전 생성
d3 = dict([('one', 1), ('two', 2)])
print(d3)  # 출력: {'one': 1, 'two': 2}

# 방법 4: 키워드 인자를 사용하여 사전 생성
d4 = dict(one=1, two=2)
print(d4)  # 출력: {'one': 1, 'two': 2}
'''

a = dict(
    Name='NiceMan',
    City='Seoul'
)
# print(a.popitem())
# print(a)
# print(a.popitem())
# print(a)
# print(a.popitem())
# print(a)
# print(a.popitem())
# print(a)
a.update(address="dj")
print(a)