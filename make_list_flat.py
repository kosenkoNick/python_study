dim_list = [[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]

def flattern(array : list):
    result = []
    for el in array:
        if type(el) == list:
            el = flattern(el)
            result += el
        else:
            result.append(el)

        
    return result