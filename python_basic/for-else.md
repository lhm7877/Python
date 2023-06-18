- https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops
- for else 보단 for completed나 for passed가 맞지 않나?
  - 파이썬 개발자들도 for - no break로 읽으라고 함
  - Here’s why (Hettinger):
> In 1991, “else” was the obvious choice because of the traditional way compilers implemented while-loops: pastebin.com/tY35CTJ4   
That is, “if I haven’t finished the loop, GOTO the body.”
He says if he had a time machine he could tell Guido in the future we’re all using structured programming so no one will find “else” intuitive; call it “nobreak” instead: https://m.youtube.com/watch?v=OSGv2VnC0go#
Guido says if he had a time machine he would not have included the feature at all: https://mail.python.org/pipermail/python-ideas/2009-October/...
This whole thing was Knuth’s idea, not Guido’s: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.103...