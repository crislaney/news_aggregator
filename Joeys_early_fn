def final_list_maker(fin_list,master_list):
    checklist = []
    c = 0
    for i in fin_list:
        checklist.append(rob(i))
    for k in master_list[1]:
        str_list = rob(k)
        result = griffin(checklist, str_list)
        if result == False:
            c = c + 1
            fin_list.append(k)
            if c > 4:
                c = 0
                break
    for k in master_list[2]:
        str_list = rob(k)
        if result == False:
            c = c + 1
            fin_list.append(k)
            if c > 4:
                c = 0
                break
    return(fin_list)

def rob(i):
    return i

def griffin(checklist, str_list):
    for i in checklist:
        if i == str_list:
            return True
    return False
        

def main():
    fin_list = [4,3,2,7,8]
    master_list = [[4,3,2,7,8,9,11,111,12],[4,12,22,44,55,23,44,23,66],[7,12,342,543,675,987,201]]
    fin_list = final_list_maker(fin_list, master_list)
    print(fin_list)
main()
    
