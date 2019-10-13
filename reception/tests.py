x = 10
expr = """
z = 30
sum = z
print(sum)
"""


def func():
    y = 20
    exec(expr)
    # exec(expr, {'x': 1, 'y': 2})
    # exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})


func()
c=[22,33]
d=[55,66] #循环引用`
c.append(d)#c的引用+1=2
d.append(c)#d的引用+1=2
