## Iterable vs Iterator

* **Iterable**: `__iter__()` 메소드를 가지고 있으며 이 메소드를 통해 iterator를 반환하는 객체입니다. 파이썬의 대표적인 iterable 객체로는 list, tuple, string 등이 있습니다.
* **Iterator**: `__next__()` 메소드를 가지고 있는 객체입니다. 이 메소드는 데이터의 다음 항목을 반환합니다. 모든 데이터가 반환되었을 때는 `StopIteration` 예외를 발생시킵니다. Iterator는 `__iter__()` 메소드도 가지고 있으므로 iterable이기도 합니다.
### 사용자 정의 Iterable 클래스 만들기
사용자 정의 Iterable 클래스를 만드는 예시입니다.
```python
class MyIterable:
    def __init__(self):
        self.items = []
        
    def add(self, value):
        self.items.append(value)
        
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.items):
            result = self.items[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

```
위의 클래스는 이렇게 사용할 수 있습니다:
```python
my_iterable = MyIterable()
my_iterable.add('Hello')
my_iterable.add('World')

for item in my_iterable:
    print(item)  # Output: Hello, World

```
### Iterator 확인하기
디버깅 중에 `isinstance(my_iterable, collections.abc.Iterator)`를 사용하면 `my_iterable`이 iterator인지 확인할 수 있습니다. 이 구문은 Evaluate Expression이나 Watch에서 사용할 수 있습니다.