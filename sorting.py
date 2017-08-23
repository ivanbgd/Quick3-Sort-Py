import sys
import random

def partition3(a, l, r):
    x = a[l]
    j, o = l, l
    for i in range(l+1, r+1):
        if a[i] < x:
            o += 1
            a[i], a[o] = a[o], a[i]
            a[j], a[o] = a[o], a[j]
            j += 1
        elif a[i] == x:
            o += 1
            a[i], a[o] = a[o], a[i]
        else:
            continue
    if j > l:
        a[l], a[j-1] = a[j-1], a[l]
    else:
        a[l], a[j] = a[j], a[l]
    return j, o

def randomized_quick_sort3(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort3(a, l, m1 - 1)
    randomized_quick_sort3(a, m2 + 1, r)


if __name__ == '__main__':
    #input = sys.stdin.read()
    input = "5\n2 3 9 2 2"  # Correct output is: 2 2 2 3 9.
    #input = "13\n6 2 3 4 2 6 8 9 2 6 5 6 8"

    input = list(map(int, input.split()))
    n = input[0]
    a = input[1:]

    randomized_quick_sort3(a, 0, n - 1)
    #a.sort();      # This is TimSort from Python Standard Library.

    for x in a:
        print(x,)
    
    print(a)
    print()