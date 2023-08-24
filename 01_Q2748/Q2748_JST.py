# Bottom Up 방식

# import sys

# n = int(sys.stdin.readline())

# d = [0] * 91

# d[0] = 0
# d[1] = 1

# for i in range (2,n+1):
#     d[i] = d[i-1] + d[i-2]

# print(d[n])


'''
    [효율성]
    -메모리 : 31256 KB
    -시간 : 40 ms
'''



# Top Down 방식
import sys

d = [0]*91

def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(int(sys.stdin.readline())))

'''
    [효율성]
    -메모리 : 31256 KB
    -시간 : 44 ms
'''