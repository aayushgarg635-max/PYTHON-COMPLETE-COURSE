#1 Creating a set - duplicates are automatically removed
s = {1,2,4,5,54,5,6,2,2,2}
print(s) # output:{1,2,4,5,6,54}
#2 Adding elements
s.add(24)
s.add(12)
print(f"after adding 24 and 12 :{s}")
#3 Removing - remove() and discard()
s.remove(4)
print(f"after removing 4:{s}")
#dicard():it will not give error if value not found
s.discard(10)
print(f"after discard:{s}")
# Len and type.
print(f"length of set is:{len(s)}")
print(f" type of s:{type(s)}")
# clear:empties the set
s.clear()
print(f" after clear:{s}")
# update - updates the set 
skills = {"Python", "HTML"}
new_skills = ["CSS", "JavaScript", "Python"]  # A list

skills.update(new_skills)
print(skills)  # {'Python', 'HTML', 'CSS', 'JavaScript'}



