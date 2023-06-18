# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()

print('P', 'Y', 'Y', 'H', 'O', 'N', sep='\t')

print("aa", end='')
print("bb")

import sys

print('Learn Python', file=sys.stdout)

print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 2))
print('{1} {0}'.format('one', 2))

print()

print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % 'nice')
print('{:10}'.format('nice'))

print('{:<10}'.format('nice'))
print('{:$>10}'.format('nice'))
print('{:$<10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % 'nice')
print('%.5s' % 'pythonstudy')
print('%5s' % 'pythonstudy')
print('{:10.5}'.format('pythonstudy'))

print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))
print('%4d' % 42, '\'%4d\'')
print('%04d' % 42, '\'%04d\'')
print('{:4d}'.format(42))

print('%f' % 3.14132323)
print('%1.8f' % 3.14132323)
print('%1.18f' % 3.14132323)
print('{:f}'.format(3.14132323))

print('%06.2f' % 3.141592653589793)
print('%006.2f' % 3.141592653589793)
print('%06.2f' % 3.141592653589793)
print('{:06.2f}'.format(3.141592653589793))
print(f'{3.141592653589793:06.2f}')

print('\000')
print('\"')
print('\'')
print('\\')