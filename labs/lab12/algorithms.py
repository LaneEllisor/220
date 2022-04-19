def read_data(filename):
    file = open(filename, 'r')
    words = file.read()
    list = words.replace('\n', ' ').split(" ")
    return list

def is_in_linear(search_val, values):
    count = 0
    while count < len(values) and search_val != values[count]:
        count += 1 
        return count < len(values)
 
def find_and_remove_first(list, value):
    list_index = list.index(value)
    list.pop(list_index)
    list.insert(list_index, 'Lane')
    return list
