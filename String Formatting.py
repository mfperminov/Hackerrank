def print_formatted(number):
    # your code goes here    
    width=len(str(bin(number)))-2
    for i in range(1,number+1):
        for base in 'doXb':
            print('{0:{width}{base}}'.format(i, base=base, width=width), end=' ')
        print('')