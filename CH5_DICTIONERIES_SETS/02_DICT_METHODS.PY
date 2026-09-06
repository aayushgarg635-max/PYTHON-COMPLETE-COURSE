marks={
    "harry": 100,
    "rohan":40,
    "sohan":23
}
print(marks.items())  # FIRST METHOD
print(marks.keys()) # SECOND
print(marks.values()) # THIRD 
marks.update({"aayush":98})
print(marks)
print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.update({"haary":99}))
print(marks)

d = {} # EMPTY DICTIONARY



print(marks.get("aayush"))
print(marks.get("shivam")) # RETURNS NONE
# print(marks[harry2]) # WILL GIVE AN ERROR
#  # methods got from AI
#  user = {"name": "Alice", "role": "Admin"}
# print(user.keys())    # dict_keys(['name', 'role']) 
# print(user.values())  # dict_values(['Alice', 'Admin'])
# print(user.items())   # dict_items([('name', 'Alice'), ('role', 'Admin')])
