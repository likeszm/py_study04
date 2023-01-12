#学习记录04-条件语句and方法



#布尔表达式测试
"""
print(" 1 == 2 :", 1 == 2 )
print(" 1 != 2 :", 1 != 2 )
print(" bool(1) :", bool(1) )
print(" not 1 :", not 1 )
print(" 1 <= 1 :", 1 <= 1 )
print(" 1 >= 0 :", 1 >= 0 )
print(" true and false :", True and False )
print(" true and true :", True and True)
print(" true or false :", True or False )
print(" true or true :", True or True)
print(" not true : ", not True )
"""

#if
"""
if 1 == 2 :
    print("1 == 2")
if 1 != 2 :
    print("1 != 2")
"""

#if else
"""
if 1 != 2 :
    print("1!=2")
else :
    print("1==2")
"""

#多分支
"""
a = 9
if a == 0 :
    print("a = ", a)
elif a == 1:
    print("a = ", a)
elif a == 2 :
    print("a = ", a)
elif a == 3 :
    print("a = ", a)
elif a == 4 :
    print("a = ", a)
else :
    print("l a = ", a)
"""

#号码获取
"""
phone = input("请输入电话号码:")
if len(phone) == 11 :
    if phone[0] == '1' :
        if phone.isdigit() :
            print("成功获取号码")
        else:
            print("您输入的不全是数字!")
    else:
        print("号码不是1开头!")
else :
    print("您输入的号码不是11位")
"""

#题目
"""
def f1():
    print('f1')
    return True

def f2():
    print('f2')
    return True

if f1():
    print("a")
elif f2():
    print("b")
else:
    print("c")
"""

#字符串的方法
"""
print('"abcdefgaaa".count("a") =',"abcdefgaaa".count('a'))
print("'ABC'.find('C') =", 'ABC'.find('C'))
str1 = 'ABC|CDE|DEF'
list1 = str1.split('|')
print( "str1 = " + str1)
print("list1 = " , list1)
"""
Str2 = """1.line1
2.line2
3.line3"""
"""
list2 = Str2.splitlines()
print("str2 = "+ Str2)
print("list2 = ",list2)
print("'|'.join(['S','A','S']) =", '|'.join(['S','A','S']))
print("'  A  B  '.strip() =", '  A  B  '.strip())
print("'  A  B  '.lstrip() =", '  A  B  '.lstrip())
print("'  A  B  '.rstrip() =", '  A  B  '.rstrip())
print("'ABCDS'.replace('S','E') =" , 'ABCDS'.replace('S','E'))
print("'ABC'.startswith('A') =", 'ABC'.startswith('A'))
print("'ABC'.endswith('A') =", 'ABC'.endswith('A'))
print("'ABC'[::-1] = ", 'ABC'[::-1])
"""


#列表的方法
"""
list1 = [1,2.0,'3',[4,0]]
print("list1 = " , list1)
list1.append('test')
print("list1 = " , list1)
list1.insert(0,'000')
print("list1 = " , list1)
a = list1.pop(-1)
print("a = ",a)
print("list1 = " , list1)
list2 = ['a','a','b','b','c','c']
print("list2 = " , list2)
list2.remove('b')
print("list2 = " , list2)
list2.reverse()
print("list2 = " , list2)
num = list2.index('c')
print("num = ", num)
list2.sort()
print("list2 = " , list2)
"""

