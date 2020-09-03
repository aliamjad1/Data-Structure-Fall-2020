#In this sortion we sort from right to left ... Like this
# [3,2,5,4]   ------- [2|3,5,4] 0 index element asa he chor dain ga

def insertSort(list):
    lenoflist=len(list)
    rangeoflist=range(1,lenoflist)
    for i in rangeoflist:
        isSorted=list[i]
        while list[i-1]>isSorted and i>0:
            temp=list[i]
            list[i]=list[i-1]
            list[i-1]=temp
            i=i-1
        print(list)
list=[3,2,5,4]
insertSort(list)