##It compares every index like   [2,1,4,3]-------Firstly 2 compare with 1 bcz of greater 1 is moved towards left and 2 is on right
# [1,2,4,3]

def bubblesort(list):

    listed=len(list)
    isSorted=False
    while not isSorted:
        isSorted=True
        for eachvalue in range(0,listed-1):
            if list[eachvalue]>list[eachvalue+1]:
                isSorted=False
                temp=list[eachvalue]
                list[eachvalue]=list[eachvalue+1]
                list[eachvalue+1]=temp
    print(list)
listed=[3,2,5,4,6]
bubblesort(listed)
# print(list)