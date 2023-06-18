# tuple

a = ()
b = (1,)
c = (70, 75, 80, 85)
d = (1000, 10000, 'Ace', 'Base', 'Captain')
e = (1000, 10000, ('Ace', 'Base', 'Captain'))
f = (21.42, 'foobar', 3, 4, 'bark', False, 3.14159)


a = (5, 2, 3, 1, 4)
add__ = a.__add__((1,))
print(add__)
# 파이썬스럽지 않다

'''
python에서 import this 하면
Beautiful is better than ugly. 아름다움이 추한 것보다 낫다.
Explicit is better than implicit. 명확함이 함축된 것보다 낫다.
Simple is better than complex. 단순함이 복잡한 것보다 낫다.
Complex is better than complicated. 복잡함이 난해한 것보다 낫다.
Flat is better than nested. 단조로움이 중접된 것보다 낫다.
Sparse is better than dense. 여유로움이 밀집된 것보다 낫다.
Readability counts. 가독성은 중요하다.
Special cases aren't special enough to break the rules. 규칙을 깨야할 정도로 특별한 경우란 없다. Although practicality beats purity. 비록 실용성이 이상을 능가한다 하더라도.
Errors should never pass silently. 오류는 결코 조용히 지나가지 않는다. Unless explicitly silenced. 알고도 침묵하지 않는 한.
In the face of ambiguity, refuse the temptation to guess. 모호함을 마주하고 추측하려는 유혹을 거절하라. There should be one-- and preferably only one --obvious way to do it. 문제를 해결할 하나의 - 바람직하고 유일한 - 명백한 방법이 있을 것이다. Although that way may not be obvious at first unless you're Dutch. 비록 당신이 우둔해서 처음에는 명백해 보이지 않을 수도 있겠지만.
Now is better than never. 지금 하는 것이 전혀 안하는 것보다 낫다. Although never is often better than right now. 비록 하지않는 것이 지금 하는 것보다 나을 때도 있지만.
If the implementation is hard to explain, it's a bad idea. 설명하기 어려운 구현이라면 좋은 아이디어가 아니다. If the implementation is easy to explain, it may be a good idea. 쉽게 설명할 수 있는 구현이라면 좋은 아이디어일 수 있다. Namespaces are one honking great idea -- let's do more of those! 네임스페이스는 정말 대단한 아이디어다. -- 자주 사용하자!
'''
abc = dict([
    ('Name', 'dd'),('city', 'aa')
])