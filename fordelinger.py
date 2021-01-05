import math

def poisson(x: int, l):
    return (math.exp(-l)*l**x)/math.factorial(x)

def diskre_kumulativ(x: int, funk: str, l:float=0,):
    if funk == 'poisson':
        sum = 0
        for x in range(x+1):
            sum+=poisson(x, l)
        return sum

print('2a)\n', 1-diskre_kumulativ(x=20, l=15, funk='poisson'))
print('2b)\n', diskre_kumulativ(x=20, l=15, funk='poisson')-diskre_kumulativ(x=9, l=15, funk='poisson'))