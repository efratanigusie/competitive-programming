def countSwaps(a):
    n = len(a)
    count = 0
    for i in range( 0,n):

        for j in range(0, n - 1):

            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                count=count+1
    print("Array is sorted in {} swaps.".format(count))
    print("First Element: {}".format(a[0]))
    print("First Element: {}".format(a[n - 1]))
countSwaps([9,0,3])
