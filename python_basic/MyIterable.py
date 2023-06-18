import collections.abc

class MyIterable:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def __iter__(self):
        self.index = -1  # iterator 초기 상태 설정
        return self  # iterator 객체 반환

    def __next__(self):
        self.index += 1  # 다음 요소로 이동
        if self.index < len(self.data):  # 아직 반환할 요소가 남아 있는 경우
            return self.data[self.index]  # 현재 요소 반환
        else:  # 더 이상 반환할 요소가 없는 경우
            raise StopIteration  # 예외 발생


my_iterable = MyIterable()
my_iterable.add(1)
my_iterable.add(2)
my_iterable.add(3)

print(isinstance(my_iterable, collections.abc.Iterable))
for item in my_iterable:
    print(item)  # 출력: 1, 2, 3