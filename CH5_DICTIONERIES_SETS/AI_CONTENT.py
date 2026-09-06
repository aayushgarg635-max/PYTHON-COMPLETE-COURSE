fruits = {"apple", "banana"}
fruits.add("orange")      # {"apple", "banana", "orange"}
fruits.discard("banana")  # {"apple", "orange"}
fruits.discard("grape")   # Does nothing, no error thrown
