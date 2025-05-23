def remove_elements(elements_given):
    if len(elements_given) > 5:
        del elements_given[0] 
        del elements_given[3]
        del elements_given[3]
    elif len(elements_given) == 5:
        del elements_given [0]
    elif len(elements_given) == 4:
        del elements_given [0]
    return elements_given

def add_elements(las_cosas):
    las_cosas.insert(0, "Pink")
    las_cosas.append("Yellow")
    return las_cosas

def is_empty(list_to_check):
 return len(list_to_check) == 0

def check_lists(list1, list2):
    if len(list1) < 3 or len(list2) < 3:
        return False
    elif list1[2] == list2[2]:
        return True
    else:   
        return False

def list_of_lists(list_of_lists_to_modify):
    #Separar la listas para simplificar
    list1 = list_of_lists_to_modify[0]
    list2 = list_of_lists_to_modify[1]
    list3 = list_of_lists_to_modify[2]

    if len(list1) > 2:
        list1_new = [list1[0], list1[1]]
    else:
        list1_new = list1

    len2 = len(list2)
    if len2 == 2:
        list2_new = [list2[1]]
    elif len2 == 3:
        list2_new = [list2[1], list2[2]]
    elif len2 >= 4:
        list2_new = [list2[1], list2[2], list2[3]]
    else:
        list2_new = []

    len3 = len(list3)
    if len3 > 2:
        list3_new = [list3[-2], list3[-1]]
    else:
        list3_new = list3

    return [list1_new, list2_new, list3_new]        
