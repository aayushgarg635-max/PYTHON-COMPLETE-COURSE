# tuples are immutables,uses()
a = (1,2,4,6,8,9)
print(a)
print(type(a)) #class'tuple'
# count(x)-how many times x appeared
no = a.count(45)
print(no) # 0 as 45 is not in the tuple
#index(x)- first index of x
i=a.index(4)
print(i)
# len()- length of tuple
print(len(a))
b =(2,3,4,5,67,8,9)
print(b)
print(type(b))
no=b.count(5) #1
print(no) #7
print(len(b))
# index with duplicates
t = ("a", "b", "c", "b")
t.index("b")      # 1
t.index("b", 2)   # 3
print(t.index("b")) # will print 1
print(t.index("b",2)) # will print 3
