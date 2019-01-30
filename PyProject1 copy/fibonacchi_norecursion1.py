n = 0
def fibonacci(n):
    n = int(input('Which Fibonacci number you want to compute? Type here: '))
    if n == 0:
        return n, 0
    elif n == 1:
        return n, 1
    else:
        Fn_min_2 = 0
        Fn_min_1 = 1
        for i in range(1,n-1):
            Fn_min_2, Fn_min_1 = Fn_min_1, Fn_min_2 + Fn_min_1
        Fn = Fn_min_2 + Fn_min_1
        return n, Fn
n, Fn = fibonacci(n)
print('The ' + str(n) + '. Fibonacci number is = ' + str(Fn))
print('The ' + str(n) + '. Fibonacci number is ' + str(len(str(Fn))) + ' digits long')
exit()