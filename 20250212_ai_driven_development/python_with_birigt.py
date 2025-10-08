def print_multiplication_table(birgit):
    """
    print the multiplication table for the given range
    on the screen
    :param rng:
    :return:
    """

    for row in range(birgit[0], birgit[1] + 1):
        for col in range(birgit[0], birgit[1] + 1):
            print(row * col, end=' ')
        print()


dictionary={'January':100, 'February':200, 'March':300,'April':400, 'May':500, 'June':600, 'July':700, 'August':800, 'September':900, 'October':1000, 'November':1100, 'December':1200}

dictionary={'A':14, 'B':15, 'C':16,'D':45, 'E':46, 'F':47, 'G':48, 'H':49, 'I':50, 'J':51, 'K':52, 'L':53, 'M':54, 'N':55, 'O':56, 'P':57, 'Q':58, 'R':59, 'S':60, 'T':61, 'U':62, 'V':63, 'W':64, 'X':65, 'Y':66, 'Z':67}


if __name__ == '__main__':
    print_multiplication_table([5,20])