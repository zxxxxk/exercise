m=eval(input("输入第一个数："))
n=eval(input("输入第二个数："))
o=eval(input("输入第三个数："))
p=eval(input("输入第三个数"))



def sort_int(a, b, c, d):
    L = [a, b, c, d]
    L.sort(reverse=True)
    return L
 
w, x, y, z = sort_int(m, n ,o , p)
print(w, x, y, z)
