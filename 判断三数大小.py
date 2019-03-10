m=eval(input("输入第一个数："))
n=eval(input("输入第二个数："))
o=eval(input("输入第三个数："))



def sort_int(a, b, c):
    L = [a, b, c]
    L.sort()
    return L
 
x, y, z = sort_int(m, n, o)
print(x, y, z)
