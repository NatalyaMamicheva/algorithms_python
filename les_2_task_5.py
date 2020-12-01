for i in range(32, 128):
    print("%6d - %s" % (i, chr(i)), end=' ')
    if i % 10 == 0:
        print(i)
