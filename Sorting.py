def sorting(list):
    temp=()
    i=0
    while i <len(list):

        j=i+1

        while j<len(list):

            if list[i]>list[j]:
                temp=list[i]

                list[i]=list[j]

                list[j]=temp

            j=j+1
        i=i+1
    print(list)
list=[2,1,4,3]
sorting(list)


