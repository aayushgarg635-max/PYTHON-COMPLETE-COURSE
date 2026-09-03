letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>" , "Harry").replace ("<|Date|>" , "24 july 2027"))