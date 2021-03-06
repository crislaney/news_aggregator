#parameters: two lists
#operation: compares the two lists
#return: returns True if more than 3 matches between lists, and false otherwise
def lists_overlap(list1, list2): #takes 2 lists
    overlap_bool = bool(set(list1) & set(list2))
    overlap_int = len(set(list1) & set(list2))
    
    if overlap_int > 2:
        return(True)
    else:
        return(False)
    
     #returns the overlap_int, which is the number of elements in both list1 and list2, and overlap_bool, a boolean (True means they have elements in common, False means they do not). 



