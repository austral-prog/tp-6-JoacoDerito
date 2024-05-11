def remove_elements(lst):
    if len(lst) >= 6:
        del lst[5]
    if len(lst) >= 5:
        del lst[4]
    if len(lst) >= 1:
        del lst[0]
    return lst

def add_elements(lst):
    lst.insert(0, 'Pink')
    lst.append('Yellow')
    return lst

def is_empty(lst):
    return len(lst) == 0

def check_lists(lst1, lst2):
    if len(lst1) >= 3 and len(lst2) >= 3:
        return lst1[2] == lst2[2]
    else:
        return False

def list_of_lists(lst):
    modified_list = []
    for sub_list in lst:
        if len(sub_list) >= 2:
            modified_list.append(sub_list[:2])
        if len(sub_list) >= 4:
            modified_list.append(sub_list[1:4])
        if len(sub_list) >= 2:
            modified_list.append(sub_list[-2:])
    return modified_list

sample_input_1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(remove_elements(sample_input_1))  

sample_input_2 = ['Red', 'Green', 'White', 'Black']
print(add_elements(sample_input_2)) 

sample_input_3 = []
print(is_empty(sample_input_3)) 

sample_list1_1 = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
sample_list2_1 = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
print(check_lists(sample_list1_1, sample_list2_1))

sample_list1_2 = ['Black', 'Pink', 'Green', 'White']
sample_list2_2 = ['Red', 'Green', 'Yellow', 'Black', 'Pink']
print(check_lists(sample_list1_2, sample_list2_2))

sample_list_of_lists = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
print(list_of_lists(sample_list_of_lists)) 
