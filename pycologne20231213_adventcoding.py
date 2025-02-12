from itertools import groupby


def day13():
    f=open('day13.dat','r')
    content=f.read()

    data=content.split("\n\n")
    #remove empty row from last pattern
    data[-1]=data[-1][0:len(data[-1])-1]

    # analyse data
    sum_horizontal=0
    sum_vertical=0

    print(len(data))
    for sd in data:
        sl=sd.split("\n")
        print("\n".join(sl))

        #check for horizontal mirror lines
        for idx in range(1,len(sl)):
            r = sl[idx:]
            l = sl[idx-1::-1] #reversed
            if all(s1==s2 for s1,s2 in zip(l,r)):
                sum_horizontal+=idx

        # transpose
        print("Transpose: ")
        sl = transpose(sl)
        print("\n".join(sl))

        #check for vertical mirror lines
        for idx in range(1,len(sl)):
            r = sl[idx:]
            l = sl[idx-1::-1] #reversed
            if all(s1==s2 for s1,s2 in zip(l,r)):
                sum_vertical+=idx

    print(sum_horizontal*100+sum_vertical)


def transpose(string_array):

    rows= len(string_array)
    cols = len(string_array[0])
    print(rows)
    print(cols)


    return ["".join([string_array[l][i] for l in range(rows)]) for i in range(cols)]


if __name__ == '__main__':
    day13()