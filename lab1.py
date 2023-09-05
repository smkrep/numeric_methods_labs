eps = 0.01
def f(x):
    return (x-2)*((x-3)**2)*(x-7)

def find_root_dihotomy(a, b):
    if (f(a) * f(b) < 0):
        while abs(a-b) > eps:
            mid = (a+b)/2
            if (f(mid) * f(b) < 0):
                a = mid
                continue
            elif (f(a) * f(mid) < 0):
                b = mid
                continue
        return mid
    else:
        return -1

def find_root_simple_iteration():
    pass


a = float(input('Enter 1st number: '))
b = float(input('Enter 2nd number: '))

ans = find_root_dihotomy(a, b)
print('%.2f' % ans if ans != -1 else "No root has been found")