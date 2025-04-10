braket = []

c_list = []

iv = "((a+b)+c)*((a-b)-c)"

for loc, char in enumerate(iv) :
    if char == "(" :
        c_list.append(loc)
    
    if char == ")" :
        start = c_list.pop()
        braket.append([start,loc])
        
        

        
print((braket))