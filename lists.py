def remove_elements(list_to_remove_elements: list):
    del list_to_remove_elements[4: 6]
    del list_to_remove_elements[0:1]
    return list_to_remove_elements

def add_elements(list_to_add_elements: list):
    list_to_add_elements.insert(0, 'Pink')
    list_to_add_elements.append("Yellow")
    return list_to_add_elements

def is_empty(list_to_check):
    return not len(list_to_check)

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) < 3 or len(list_to_compare2) < 3:
        return False
    
    return list_to_compare2[2] == list_to_compare1[2]

def list_of_lists(list_of_lists_to_modify):
    newList = []

    lista1, lista2, lista3 = list_of_lists_to_modify[0],list_of_lists_to_modify[1],list_of_lists_to_modify[2]

    newList.append(lista1[:2])
    newList.append(lista2[1:4])
    newList.append(lista3[-2:])

    return newList
