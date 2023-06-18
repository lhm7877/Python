x = 50
y = 100
text = 308276567
n = 'Lee'

ex1 = 'n = %s, s= %s, sum=%d' % (n, text, x+y)
print(ex1)

ex2 = 'n = {n}, s= {s}, sum={sum}'.format(n=n, s=text, sum=x+y)
print(ex2)

ex3 = f'n = {n}, s= {text}, sum={x + y}'
print(ex3)

m = 1000000000

print(f'm : {m:,}')

print()
# ^ : 가운데, < : 왼쪽, > : 오른쪽

t = 22
print(f"t : {t:10}")
print(f"t center : {t:^10}")
print(f"t center : {t:^010}")
print(f"t left : {t:<10}")
print(f"t right : {t:>10}")

print()

print(f"t center : {t:-^10}")
print(f"t center : {t:^-10}")
print(f"t center : {t:^010}")
print(f"t center : {t:0^10}")

print()

t2 = 'hi'
print(f"t center : {t2:-^10}")
# print(f"t center : {t2:^-10}")
print(f"t center : {t2:^010}")
print(f"t center : {t2:0^10}")

