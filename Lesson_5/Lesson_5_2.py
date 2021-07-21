def function(x):
    if x < 0:
        return x * 2
    else:
        return x * 3


def main():
    for i in arange(-5, 5, 0.5):
        y = function(i)
        print('function(', i, ') =', y, sep='')


main()
