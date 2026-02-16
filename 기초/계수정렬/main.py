import sys


# N = int(sys.stdin.readline())
count = [0]*1001
numbers = list(map(int, sys.stdin.readline().split()))

for number in numbers:
    count[number] += 1

for i in range(1001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i, end=' ')
            
