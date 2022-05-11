def bb(dd):
    l=list()
    while dd!=0:
        i=dd%2
        dd//=2
        l.append(i)
    l.reverse()
    for i in l:
        print(i,end=" ")

number=int(input('enter number'))
bb(number)
