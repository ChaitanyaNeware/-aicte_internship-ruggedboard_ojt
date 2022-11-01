def returnSum(myDict):
 

    list = []

    for i in myDict:

        list.append(myDict[i])

    final = sum(list)
 

    return final
 
 
# Driver Function

dict = ("Enter:")

print("Sum :", returnSum(dict))