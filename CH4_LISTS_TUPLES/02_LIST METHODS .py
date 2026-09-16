# lists can have mixed datatypes and indexing
freinds = ["apple","orange",276,True,False , "variables"]
print(freinds[0]) #apple
#append()-add items at the end
freinds.append("harry potter")
print(freinds)
#sort()-sorts in ascending manner
l1=[2,44,35,24,97]
l1.sort()
print(l1)
# reverse in place
l2=[2,44,35,24,97]
l2.reverse()
print(l2)
# insert(index,value)-inserts at given index
l3=[2,44,35,24,97]
l3.insert(2,245) # INSERT 245 IN THE LIST AT INDEX 2
print(l3)
#remove(value) removes first occurence of value 
l3.pop(2)
print(l3)
l3.remove(44)
print(l3)

