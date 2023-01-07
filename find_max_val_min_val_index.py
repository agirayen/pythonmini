list = [23, 76, 45, 20, 70, 65, 15, 54]

def find_max_val_index(x):
    max_index=0
    current_index=1
    while current_index < len(x):
        if x[current_index] > x[max_index]:
            max_index=current_index
        current_index=current_index+1
    return max_index    
    
print(find_max_val_index(list))

def find_mix_val_index(x1):
    min_value=0
    current_index=1
    while current_index < len(x1):
        if x1[current_index]<x1[min_value]:
            min_value=current_index
        current_index=current_index+1
    return min_value
print(find_mix_val_index(list))
