str1 = "python"
bool = True
list = [str1, bool]
print(list)

"""
+
-
*
/
// : 몫
% : 나머지
abs(x)
pow(x,y) / x ** y / 2 ** 3
"""

a = 3.
b = 6
c = .7
d = 12.7

print(type(a), type(b), type(c), type(d))

print(float(b))
print(int(c))
print(int(d))
print(int(True))
print(float(False))
print(complex(3))
print(complex('3'))
print(complex(False))

str1_t1 = ''
str2_t2 = ""
str3_t3 = str()

print(type(str1_t1), type(str2_t2), type(str3_t3))
print(len(str1_t1), len(str2_t2), len(str3_t3))

raw_s1 = r'D:\python\test'
print(raw_s1)

multi_str = \
'''
multi
line
string
'''
print(multi_str)

print(1)

def foo():
    multi_str = '''
multi
line
string
    '''
    print(multi_str)
foo()

str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing?"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print("y" in str_o1)
print('n' in str_o1)
print("P" not in str_o1)

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # __iter__

# iter 치고 엔터
for i in im_str:
    print(i)

print()
# 슬라이싱
str_sl = "Nice Python"
print(len(str_sl))
print(str_sl[0:3])
print(str_sl[5:])
print(str_sl[5:11])
print(str_sl[5:-1])
print(str_sl[:len(str_sl)])
print(str_sl[-1:])
print(str_sl[-1:3])
print(str_sl[1:9:2])
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1])

print()
a = 'z'
print(ord)
print(ord(a))
print(chr(122))