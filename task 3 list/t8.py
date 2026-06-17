#task 8. Плоский список с произвольной вложенностью

nested_list = [1,[2,3],[[4],[5,6]],7]

flat_list = []
stack = [nested_list]        

while stack:            
    element = stack.pop()  
    
    if type(element) == list:   

        for i in range(len(element) - 1, -1, -1):
            stack.append(element[i])

    else:                 
        flat_list.append(element)

print(flat_list)   # [1,2,3,4,5,6,7]