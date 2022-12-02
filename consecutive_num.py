def is_consecutive(a_list):
    #return a boolean if the numbers are consecutive
    for num in range(len(a_list)-1):
        if a_list[num] + 1 == a_list[num+1]:
            continue
        else:
            return False
    
    return True